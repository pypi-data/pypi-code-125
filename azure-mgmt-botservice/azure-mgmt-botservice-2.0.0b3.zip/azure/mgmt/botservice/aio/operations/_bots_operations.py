# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._bots_operations import build_create_request, build_delete_request, build_get_check_name_availability_request, build_get_request, build_list_by_resource_group_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BotsOperations:
    """BotsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.botservice.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        resource_name: str,
        parameters: "_models.Bot",
        **kwargs: Any
    ) -> "_models.Bot":
        """Creates a Bot Service. Bot Service is a resource group wide resource type.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param parameters: The parameters to provide for the created bot.
        :type parameters: ~azure.mgmt.botservice.models.Bot
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Bot, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.Bot
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Bot"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'Bot')

        request = build_create_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Bot', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Bot', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["_models.Sku"] = None,
        kind: Optional[Union[str, "_models.Kind"]] = None,
        etag: Optional[str] = None,
        properties: Optional["_models.BotProperties"] = None,
        **kwargs: Any
    ) -> "_models.Bot":
        """Updates a Bot Service.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :param location: Specifies the location of the resource.
        :type location: str
        :param tags: Contains resource tags defined as key/value pairs.
        :type tags: dict[str, str]
        :param sku: Gets or sets the SKU of the resource.
        :type sku: ~azure.mgmt.botservice.models.Sku
        :param kind: Required. Gets or sets the Kind of the resource.
        :type kind: str or ~azure.mgmt.botservice.models.Kind
        :param etag: Entity Tag.
        :type etag: str
        :param properties: The set of properties specific to bot resource.
        :type properties: ~azure.mgmt.botservice.models.BotProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Bot, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.Bot
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Bot"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _parameters = _models.Bot(location=location, tags=tags, sku=sku, kind=kind, etag=etag, properties=properties)
        _json = self._serialize.body(_parameters, 'Bot')

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Bot', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Bot', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a Bot Service from the resource group.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> "_models.Bot":
        """Returns a BotService specified by the parameters.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :param resource_name: The name of the Bot resource.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Bot, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.Bot
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Bot"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Bot', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}'}  # type: ignore


    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.BotResponseList"]:
        """Returns all the resources of a particular type belonging to a resource group.

        :param resource_group_name: The name of the Bot resource group in the user subscription.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BotResponseList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.botservice.models.BotResponseList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BotResponseList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("BotResponseList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices'}  # type: ignore

    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.BotResponseList"]:
        """Returns all the resources of a particular type belonging to a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BotResponseList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.botservice.models.BotResponseList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BotResponseList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("BotResponseList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.BotService/botServices'}  # type: ignore

    @distributed_trace_async
    async def get_check_name_availability(
        self,
        parameters: "_models.CheckNameAvailabilityRequestBody",
        **kwargs: Any
    ) -> "_models.CheckNameAvailabilityResponseBody":
        """Check whether a bot name is available.

        :param parameters: The request body parameters to provide for the check name availability
         request.
        :type parameters: ~azure.mgmt.botservice.models.CheckNameAvailabilityRequestBody
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResponseBody, or the result of cls(response)
        :rtype: ~azure.mgmt.botservice.models.CheckNameAvailabilityResponseBody
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CheckNameAvailabilityResponseBody"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'CheckNameAvailabilityRequestBody')

        request = build_get_check_name_availability_request(
            content_type=content_type,
            json=_json,
            template_url=self.get_check_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckNameAvailabilityResponseBody', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_check_name_availability.metadata = {'url': '/providers/Microsoft.BotService/checkNameAvailability'}  # type: ignore

