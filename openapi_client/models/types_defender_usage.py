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


class TypesDefenderUsage(object):
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
        'credit_count': 'float',
        'defenders_count': 'float'
    }

    attribute_map = {
        'credit_count': 'creditCount',
        'defenders_count': 'defendersCount'
    }

    def __init__(self, credit_count=None, defenders_count=None, local_vars_configuration=None):  # noqa: E501
        """TypesDefenderUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._credit_count = None
        self._defenders_count = None
        self.discriminator = None

        if credit_count is not None:
            self.credit_count = credit_count
        if defenders_count is not None:
            self.defenders_count = defenders_count

    @property
    def credit_count(self):
        """Gets the credit_count of this TypesDefenderUsage.  # noqa: E501

        CreditCount is credits that was used for this defender type.   # noqa: E501

        :return: The credit_count of this TypesDefenderUsage.  # noqa: E501
        :rtype: float
        """
        return self._credit_count

    @credit_count.setter
    def credit_count(self, credit_count):
        """Sets the credit_count of this TypesDefenderUsage.

        CreditCount is credits that was used for this defender type.   # noqa: E501

        :param credit_count: The credit_count of this TypesDefenderUsage.  # noqa: E501
        :type credit_count: float
        """

        self._credit_count = credit_count

    @property
    def defenders_count(self):
        """Gets the defenders_count of this TypesDefenderUsage.  # noqa: E501

        DefendersCount is the number of defenders that was used for this defender type.   # noqa: E501

        :return: The defenders_count of this TypesDefenderUsage.  # noqa: E501
        :rtype: float
        """
        return self._defenders_count

    @defenders_count.setter
    def defenders_count(self, defenders_count):
        """Sets the defenders_count of this TypesDefenderUsage.

        DefendersCount is the number of defenders that was used for this defender type.   # noqa: E501

        :param defenders_count: The defenders_count of this TypesDefenderUsage.  # noqa: E501
        :type defenders_count: float
        """

        self._defenders_count = defenders_count

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
        if not isinstance(other, TypesDefenderUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesDefenderUsage):
            return True

        return self.to_dict() != other.to_dict()