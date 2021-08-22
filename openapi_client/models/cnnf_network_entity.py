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


class CnnfNetworkEntity(object):
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
        'id': 'int',
        'allow_all': 'CnnfAllowAllConnections',
        'collections': 'list[CollectionCollection]',
        'domains': 'list[str]',
        'name': 'str',
        'subnets': 'list[CnnfSubnet]',
        'type': 'CnnfRuleEntityType'
    }

    attribute_map = {
        'id': '_id',
        'allow_all': 'allowAll',
        'collections': 'collections',
        'domains': 'domains',
        'name': 'name',
        'subnets': 'subnets',
        'type': 'type'
    }

    def __init__(self, id=None, allow_all=None, collections=None, domains=None, name=None, subnets=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CnnfNetworkEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._allow_all = None
        self._collections = None
        self._domains = None
        self._name = None
        self._subnets = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if allow_all is not None:
            self.allow_all = allow_all
        if collections is not None:
            self.collections = collections
        if domains is not None:
            self.domains = domains
        if name is not None:
            self.name = name
        if subnets is not None:
            self.subnets = subnets
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this CnnfNetworkEntity.  # noqa: E501

        EntityID represents the ID of each network firewall entity. 20 bits are used. Max legal value: 2^20-1  # noqa: E501

        :return: The id of this CnnfNetworkEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CnnfNetworkEntity.

        EntityID represents the ID of each network firewall entity. 20 bits are used. Max legal value: 2^20-1  # noqa: E501

        :param id: The id of this CnnfNetworkEntity.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def allow_all(self):
        """Gets the allow_all of this CnnfNetworkEntity.  # noqa: E501


        :return: The allow_all of this CnnfNetworkEntity.  # noqa: E501
        :rtype: CnnfAllowAllConnections
        """
        return self._allow_all

    @allow_all.setter
    def allow_all(self, allow_all):
        """Sets the allow_all of this CnnfNetworkEntity.


        :param allow_all: The allow_all of this CnnfNetworkEntity.  # noqa: E501
        :type allow_all: CnnfAllowAllConnections
        """

        self._allow_all = allow_all

    @property
    def collections(self):
        """Gets the collections of this CnnfNetworkEntity.  # noqa: E501

        Collections indicate the collection the entity is part of.   # noqa: E501

        :return: The collections of this CnnfNetworkEntity.  # noqa: E501
        :rtype: list[CollectionCollection]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this CnnfNetworkEntity.

        Collections indicate the collection the entity is part of.   # noqa: E501

        :param collections: The collections of this CnnfNetworkEntity.  # noqa: E501
        :type collections: list[CollectionCollection]
        """

        self._collections = collections

    @property
    def domains(self):
        """Gets the domains of this CnnfNetworkEntity.  # noqa: E501

        Domains is a list of domains.   # noqa: E501

        :return: The domains of this CnnfNetworkEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this CnnfNetworkEntity.

        Domains is a list of domains.   # noqa: E501

        :param domains: The domains of this CnnfNetworkEntity.  # noqa: E501
        :type domains: list[str]
        """

        self._domains = domains

    @property
    def name(self):
        """Gets the name of this CnnfNetworkEntity.  # noqa: E501

        Name is the entity name.   # noqa: E501

        :return: The name of this CnnfNetworkEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CnnfNetworkEntity.

        Name is the entity name.   # noqa: E501

        :param name: The name of this CnnfNetworkEntity.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def subnets(self):
        """Gets the subnets of this CnnfNetworkEntity.  # noqa: E501

        Subnets are the CIDR format network.   # noqa: E501

        :return: The subnets of this CnnfNetworkEntity.  # noqa: E501
        :rtype: list[CnnfSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this CnnfNetworkEntity.

        Subnets are the CIDR format network.   # noqa: E501

        :param subnets: The subnets of this CnnfNetworkEntity.  # noqa: E501
        :type subnets: list[CnnfSubnet]
        """

        self._subnets = subnets

    @property
    def type(self):
        """Gets the type of this CnnfNetworkEntity.  # noqa: E501


        :return: The type of this CnnfNetworkEntity.  # noqa: E501
        :rtype: CnnfRuleEntityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CnnfNetworkEntity.


        :param type: The type of this CnnfNetworkEntity.  # noqa: E501
        :type type: CnnfRuleEntityType
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
        if not isinstance(other, CnnfNetworkEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CnnfNetworkEntity):
            return True

        return self.to_dict() != other.to_dict()