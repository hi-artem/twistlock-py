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


class PrismaIaCScanFailureCriteria(object):
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
        'high': 'int',
        'low': 'int',
        'medium': 'int',
        'operator': 'str'
    }

    attribute_map = {
        'high': 'high',
        'low': 'low',
        'medium': 'medium',
        'operator': 'operator'
    }

    def __init__(self, high=None, low=None, medium=None, operator=None, local_vars_configuration=None):  # noqa: E501
        """PrismaIaCScanFailureCriteria - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._high = None
        self._low = None
        self._medium = None
        self._operator = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if medium is not None:
            self.medium = medium
        if operator is not None:
            self.operator = operator

    @property
    def high(self):
        """Gets the high of this PrismaIaCScanFailureCriteria.  # noqa: E501

        High is the minimal number of high compliance issues that would fail the scan.   # noqa: E501

        :return: The high of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this PrismaIaCScanFailureCriteria.

        High is the minimal number of high compliance issues that would fail the scan.   # noqa: E501

        :param high: The high of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :type high: int
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this PrismaIaCScanFailureCriteria.  # noqa: E501

        Low is the minimal number of low compliance issues that would fail the scan.   # noqa: E501

        :return: The low of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this PrismaIaCScanFailureCriteria.

        Low is the minimal number of low compliance issues that would fail the scan.   # noqa: E501

        :param low: The low of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :type low: int
        """

        self._low = low

    @property
    def medium(self):
        """Gets the medium of this PrismaIaCScanFailureCriteria.  # noqa: E501

        Medium is the minimal number of medium compliance issues that would fail the scan.   # noqa: E501

        :return: The medium of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this PrismaIaCScanFailureCriteria.

        Medium is the minimal number of medium compliance issues that would fail the scan.   # noqa: E501

        :param medium: The medium of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :type medium: int
        """

        self._medium = medium

    @property
    def operator(self):
        """Gets the operator of this PrismaIaCScanFailureCriteria.  # noqa: E501

        Operator is the logical operator (and/or) for defining when the scan should fail given the above numbers.   # noqa: E501

        :return: The operator of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PrismaIaCScanFailureCriteria.

        Operator is the logical operator (and/or) for defining when the scan should fail given the above numbers.   # noqa: E501

        :param operator: The operator of this PrismaIaCScanFailureCriteria.  # noqa: E501
        :type operator: str
        """

        self._operator = operator

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
        if not isinstance(other, PrismaIaCScanFailureCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrismaIaCScanFailureCriteria):
            return True

        return self.to_dict() != other.to_dict()
