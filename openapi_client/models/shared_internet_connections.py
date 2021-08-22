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


class SharedInternetConnections(object):
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
        'incoming': 'list[SharedConnection]',
        'outgoing': 'list[SharedConnection]'
    }

    attribute_map = {
        'incoming': 'incoming',
        'outgoing': 'outgoing'
    }

    def __init__(self, incoming=None, outgoing=None, local_vars_configuration=None):  # noqa: E501
        """SharedInternetConnections - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._incoming = None
        self._outgoing = None
        self.discriminator = None

        if incoming is not None:
            self.incoming = incoming
        if outgoing is not None:
            self.outgoing = outgoing

    @property
    def incoming(self):
        """Gets the incoming of this SharedInternetConnections.  # noqa: E501

        Incoming is the incoming connections.   # noqa: E501

        :return: The incoming of this SharedInternetConnections.  # noqa: E501
        :rtype: list[SharedConnection]
        """
        return self._incoming

    @incoming.setter
    def incoming(self, incoming):
        """Sets the incoming of this SharedInternetConnections.

        Incoming is the incoming connections.   # noqa: E501

        :param incoming: The incoming of this SharedInternetConnections.  # noqa: E501
        :type incoming: list[SharedConnection]
        """

        self._incoming = incoming

    @property
    def outgoing(self):
        """Gets the outgoing of this SharedInternetConnections.  # noqa: E501

        Outgoing is the outgoing connections.   # noqa: E501

        :return: The outgoing of this SharedInternetConnections.  # noqa: E501
        :rtype: list[SharedConnection]
        """
        return self._outgoing

    @outgoing.setter
    def outgoing(self, outgoing):
        """Sets the outgoing of this SharedInternetConnections.

        Outgoing is the outgoing connections.   # noqa: E501

        :param outgoing: The outgoing of this SharedInternetConnections.  # noqa: E501
        :type outgoing: list[SharedConnection]
        """

        self._outgoing = outgoing

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
        if not isinstance(other, SharedInternetConnections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedInternetConnections):
            return True

        return self.to_dict() != other.to_dict()
