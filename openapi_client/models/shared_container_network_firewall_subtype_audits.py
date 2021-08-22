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


class SharedContainerNetworkFirewallSubtypeAudits(object):
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
        'audits': 'list[CnnfContainerAudit]',
        'count': 'int'
    }

    attribute_map = {
        'audits': 'audits',
        'count': 'count'
    }

    def __init__(self, audits=None, count=None, local_vars_configuration=None):  # noqa: E501
        """SharedContainerNetworkFirewallSubtypeAudits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._audits = None
        self._count = None
        self.discriminator = None

        if audits is not None:
            self.audits = audits
        if count is not None:
            self.count = count

    @property
    def audits(self):
        """Gets the audits of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501

        Audits are the container network firewall audits associated with the sub-type, limited to the determined capacity.   # noqa: E501

        :return: The audits of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501
        :rtype: list[CnnfContainerAudit]
        """
        return self._audits

    @audits.setter
    def audits(self, audits):
        """Sets the audits of this SharedContainerNetworkFirewallSubtypeAudits.

        Audits are the container network firewall audits associated with the sub-type, limited to the determined capacity.   # noqa: E501

        :param audits: The audits of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501
        :type audits: list[CnnfContainerAudit]
        """

        self._audits = audits

    @property
    def count(self):
        """Gets the count of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501

        Count is the total count of the sub-type audits.   # noqa: E501

        :return: The count of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SharedContainerNetworkFirewallSubtypeAudits.

        Count is the total count of the sub-type audits.   # noqa: E501

        :param count: The count of this SharedContainerNetworkFirewallSubtypeAudits.  # noqa: E501
        :type count: int
        """

        self._count = count

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
        if not isinstance(other, SharedContainerNetworkFirewallSubtypeAudits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedContainerNetworkFirewallSubtypeAudits):
            return True

        return self.to_dict() != other.to_dict()
