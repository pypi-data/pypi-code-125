# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class UploadChunk(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'file': 'file',
        'sha256': 'str'
    }

    attribute_map = {
        'file': 'file',
        'sha256': 'sha256'
    }

    def __init__(self, file=None, sha256=None, local_vars_configuration=None):  # noqa: E501
        """UploadChunk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self._sha256 = None
        self.discriminator = None

        self.file = file
        self.sha256 = sha256

    @property
    def file(self):
        """Gets the file of this UploadChunk.  # noqa: E501

        A chunk of the uploaded file.  # noqa: E501

        :return: The file of this UploadChunk.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UploadChunk.

        A chunk of the uploaded file.  # noqa: E501

        :param file: The file of this UploadChunk.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def sha256(self):
        """Gets the sha256 of this UploadChunk.  # noqa: E501

        The SHA-256 checksum of the chunk if available.  # noqa: E501

        :return: The sha256 of this UploadChunk.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this UploadChunk.

        The SHA-256 checksum of the chunk if available.  # noqa: E501

        :param sha256: The sha256 of this UploadChunk.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sha256 is not None and len(sha256) < 1):
            raise ValueError("Invalid value for `sha256`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha256 = sha256

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadChunk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadChunk):
            return True

        return self.to_dict() != other.to_dict()
