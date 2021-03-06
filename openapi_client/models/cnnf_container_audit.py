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


class CnnfContainerAudit(object):
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
        'block': 'bool',
        'count': 'int',
        'dst_container_name': 'str',
        'dst_domain': 'str',
        'dst_image_name': 'str',
        'dst_port': 'int',
        'dst_profile_hash': 'int',
        'dst_profile_id': 'str',
        'dst_subnet': 'str',
        'labels': 'dict(str, str)',
        'msg': 'str',
        'rule_id': 'int',
        'src_container_name': 'str',
        'src_image_name': 'str',
        'src_profile_hash': 'int',
        'src_profile_id': 'str',
        'time': 'datetime',
        'type': 'CnnfNetworkFirewallAttackType'
    }

    attribute_map = {
        'block': 'block',
        'count': 'count',
        'dst_container_name': 'dstContainerName',
        'dst_domain': 'dstDomain',
        'dst_image_name': 'dstImageName',
        'dst_port': 'dstPort',
        'dst_profile_hash': 'dstProfileHash',
        'dst_profile_id': 'dstProfileID',
        'dst_subnet': 'dstSubnet',
        'labels': 'labels',
        'msg': 'msg',
        'rule_id': 'ruleID',
        'src_container_name': 'srcContainerName',
        'src_image_name': 'srcImageName',
        'src_profile_hash': 'srcProfileHash',
        'src_profile_id': 'srcProfileID',
        'time': 'time',
        'type': 'type'
    }

    def __init__(self, block=None, count=None, dst_container_name=None, dst_domain=None, dst_image_name=None, dst_port=None, dst_profile_hash=None, dst_profile_id=None, dst_subnet=None, labels=None, msg=None, rule_id=None, src_container_name=None, src_image_name=None, src_profile_hash=None, src_profile_id=None, time=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CnnfContainerAudit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._block = None
        self._count = None
        self._dst_container_name = None
        self._dst_domain = None
        self._dst_image_name = None
        self._dst_port = None
        self._dst_profile_hash = None
        self._dst_profile_id = None
        self._dst_subnet = None
        self._labels = None
        self._msg = None
        self._rule_id = None
        self._src_container_name = None
        self._src_image_name = None
        self._src_profile_hash = None
        self._src_profile_id = None
        self._time = None
        self._type = None
        self.discriminator = None

        if block is not None:
            self.block = block
        if count is not None:
            self.count = count
        if dst_container_name is not None:
            self.dst_container_name = dst_container_name
        if dst_domain is not None:
            self.dst_domain = dst_domain
        if dst_image_name is not None:
            self.dst_image_name = dst_image_name
        if dst_port is not None:
            self.dst_port = dst_port
        if dst_profile_hash is not None:
            self.dst_profile_hash = dst_profile_hash
        if dst_profile_id is not None:
            self.dst_profile_id = dst_profile_id
        if dst_subnet is not None:
            self.dst_subnet = dst_subnet
        if labels is not None:
            self.labels = labels
        if msg is not None:
            self.msg = msg
        if rule_id is not None:
            self.rule_id = rule_id
        if src_container_name is not None:
            self.src_container_name = src_container_name
        if src_image_name is not None:
            self.src_image_name = src_image_name
        if src_profile_hash is not None:
            self.src_profile_hash = src_profile_hash
        if src_profile_id is not None:
            self.src_profile_id = src_profile_id
        if time is not None:
            self.time = time
        if type is not None:
            self.type = type

    @property
    def block(self):
        """Gets the block of this CnnfContainerAudit.  # noqa: E501

        Block indicates whether the connection was blocked.   # noqa: E501

        :return: The block of this CnnfContainerAudit.  # noqa: E501
        :rtype: bool
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this CnnfContainerAudit.

        Block indicates whether the connection was blocked.   # noqa: E501

        :param block: The block of this CnnfContainerAudit.  # noqa: E501
        :type block: bool
        """

        self._block = block

    @property
    def count(self):
        """Gets the count of this CnnfContainerAudit.  # noqa: E501

        Count is the event occurrences count.   # noqa: E501

        :return: The count of this CnnfContainerAudit.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CnnfContainerAudit.

        Count is the event occurrences count.   # noqa: E501

        :param count: The count of this CnnfContainerAudit.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def dst_container_name(self):
        """Gets the dst_container_name of this CnnfContainerAudit.  # noqa: E501

        DstContainerName is the destination container name.   # noqa: E501

        :return: The dst_container_name of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._dst_container_name

    @dst_container_name.setter
    def dst_container_name(self, dst_container_name):
        """Sets the dst_container_name of this CnnfContainerAudit.

        DstContainerName is the destination container name.   # noqa: E501

        :param dst_container_name: The dst_container_name of this CnnfContainerAudit.  # noqa: E501
        :type dst_container_name: str
        """

        self._dst_container_name = dst_container_name

    @property
    def dst_domain(self):
        """Gets the dst_domain of this CnnfContainerAudit.  # noqa: E501

        DstDomain is the destination domain that was queried.   # noqa: E501

        :return: The dst_domain of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._dst_domain

    @dst_domain.setter
    def dst_domain(self, dst_domain):
        """Sets the dst_domain of this CnnfContainerAudit.

        DstDomain is the destination domain that was queried.   # noqa: E501

        :param dst_domain: The dst_domain of this CnnfContainerAudit.  # noqa: E501
        :type dst_domain: str
        """

        self._dst_domain = dst_domain

    @property
    def dst_image_name(self):
        """Gets the dst_image_name of this CnnfContainerAudit.  # noqa: E501

        DstImage is the destination image name.   # noqa: E501

        :return: The dst_image_name of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._dst_image_name

    @dst_image_name.setter
    def dst_image_name(self, dst_image_name):
        """Sets the dst_image_name of this CnnfContainerAudit.

        DstImage is the destination image name.   # noqa: E501

        :param dst_image_name: The dst_image_name of this CnnfContainerAudit.  # noqa: E501
        :type dst_image_name: str
        """

        self._dst_image_name = dst_image_name

    @property
    def dst_port(self):
        """Gets the dst_port of this CnnfContainerAudit.  # noqa: E501

        DstPort is the connection destination port.   # noqa: E501

        :return: The dst_port of this CnnfContainerAudit.  # noqa: E501
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this CnnfContainerAudit.

        DstPort is the connection destination port.   # noqa: E501

        :param dst_port: The dst_port of this CnnfContainerAudit.  # noqa: E501
        :type dst_port: int
        """

        self._dst_port = dst_port

    @property
    def dst_profile_hash(self):
        """Gets the dst_profile_hash of this CnnfContainerAudit.  # noqa: E501

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :return: The dst_profile_hash of this CnnfContainerAudit.  # noqa: E501
        :rtype: int
        """
        return self._dst_profile_hash

    @dst_profile_hash.setter
    def dst_profile_hash(self, dst_profile_hash):
        """Sets the dst_profile_hash of this CnnfContainerAudit.

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :param dst_profile_hash: The dst_profile_hash of this CnnfContainerAudit.  # noqa: E501
        :type dst_profile_hash: int
        """

        self._dst_profile_hash = dst_profile_hash

    @property
    def dst_profile_id(self):
        """Gets the dst_profile_id of this CnnfContainerAudit.  # noqa: E501

        DstProfileID is the destination profile ID.   # noqa: E501

        :return: The dst_profile_id of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._dst_profile_id

    @dst_profile_id.setter
    def dst_profile_id(self, dst_profile_id):
        """Sets the dst_profile_id of this CnnfContainerAudit.

        DstProfileID is the destination profile ID.   # noqa: E501

        :param dst_profile_id: The dst_profile_id of this CnnfContainerAudit.  # noqa: E501
        :type dst_profile_id: str
        """

        self._dst_profile_id = dst_profile_id

    @property
    def dst_subnet(self):
        """Gets the dst_subnet of this CnnfContainerAudit.  # noqa: E501

        DstSubnet is the destination subnet.   # noqa: E501

        :return: The dst_subnet of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._dst_subnet

    @dst_subnet.setter
    def dst_subnet(self, dst_subnet):
        """Sets the dst_subnet of this CnnfContainerAudit.

        DstSubnet is the destination subnet.   # noqa: E501

        :param dst_subnet: The dst_subnet of this CnnfContainerAudit.  # noqa: E501
        :type dst_subnet: str
        """

        self._dst_subnet = dst_subnet

    @property
    def labels(self):
        """Gets the labels of this CnnfContainerAudit.  # noqa: E501

        Labels are the custom labels associated with the target container.   # noqa: E501

        :return: The labels of this CnnfContainerAudit.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CnnfContainerAudit.

        Labels are the custom labels associated with the target container.   # noqa: E501

        :param labels: The labels of this CnnfContainerAudit.  # noqa: E501
        :type labels: dict(str, str)
        """

        self._labels = labels

    @property
    def msg(self):
        """Gets the msg of this CnnfContainerAudit.  # noqa: E501

        Message is the event message.   # noqa: E501

        :return: The msg of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this CnnfContainerAudit.

        Message is the event message.   # noqa: E501

        :param msg: The msg of this CnnfContainerAudit.  # noqa: E501
        :type msg: str
        """

        self._msg = msg

    @property
    def rule_id(self):
        """Gets the rule_id of this CnnfContainerAudit.  # noqa: E501

        RuleID represents the ID of each container network firewall policy rule  # noqa: E501

        :return: The rule_id of this CnnfContainerAudit.  # noqa: E501
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CnnfContainerAudit.

        RuleID represents the ID of each container network firewall policy rule  # noqa: E501

        :param rule_id: The rule_id of this CnnfContainerAudit.  # noqa: E501
        :type rule_id: int
        """

        self._rule_id = rule_id

    @property
    def src_container_name(self):
        """Gets the src_container_name of this CnnfContainerAudit.  # noqa: E501

        SrcContainerName is the source container name.   # noqa: E501

        :return: The src_container_name of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._src_container_name

    @src_container_name.setter
    def src_container_name(self, src_container_name):
        """Sets the src_container_name of this CnnfContainerAudit.

        SrcContainerName is the source container name.   # noqa: E501

        :param src_container_name: The src_container_name of this CnnfContainerAudit.  # noqa: E501
        :type src_container_name: str
        """

        self._src_container_name = src_container_name

    @property
    def src_image_name(self):
        """Gets the src_image_name of this CnnfContainerAudit.  # noqa: E501

        SrcImage is the source image name.   # noqa: E501

        :return: The src_image_name of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._src_image_name

    @src_image_name.setter
    def src_image_name(self, src_image_name):
        """Sets the src_image_name of this CnnfContainerAudit.

        SrcImage is the source image name.   # noqa: E501

        :param src_image_name: The src_image_name of this CnnfContainerAudit.  # noqa: E501
        :type src_image_name: str
        """

        self._src_image_name = src_image_name

    @property
    def src_profile_hash(self):
        """Gets the src_profile_hash of this CnnfContainerAudit.  # noqa: E501

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :return: The src_profile_hash of this CnnfContainerAudit.  # noqa: E501
        :rtype: int
        """
        return self._src_profile_hash

    @src_profile_hash.setter
    def src_profile_hash(self, src_profile_hash):
        """Sets the src_profile_hash of this CnnfContainerAudit.

        ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types  # noqa: E501

        :param src_profile_hash: The src_profile_hash of this CnnfContainerAudit.  # noqa: E501
        :type src_profile_hash: int
        """

        self._src_profile_hash = src_profile_hash

    @property
    def src_profile_id(self):
        """Gets the src_profile_id of this CnnfContainerAudit.  # noqa: E501

        SrcProfileID is the source profile ID.   # noqa: E501

        :return: The src_profile_id of this CnnfContainerAudit.  # noqa: E501
        :rtype: str
        """
        return self._src_profile_id

    @src_profile_id.setter
    def src_profile_id(self, src_profile_id):
        """Sets the src_profile_id of this CnnfContainerAudit.

        SrcProfileID is the source profile ID.   # noqa: E501

        :param src_profile_id: The src_profile_id of this CnnfContainerAudit.  # noqa: E501
        :type src_profile_id: str
        """

        self._src_profile_id = src_profile_id

    @property
    def time(self):
        """Gets the time of this CnnfContainerAudit.  # noqa: E501

        Time is the UTC time of the audit event.   # noqa: E501

        :return: The time of this CnnfContainerAudit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CnnfContainerAudit.

        Time is the UTC time of the audit event.   # noqa: E501

        :param time: The time of this CnnfContainerAudit.  # noqa: E501
        :type time: datetime
        """

        self._time = time

    @property
    def type(self):
        """Gets the type of this CnnfContainerAudit.  # noqa: E501


        :return: The type of this CnnfContainerAudit.  # noqa: E501
        :rtype: CnnfNetworkFirewallAttackType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CnnfContainerAudit.


        :param type: The type of this CnnfContainerAudit.  # noqa: E501
        :type type: CnnfNetworkFirewallAttackType
        """

        self._type = type

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
        if not isinstance(other, CnnfContainerAudit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CnnfContainerAudit):
            return True

        return self.to_dict() != other.to_dict()
