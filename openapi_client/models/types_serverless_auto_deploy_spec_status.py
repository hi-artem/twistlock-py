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


class TypesServerlessAutoDeploySpecStatus(object):
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
        'defended': 'int',
        'discovered': 'int',
        'name': 'str'
    }

    attribute_map = {
        'defended': 'defended',
        'discovered': 'discovered',
        'name': 'name'
    }

    def __init__(self, defended=None, discovered=None, name=None, local_vars_configuration=None):  # noqa: E501
        """TypesServerlessAutoDeploySpecStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._defended = None
        self._discovered = None
        self._name = None
        self.discriminator = None

        if defended is not None:
            self.defended = defended
        if discovered is not None:
            self.discovered = discovered
        if name is not None:
            self.name = name

    @property
    def defended(self):
        """Gets the defended of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501

        Defended is the number of already defended functions.   # noqa: E501

        :return: The defended of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._defended

    @defended.setter
    def defended(self, defended):
        """Sets the defended of this TypesServerlessAutoDeploySpecStatus.

        Defended is the number of already defended functions.   # noqa: E501

        :param defended: The defended of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :type defended: int
        """

        self._defended = defended

    @property
    def discovered(self):
        """Gets the discovered of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501

        Discovered is the number of functions to protect.   # noqa: E501

        :return: The discovered of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this TypesServerlessAutoDeploySpecStatus.

        Discovered is the number of functions to protect.   # noqa: E501

        :param discovered: The discovered of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :type discovered: int
        """

        self._discovered = discovered

    @property
    def name(self):
        """Gets the name of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501

        Name is the spec name.   # noqa: E501

        :return: The name of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TypesServerlessAutoDeploySpecStatus.

        Name is the spec name.   # noqa: E501

        :param name: The name of this TypesServerlessAutoDeploySpecStatus.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, TypesServerlessAutoDeploySpecStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesServerlessAutoDeploySpecStatus):
            return True

        return self.to_dict() != other.to_dict()