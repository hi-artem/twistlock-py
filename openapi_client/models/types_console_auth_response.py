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


class TypesConsoleAuthResponse(object):
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
        'role': 'str',
        'token': 'str'
    }

    attribute_map = {
        'role': 'role',
        'token': 'token'
    }

    def __init__(self, role=None, token=None, local_vars_configuration=None):  # noqa: E501
        """TypesConsoleAuthResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._role = None
        self._token = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if token is not None:
            self.token = token

    @property
    def role(self):
        """Gets the role of this TypesConsoleAuthResponse.  # noqa: E501

        UserRole is the authenticated user role.   # noqa: E501

        :return: The role of this TypesConsoleAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TypesConsoleAuthResponse.

        UserRole is the authenticated user role.   # noqa: E501

        :param role: The role of this TypesConsoleAuthResponse.  # noqa: E501
        :type role: str
        """

        self._role = role

    @property
    def token(self):
        """Gets the token of this TypesConsoleAuthResponse.  # noqa: E501

        Token is the console authentication response token.   # noqa: E501

        :return: The token of this TypesConsoleAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TypesConsoleAuthResponse.

        Token is the console authentication response token.   # noqa: E501

        :param token: The token of this TypesConsoleAuthResponse.  # noqa: E501
        :type token: str
        """

        self._token = token

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
        if not isinstance(other, TypesConsoleAuthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesConsoleAuthResponse):
            return True

        return self.to_dict() != other.to_dict()
