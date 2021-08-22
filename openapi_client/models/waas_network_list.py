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


class WaasNetworkList(object):
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
        'id': 'str',
        'description': 'str',
        'disabled': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'notes': 'str',
        'owner': 'str',
        'previous_name': 'str',
        'subnets': 'list[str]'
    }

    attribute_map = {
        'id': '_id',
        'description': 'description',
        'disabled': 'disabled',
        'modified': 'modified',
        'name': 'name',
        'notes': 'notes',
        'owner': 'owner',
        'previous_name': 'previousName',
        'subnets': 'subnets'
    }

    def __init__(self, id=None, description=None, disabled=None, modified=None, name=None, notes=None, owner=None, previous_name=None, subnets=None, local_vars_configuration=None):  # noqa: E501
        """WaasNetworkList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._description = None
        self._disabled = None
        self._modified = None
        self._name = None
        self._notes = None
        self._owner = None
        self._previous_name = None
        self._subnets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if owner is not None:
            self.owner = owner
        if previous_name is not None:
            self.previous_name = previous_name
        if subnets is not None:
            self.subnets = subnets

    @property
    def id(self):
        """Gets the id of this WaasNetworkList.  # noqa: E501

        Unique ID.   # noqa: E501

        :return: The id of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WaasNetworkList.

        Unique ID.   # noqa: E501

        :param id: The id of this WaasNetworkList.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this WaasNetworkList.  # noqa: E501

        Description of the network list.   # noqa: E501

        :return: The description of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WaasNetworkList.

        Description of the network list.   # noqa: E501

        :param description: The description of this WaasNetworkList.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this WaasNetworkList.  # noqa: E501

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :return: The disabled of this WaasNetworkList.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this WaasNetworkList.

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :param disabled: The disabled of this WaasNetworkList.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def modified(self):
        """Gets the modified of this WaasNetworkList.  # noqa: E501

        Datetime when the rule was last modified.   # noqa: E501

        :return: The modified of this WaasNetworkList.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WaasNetworkList.

        Datetime when the rule was last modified.   # noqa: E501

        :param modified: The modified of this WaasNetworkList.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this WaasNetworkList.  # noqa: E501

        Name of the rule.   # noqa: E501

        :return: The name of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WaasNetworkList.

        Name of the rule.   # noqa: E501

        :param name: The name of this WaasNetworkList.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this WaasNetworkList.  # noqa: E501

        Free-form text.   # noqa: E501

        :return: The notes of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this WaasNetworkList.

        Free-form text.   # noqa: E501

        :param notes: The notes of this WaasNetworkList.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def owner(self):
        """Gets the owner of this WaasNetworkList.  # noqa: E501

        User who created or last modified the rule.   # noqa: E501

        :return: The owner of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this WaasNetworkList.

        User who created or last modified the rule.   # noqa: E501

        :param owner: The owner of this WaasNetworkList.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def previous_name(self):
        """Gets the previous_name of this WaasNetworkList.  # noqa: E501

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :return: The previous_name of this WaasNetworkList.  # noqa: E501
        :rtype: str
        """
        return self._previous_name

    @previous_name.setter
    def previous_name(self, previous_name):
        """Sets the previous_name of this WaasNetworkList.

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :param previous_name: The previous_name of this WaasNetworkList.  # noqa: E501
        :type previous_name: str
        """

        self._previous_name = previous_name

    @property
    def subnets(self):
        """Gets the subnets of this WaasNetworkList.  # noqa: E501

        List of the IPv4 addresses and IP CIDR blocks.   # noqa: E501

        :return: The subnets of this WaasNetworkList.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this WaasNetworkList.

        List of the IPv4 addresses and IP CIDR blocks.   # noqa: E501

        :param subnets: The subnets of this WaasNetworkList.  # noqa: E501
        :type subnets: list[str]
        """

        self._subnets = subnets

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
        if not isinstance(other, WaasNetworkList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaasNetworkList):
            return True

        return self.to_dict() != other.to_dict()