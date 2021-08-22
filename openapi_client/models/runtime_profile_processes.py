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


class RuntimeProfileProcesses(object):
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
        'behavioral': 'list[RuntimeProfileProcess]',
        'static': 'list[RuntimeProfileProcess]'
    }

    attribute_map = {
        'behavioral': 'behavioral',
        'static': 'static'
    }

    def __init__(self, behavioral=None, static=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeProfileProcesses - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._behavioral = None
        self._static = None
        self.discriminator = None

        if behavioral is not None:
            self.behavioral = behavioral
        if static is not None:
            self.static = static

    @property
    def behavioral(self):
        """Gets the behavioral of this RuntimeProfileProcesses.  # noqa: E501

        Behavioral are process details learned from behavioral analysis.   # noqa: E501

        :return: The behavioral of this RuntimeProfileProcesses.  # noqa: E501
        :rtype: list[RuntimeProfileProcess]
        """
        return self._behavioral

    @behavioral.setter
    def behavioral(self, behavioral):
        """Sets the behavioral of this RuntimeProfileProcesses.

        Behavioral are process details learned from behavioral analysis.   # noqa: E501

        :param behavioral: The behavioral of this RuntimeProfileProcesses.  # noqa: E501
        :type behavioral: list[RuntimeProfileProcess]
        """

        self._behavioral = behavioral

    @property
    def static(self):
        """Gets the static of this RuntimeProfileProcesses.  # noqa: E501

        Static are process details learned from static analysis.   # noqa: E501

        :return: The static of this RuntimeProfileProcesses.  # noqa: E501
        :rtype: list[RuntimeProfileProcess]
        """
        return self._static

    @static.setter
    def static(self, static):
        """Sets the static of this RuntimeProfileProcesses.

        Static are process details learned from static analysis.   # noqa: E501

        :param static: The static of this RuntimeProfileProcesses.  # noqa: E501
        :type static: list[RuntimeProfileProcess]
        """

        self._static = static

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
        if not isinstance(other, RuntimeProfileProcesses):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeProfileProcesses):
            return True

        return self.to_dict() != other.to_dict()