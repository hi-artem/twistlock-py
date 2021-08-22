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


class SharedHostRadarIncomingConnection(object):
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
        'dst_host': 'str',
        'policy_rules': 'list[CnnfRadarPolicyRule]',
        'ports': 'list[CommonPortData]',
        'src_hash': 'int',
        'src_host': 'str'
    }

    attribute_map = {
        'dst_host': 'dstHost',
        'policy_rules': 'policyRules',
        'ports': 'ports',
        'src_hash': 'srcHash',
        'src_host': 'srcHost'
    }

    def __init__(self, dst_host=None, policy_rules=None, ports=None, src_hash=None, src_host=None, local_vars_configuration=None):  # noqa: E501
        """SharedHostRadarIncomingConnection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dst_host = None
        self._policy_rules = None
        self._ports = None
        self._src_hash = None
        self._src_host = None
        self.discriminator = None

        if dst_host is not None:
            self.dst_host = dst_host
        if policy_rules is not None:
            self.policy_rules = policy_rules
        if ports is not None:
            self.ports = ports
        if src_hash is not None:
            self.src_hash = src_hash
        if src_host is not None:
            self.src_host = src_host

    @property
    def dst_host(self):
        """Gets the dst_host of this SharedHostRadarIncomingConnection.  # noqa: E501

        DstHost is the src hostname.   # noqa: E501

        :return: The dst_host of this SharedHostRadarIncomingConnection.  # noqa: E501
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        """Sets the dst_host of this SharedHostRadarIncomingConnection.

        DstHost is the src hostname.   # noqa: E501

        :param dst_host: The dst_host of this SharedHostRadarIncomingConnection.  # noqa: E501
        :type dst_host: str
        """

        self._dst_host = dst_host

    @property
    def policy_rules(self):
        """Gets the policy_rules of this SharedHostRadarIncomingConnection.  # noqa: E501

        PolicyRules are the policy rules that are applicable for source/dest. Used for radar display of connections deduced from policy rules.   # noqa: E501

        :return: The policy_rules of this SharedHostRadarIncomingConnection.  # noqa: E501
        :rtype: list[CnnfRadarPolicyRule]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        """Sets the policy_rules of this SharedHostRadarIncomingConnection.

        PolicyRules are the policy rules that are applicable for source/dest. Used for radar display of connections deduced from policy rules.   # noqa: E501

        :param policy_rules: The policy_rules of this SharedHostRadarIncomingConnection.  # noqa: E501
        :type policy_rules: list[CnnfRadarPolicyRule]
        """

        self._policy_rules = policy_rules

    @property
    def ports(self):
        """Gets the ports of this SharedHostRadarIncomingConnection.  # noqa: E501

        Ports are the destination ports.   # noqa: E501

        :return: The ports of this SharedHostRadarIncomingConnection.  # noqa: E501
        :rtype: list[CommonPortData]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this SharedHostRadarIncomingConnection.

        Ports are the destination ports.   # noqa: E501

        :param ports: The ports of this SharedHostRadarIncomingConnection.  # noqa: E501
        :type ports: list[CommonPortData]
        """

        self._ports = ports

    @property
    def src_hash(self):
        """Gets the src_hash of this SharedHostRadarIncomingConnection.  # noqa: E501

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :return: The src_hash of this SharedHostRadarIncomingConnection.  # noqa: E501
        :rtype: int
        """
        return self._src_hash

    @src_hash.setter
    def src_hash(self, src_hash):
        """Sets the src_hash of this SharedHostRadarIncomingConnection.

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :param src_hash: The src_hash of this SharedHostRadarIncomingConnection.  # noqa: E501
        :type src_hash: int
        """

        self._src_hash = src_hash

    @property
    def src_host(self):
        """Gets the src_host of this SharedHostRadarIncomingConnection.  # noqa: E501

        SrcHost is the src hostname.   # noqa: E501

        :return: The src_host of this SharedHostRadarIncomingConnection.  # noqa: E501
        :rtype: str
        """
        return self._src_host

    @src_host.setter
    def src_host(self, src_host):
        """Sets the src_host of this SharedHostRadarIncomingConnection.

        SrcHost is the src hostname.   # noqa: E501

        :param src_host: The src_host of this SharedHostRadarIncomingConnection.  # noqa: E501
        :type src_host: str
        """

        self._src_host = src_host

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
        if not isinstance(other, SharedHostRadarIncomingConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedHostRadarIncomingConnection):
            return True

        return self.to_dict() != other.to_dict()
