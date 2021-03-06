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


class ServerlessAssociatedVersion(object):
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
        'version': 'str',
        'weight': 'str'
    }

    attribute_map = {
        'version': 'version',
        'weight': 'weight'
    }

    def __init__(self, version=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """ServerlessAssociatedVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._weight = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if weight is not None:
            self.weight = weight

    @property
    def version(self):
        """Gets the version of this ServerlessAssociatedVersion.  # noqa: E501

        Version is the function version.   # noqa: E501

        :return: The version of this ServerlessAssociatedVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServerlessAssociatedVersion.

        Version is the function version.   # noqa: E501

        :param version: The version of this ServerlessAssociatedVersion.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def weight(self):
        """Gets the weight of this ServerlessAssociatedVersion.  # noqa: E501

        Weight is the possibility that the function will be called when triggering the alias.   # noqa: E501

        :return: The weight of this ServerlessAssociatedVersion.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ServerlessAssociatedVersion.

        Weight is the possibility that the function will be called when triggering the alias.   # noqa: E501

        :param weight: The weight of this ServerlessAssociatedVersion.  # noqa: E501
        :type weight: str
        """

        self._weight = weight

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
        if not isinstance(other, ServerlessAssociatedVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerlessAssociatedVersion):
            return True

        return self.to_dict() != other.to_dict()
