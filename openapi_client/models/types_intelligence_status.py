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


class TypesIntelligenceStatus(object):
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
        'connected': 'bool',
        'err': 'str',
        'last_update': 'datetime'
    }

    attribute_map = {
        'connected': 'connected',
        'err': 'err',
        'last_update': 'lastUpdate'
    }

    def __init__(self, connected=None, err=None, last_update=None, local_vars_configuration=None):  # noqa: E501
        """TypesIntelligenceStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._connected = None
        self._err = None
        self._last_update = None
        self.discriminator = None

        if connected is not None:
            self.connected = connected
        if err is not None:
            self.err = err
        if last_update is not None:
            self.last_update = last_update

    @property
    def connected(self):
        """Gets the connected of this TypesIntelligenceStatus.  # noqa: E501

        .   # noqa: E501

        :return: The connected of this TypesIntelligenceStatus.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this TypesIntelligenceStatus.

        .   # noqa: E501

        :param connected: The connected of this TypesIntelligenceStatus.  # noqa: E501
        :type connected: bool
        """

        self._connected = connected

    @property
    def err(self):
        """Gets the err of this TypesIntelligenceStatus.  # noqa: E501

        .   # noqa: E501

        :return: The err of this TypesIntelligenceStatus.  # noqa: E501
        :rtype: str
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this TypesIntelligenceStatus.

        .   # noqa: E501

        :param err: The err of this TypesIntelligenceStatus.  # noqa: E501
        :type err: str
        """

        self._err = err

    @property
    def last_update(self):
        """Gets the last_update of this TypesIntelligenceStatus.  # noqa: E501

        .   # noqa: E501

        :return: The last_update of this TypesIntelligenceStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this TypesIntelligenceStatus.

        .   # noqa: E501

        :param last_update: The last_update of this TypesIntelligenceStatus.  # noqa: E501
        :type last_update: datetime
        """

        self._last_update = last_update

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
        if not isinstance(other, TypesIntelligenceStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesIntelligenceStatus):
            return True

        return self.to_dict() != other.to_dict()
