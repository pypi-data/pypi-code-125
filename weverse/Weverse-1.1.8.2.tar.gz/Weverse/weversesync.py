import json
import time
from typing import Optional, List

import requests
from .models import Community, Post as w_Post, Notification, Announcement
from . import WeverseClient, create_post_objects, create_community_objects, create_notification_objects, \
    create_comment_objects, create_media_object, iterate_community_media_categories, create_announcement_object, \
    InvalidCredentials, LoginFailed, InvalidToken, NoHookFound, check_expired_token


class WeverseClientSync(WeverseClient):
    r"""
    Synchronous Weverse Client that Inherits from :ref:`WeverseClient`.

    Parameters
    ----------
    kwargs:
        Same as :ref:`WeverseClient`.


    Attributes are the same as :ref:`WeverseClient`.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, create_old_posts=False, create_notifications=True, create_media=False):
        """Creates internal cache.

        This is the main process that should be run.

        :parameter create_old_posts: (:class:`bool`) Whether to create cache for old posts.
        :parameter create_notifications: (:class:`bool`) Whether to create/update cache for old notifications.
        :parameter create_media: (:class:`bool`) Whether to create/update cache for old media.

        :raises: :class:`Weverse.error.InvalidToken`
            If the token was invalid.
        :raises: :class:`Weverse.error.BeingRateLimited`
            If the client is being rate-limited.
        :raises: :class:`Weverse.error.LoginFailed`
            Login process had failed.
        :raises: :class:`Weverse.error.InvalidCredentials`
            If the user credentials were invalid or not provided.
        """
        try:
            if not self.web_session:
                self.web_session = requests.Session()

            if not self._login_info_exists and not self._token_exists:
                raise InvalidCredentials

            if self._login_info_exists:
                self._try_login()

            if not self.check_token_works():
                raise InvalidToken

            # create all communities that are subscribed to
            self.create_communities()  # communities should be created no matter what

            # create and update community artists and their tabs
            self.create_community_artists_and_tabs()

            # create and update user notifications
            if create_notifications:
                self.get_user_notifications()

            for community in self.all_communities.values():
                # load up posts
                if create_old_posts:
                    self.create_posts(community)

                if create_media:
                    self.create_media(community)

            self.cache_loaded = True

            if self._hook:
                if self.verbose:
                    print("Starting Notification Loop for Weverse Client.")
                self._start_loop_for_hook()
        except Exception as err:
            raise err

    def _start_loop_for_hook(self):
        """
        Start checking for new notifications in a new loop and call the hook with the list of new Notifications
        This will also create the posts associated with the notification so they can be used efficiently.
        """
        if not self._hook:
            raise NoHookFound

        self._hook_loop = True
        while self._hook_loop:
            time.sleep(30)
            new_notifications = self.update_cache_from_notification()
            if not new_notifications:
                continue

            self._hook(new_notifications)

    def _try_login(self):
        """
        Will attempt to login to Weverse and set refresh token and token.
        """
        self._login(self.__process_login)

    def __process_login(self, login_payload: dict):
        """
        Will process login credentials and set refresh token and token.
        Parameters
        ----------
        login_payload: dict
            The client's login payload
        """
        with self.web_session.post(url=self._login_url, json=login_payload) as resp:
            if self.check_status(resp.status_code, self._login_url):
                data = json.loads(resp.text)
                refresh_token = data.get("refresh_token")
                token = data.get("access_token")
                if refresh_token:
                    self._set_refresh_token(refresh_token)
                if token:
                    self._set_token(token)
                self.expired_token = False
                return
        raise LoginFailed

    def _refresh_token(self):
        """
        Refresh a token while logged in.
        """
        with self.web_session.post(url=self._login_url, json=self._refresh_payload) as resp:
            if self.check_status(resp.status_code, self._login_url):
                data = json.loads(resp.text)
                token = data.get("access_token")
                if token:
                    self._set_token(token)
                self.expired_token = False
                return
        self._set_refresh_token("")  # resetting refresh token.
        self._try_login()  # will attempt to log in again.

    @check_expired_token
    def _check_new_notifications(self) -> List[Notification]:
        """
        Checks and returns new notifications.
        Compares with the already existing notifications.
        This will also create the posts associated with the notification so they can be used efficiently.
        This is a coroutine and must be awaited.

        Returns
        -------
        A list of new Notifications.: List[:class:`models.Notification`]
        """
        all_new_notifications = []

        if self.check_new_user_notifications():

            all_new_notifications = self.get_new_notifications()
        return all_new_notifications

    @check_expired_token
    def create_media(self, community: Community):
        """Paginate through a community's media and add it to object cache.

        :parameter community: :ref:`Community` the posts exist under.
        """
        media_tab_url = f"{self._api_stream_url}{community.id}/{self._api_media_tab}"
        with self.web_session.get(media_tab_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, media_tab_url):
                response_text_as_dict = json.loads(resp.text)
                media_objects, photo_media_dicts = iterate_community_media_categories(response_text_as_dict)

                # This endpoint does NOT give us any information about the photos, therefore we must make
                # a separate api call to retrieve proper photo information for the photo media.
                for media in photo_media_dicts:
                    media_obj = self.fetch_media(community.id, media.get("id"))
                    if media_obj:
                        media_objects.append(media_obj)

                self._add_media_to_cache(media_objects)

    @check_expired_token
    def create_communities(self):
        """Get and Create the communities the logged in user has access to."""
        with self.web_session.get(self._api_communities_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, self._api_communities_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                user_communities = response_text_as_dict.get("communities")
                self.all_communities = create_community_objects(user_communities)

    @check_expired_token
    def create_community_artists_and_tabs(self):
        """Create the community artists and tabs and add them to their respective communities."""
        for community in self.all_communities.values():
            url = self._api_communities_url + str(community.id)
            with self.web_session.get(url, headers=self._headers) as resp:
                if self.check_status(resp.status_code, url):
                    response_text = resp.text
                    response_text_as_dict = json.loads(response_text)
                    self.process_community_artists_and_tabs(community, response_text_as_dict)
                    for artist in community.artists:
                        self.all_artists[artist.id] = artist
                    for tab in community.tabs:
                        self.all_tabs[tab.id] = tab

    @check_expired_token
    def create_posts(self, community: Community, next_page_id: int = None):
        """Paginate through a community's posts and add it to object cache.

        :parameter community: :ref:`Community` the posts exist under.
        :parameter [OPTIONAL] next_page_id: Next Page ID (Weverse paginates posts).
        """
        artist_tab_url = self._api_communities_url + str(community.id) + '/' + self._api_all_artist_posts_url
        if next_page_id:
            artist_tab_url = artist_tab_url + "?from=" + str(next_page_id)
        with self.web_session.get(artist_tab_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, artist_tab_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                posts = create_post_objects(response_text_as_dict.get('posts'), community)
                for post in posts:
                    self.all_posts[post.id] = post
                    if post.photos:
                        for photo in post.photos:
                            self.all_photos[photo.id] = photo

                    if post.videos:
                        for video in post.photos:
                            self.all_videos[video.video_url] = video
                if not response_text_as_dict.get('isEnded'):
                    self.create_posts(community, response_text_as_dict.get('lastId'))

    @check_expired_token
    def create_post(self, community: Community, post_id) -> w_Post:
        """Create a post and update the cache with it. This is meant for an individual post.

        :parameter community: :ref:`Community` the post was created under.
        :parameter post_id: The id of the post we are needing to fetch.
        """
        post_url = self._api_communities_url + str(community.id) + '/posts/' + str(post_id)
        with self.web_session.get(post_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, post_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return (create_post_objects([response_text_as_dict], community, new=True))[0]

    @check_expired_token
    def get_user_notifications(self):
        """Get a list of updated user notification objects.

        :returns: List[:ref:`Notification`]
        """
        with self.web_session.get(self._api_notifications_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, self._api_notifications_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                self.user_notifications = create_notification_objects(response_text_as_dict.get('notifications'))
                for user_notification in self.user_notifications:
                    self.all_notifications[user_notification.id] = user_notification
                return self.user_notifications

    @check_expired_token
    def check_new_user_notifications(self):
        """Checks if there is a new user notification, updates the cache, and returns if there was.

        :returns: (:class:`bool`) Whether there is a new notification.

        This endpoint has been acting a bit off and not producing accurate results. It would be recommended to
        instantly get new notifications with :ref:`update_cache_from_notification` instead.
        """
        with self.web_session.get(self._api_new_notifications_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, self._api_new_notifications_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                has_new = response_text_as_dict.get('has_new')
                if has_new:
                    # update cache
                    # Not that cache_loaded necessarily matters here,
                    # but just in case other checks are happening concurrently.
                    self.cache_loaded = False
                    self.update_cache_from_notification()
                    self.cache_loaded = True
                return has_new

    @check_expired_token
    def translate(self, post_or_comment_id, is_post=False, is_comment=False, p_obj=None, community_id=None):
        """Translates a post or comment, must set post or comment to True.

        :parameter post_or_comment_id: A post or comment ID.
        :parameter [OPTIONAL] is_post: If we passed in a post.
        :parameter [OPTIONAL] is_comment: If we passed in a comment
        :parameter [OPTIONAL] p_obj: The object we are looking to translate
        :parameter [OPTIONAL] community_id: The community id the post/comment was made under.
        :returns: (:class:`str`) Translated message or NoneType
        """
        post_check = False
        comment_check = False
        method_url = None
        if is_post:
            method_url = "posts/"
            if not p_obj:
                p_obj = self.get_post_by_id(post_or_comment_id)
            post_check = True
        elif is_comment:
            method_url = "comments/"
            if not p_obj:
                p_obj = self.get_comment_by_id(post_or_comment_id)
            comment_check = True
        if not community_id:
            if p_obj:
                if comment_check:
                    if p_obj.post:
                        community_id = p_obj.post.artist.community_id
                if post_check:
                    if p_obj.artist:
                        community_id = p_obj.artist.community_id
            else:
                return None
        url = self._api_communities_url + str(community_id) + "/" + method_url + str(
            post_or_comment_id) + "/translate?languageCode=en"
        with self.web_session.get(url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return response_text_as_dict.get('translation')

    @check_expired_token
    def fetch_artist_comments(self, community_id, post_id):
        """Fetches the artist comments on a post.

        :parameter community_id: Community ID the post is on.
        :parameter post_id: Post ID to fetch the artist comments of.
        :returns: List[:ref:`Comment`]
        """
        post_comments_url = self._api_communities_url + str(community_id) + '/posts/' + str(post_id) + "/comments/"
        with self.web_session.get(post_comments_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, post_comments_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return create_comment_objects(response_text_as_dict.get('artistComments'))

    @check_expired_token
    def fetch_comment_body(self, community_id, comment_id):
        """Fetches a comment from its ID.

        :parameter community_id: The ID of the community the comment belongs to.
        :parameter comment_id: The ID of the comment to fetch.
        :returns: (:class:`str`) Body of the comment.
        """
        comment_url = f"{self._api_communities_url}{str(community_id)}/comments/{comment_id}/"
        with self.web_session.get(comment_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, comment_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return response_text_as_dict.get('body')

    @check_expired_token
    def fetch_media(self, community_id, media_id):
        """Receive media object based on media id.

        :parameter community_id: The ID of the community the media belongs to.
        :parameter media_id: The ID of the media to fetch.
        :returns: :ref:`Media` or NoneType
        """
        media_url = self._api_communities_url + str(community_id) + "/medias/" + str(media_id)
        with self.web_session.get(media_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, media_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return create_media_object(response_text_as_dict.get('media'))

    @check_expired_token
    def fetch_announcement(self, community_id: int, announcement_id: int) -> Optional[Announcement]:
        """Receive announcement object based on announcement id.

        :parameter community_id: The ID of the community the media belongs to.
        :parameter announcement_id: The ID of the announcement to fetch.
        :returns: :ref:`Announcement` or NoneType
        """
        announcement_url = self._api_communities_url + str(community_id) + "/notices/" + str(announcement_id)
        with self.web_session.get(announcement_url, headers=self._headers) as resp:
            if self.check_status(resp.status_code, announcement_url):
                response_text = resp.text
                response_text_as_dict = json.loads(response_text)
                return create_announcement_object(response_text_as_dict)

    def update_cache_from_notification(self) -> List[Notification]:
        """Grab a new post based from new notifications and add it to cache.

        Will also return the new notifications found.

        :returns: List[:class:`models.Notification`]
        """
        new_notifications = []
        try:
            notifications = self.get_user_notifications()
            if not notifications:
                return new_notifications

            new_notifications = self.get_new_notifications()
            for notification in new_notifications:
                self.__manage_notification_posts(notification)

        except Exception as e:
            if self.verbose:
                print(f"Failed to update Weverse Cache - {e}")
        return new_notifications

    def __manage_notification_posts(self, notification: Notification):
        """
        Manages the creation of Notification posts and comments.

        :param notification: Notification to create comments and posts for.
        """
        notification_type = self.determine_notification_type(notification.message)
        community = self.get_community_by_id(notification.community_id)
        if notification_type == 'comment':
            artist_comments = self.fetch_artist_comments(notification.community_id, notification.contents_id)
            comment = artist_comments[0]
            comment.post = self.get_post_by_id(comment.post_id)
            if comment.post:
                if comment.post.artist_comments:
                    comment.post.artist_comments.insert(0, comment)
                else:
                    comment.post.artist_comments = [comment]
            self.all_comments[comment.id] = comment

        elif notification_type in ["tofans", "post"]:
            post = self.create_post(community, notification.contents_id)
            if post:
                self.all_posts[post.id] = post
        elif notification_type == 'media':
            media = self.fetch_media(community.id, notification.contents_id)
            if media:
                self.all_media[media.id] = media
        elif notification_type == 'announcement':
            announcement = self.fetch_announcement(community.id, notification.contents_id)
            if announcement:
                self.all_announcements[announcement.id] = announcement

    def check_token_works(self):
        """
        Check if a token is invalid.

        :returns: (:class:`bool`) True if the token works.
        """
        with self.web_session.get(url=self._user_endpoint, headers=self._headers) as resp:
            self._expired_token = not resp.status_code == 200
            return not self._expired_token
