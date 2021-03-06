# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class WaasMaliciousUploadConfig(object):
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
        'allowed_extensions': 'list[str]',
        'allowed_file_types': 'list[WaasFileType]',
        'effect': 'WaasEffect'
    }

    attribute_map = {
        'allowed_extensions': 'allowedExtensions',
        'allowed_file_types': 'allowedFileTypes',
        'effect': 'effect'
    }

    def __init__(self, allowed_extensions=None, allowed_file_types=None, effect=None, local_vars_configuration=None):  # noqa: E501
        """WaasMaliciousUploadConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_extensions = None
        self._allowed_file_types = None
        self._effect = None
        self.discriminator = None

        if allowed_extensions is not None:
            self.allowed_extensions = allowed_extensions
        if allowed_file_types is not None:
            self.allowed_file_types = allowed_file_types
        if effect is not None:
            self.effect = effect

    @property
    def allowed_extensions(self):
        """Gets the allowed_extensions of this WaasMaliciousUploadConfig.  # noqa: E501

        Allowed file extensions.   # noqa: E501

        :return: The allowed_extensions of this WaasMaliciousUploadConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_extensions

    @allowed_extensions.setter
    def allowed_extensions(self, allowed_extensions):
        """Sets the allowed_extensions of this WaasMaliciousUploadConfig.

        Allowed file extensions.   # noqa: E501

        :param allowed_extensions: The allowed_extensions of this WaasMaliciousUploadConfig.  # noqa: E501
        :type allowed_extensions: list[str]
        """

        self._allowed_extensions = allowed_extensions

    @property
    def allowed_file_types(self):
        """Gets the allowed_file_types of this WaasMaliciousUploadConfig.  # noqa: E501

        Allowed file types.   # noqa: E501

        :return: The allowed_file_types of this WaasMaliciousUploadConfig.  # noqa: E501
        :rtype: list[WaasFileType]
        """
        return self._allowed_file_types

    @allowed_file_types.setter
    def allowed_file_types(self, allowed_file_types):
        """Sets the allowed_file_types of this WaasMaliciousUploadConfig.

        Allowed file types.   # noqa: E501

        :param allowed_file_types: The allowed_file_types of this WaasMaliciousUploadConfig.  # noqa: E501
        :type allowed_file_types: list[WaasFileType]
        """

        self._allowed_file_types = allowed_file_types

    @property
    def effect(self):
        """Gets the effect of this WaasMaliciousUploadConfig.  # noqa: E501


        :return: The effect of this WaasMaliciousUploadConfig.  # noqa: E501
        :rtype: WaasEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this WaasMaliciousUploadConfig.


        :param effect: The effect of this WaasMaliciousUploadConfig.  # noqa: E501
        :type effect: WaasEffect
        """

        self._effect = effect

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WaasMaliciousUploadConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaasMaliciousUploadConfig):
            return True

        return self.to_dict() != other.to_dict()
