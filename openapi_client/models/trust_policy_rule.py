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


class TrustPolicyRule(object):
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
        'allowed_groups': 'list[str]',
        'block_msg': 'str',
        'collections': 'list[CollectionCollection]',
        'denied_groups': 'list[str]',
        'disabled': 'bool',
        'effect': 'VulnEffect',
        'modified': 'datetime',
        'name': 'str',
        'notes': 'str',
        'owner': 'str',
        'previous_name': 'str'
    }

    attribute_map = {
        'allowed_groups': 'allowedGroups',
        'block_msg': 'blockMsg',
        'collections': 'collections',
        'denied_groups': 'deniedGroups',
        'disabled': 'disabled',
        'effect': 'effect',
        'modified': 'modified',
        'name': 'name',
        'notes': 'notes',
        'owner': 'owner',
        'previous_name': 'previousName'
    }

    def __init__(self, allowed_groups=None, block_msg=None, collections=None, denied_groups=None, disabled=None, effect=None, modified=None, name=None, notes=None, owner=None, previous_name=None, local_vars_configuration=None):  # noqa: E501
        """TrustPolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_groups = None
        self._block_msg = None
        self._collections = None
        self._denied_groups = None
        self._disabled = None
        self._effect = None
        self._modified = None
        self._name = None
        self._notes = None
        self._owner = None
        self._previous_name = None
        self.discriminator = None

        if allowed_groups is not None:
            self.allowed_groups = allowed_groups
        if block_msg is not None:
            self.block_msg = block_msg
        if collections is not None:
            self.collections = collections
        if denied_groups is not None:
            self.denied_groups = denied_groups
        if disabled is not None:
            self.disabled = disabled
        if effect is not None:
            self.effect = effect
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

    @property
    def allowed_groups(self):
        """Gets the allowed_groups of this TrustPolicyRule.  # noqa: E501

        AllowedGroups are the ids of the groups that are whitelisted by this rule.   # noqa: E501

        :return: The allowed_groups of this TrustPolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_groups

    @allowed_groups.setter
    def allowed_groups(self, allowed_groups):
        """Sets the allowed_groups of this TrustPolicyRule.

        AllowedGroups are the ids of the groups that are whitelisted by this rule.   # noqa: E501

        :param allowed_groups: The allowed_groups of this TrustPolicyRule.  # noqa: E501
        :type allowed_groups: list[str]
        """

        self._allowed_groups = allowed_groups

    @property
    def block_msg(self):
        """Gets the block_msg of this TrustPolicyRule.  # noqa: E501

        PolicyBlockMsg represent the block message in a Policy  # noqa: E501

        :return: The block_msg of this TrustPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._block_msg

    @block_msg.setter
    def block_msg(self, block_msg):
        """Sets the block_msg of this TrustPolicyRule.

        PolicyBlockMsg represent the block message in a Policy  # noqa: E501

        :param block_msg: The block_msg of this TrustPolicyRule.  # noqa: E501
        :type block_msg: str
        """

        self._block_msg = block_msg

    @property
    def collections(self):
        """Gets the collections of this TrustPolicyRule.  # noqa: E501

        Collections is a list of collections the rule applies to.   # noqa: E501

        :return: The collections of this TrustPolicyRule.  # noqa: E501
        :rtype: list[CollectionCollection]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this TrustPolicyRule.

        Collections is a list of collections the rule applies to.   # noqa: E501

        :param collections: The collections of this TrustPolicyRule.  # noqa: E501
        :type collections: list[CollectionCollection]
        """

        self._collections = collections

    @property
    def denied_groups(self):
        """Gets the denied_groups of this TrustPolicyRule.  # noqa: E501

        DeniedGroups are the ids of the groups that are blacklisted by this rule.   # noqa: E501

        :return: The denied_groups of this TrustPolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._denied_groups

    @denied_groups.setter
    def denied_groups(self, denied_groups):
        """Sets the denied_groups of this TrustPolicyRule.

        DeniedGroups are the ids of the groups that are blacklisted by this rule.   # noqa: E501

        :param denied_groups: The denied_groups of this TrustPolicyRule.  # noqa: E501
        :type denied_groups: list[str]
        """

        self._denied_groups = denied_groups

    @property
    def disabled(self):
        """Gets the disabled of this TrustPolicyRule.  # noqa: E501

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :return: The disabled of this TrustPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this TrustPolicyRule.

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :param disabled: The disabled of this TrustPolicyRule.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def effect(self):
        """Gets the effect of this TrustPolicyRule.  # noqa: E501


        :return: The effect of this TrustPolicyRule.  # noqa: E501
        :rtype: VulnEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this TrustPolicyRule.


        :param effect: The effect of this TrustPolicyRule.  # noqa: E501
        :type effect: VulnEffect
        """

        self._effect = effect

    @property
    def modified(self):
        """Gets the modified of this TrustPolicyRule.  # noqa: E501

        Datetime when the rule was last modified.   # noqa: E501

        :return: The modified of this TrustPolicyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this TrustPolicyRule.

        Datetime when the rule was last modified.   # noqa: E501

        :param modified: The modified of this TrustPolicyRule.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this TrustPolicyRule.  # noqa: E501

        Name of the rule.   # noqa: E501

        :return: The name of this TrustPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrustPolicyRule.

        Name of the rule.   # noqa: E501

        :param name: The name of this TrustPolicyRule.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this TrustPolicyRule.  # noqa: E501

        Free-form text.   # noqa: E501

        :return: The notes of this TrustPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this TrustPolicyRule.

        Free-form text.   # noqa: E501

        :param notes: The notes of this TrustPolicyRule.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def owner(self):
        """Gets the owner of this TrustPolicyRule.  # noqa: E501

        User who created or last modified the rule.   # noqa: E501

        :return: The owner of this TrustPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TrustPolicyRule.

        User who created or last modified the rule.   # noqa: E501

        :param owner: The owner of this TrustPolicyRule.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def previous_name(self):
        """Gets the previous_name of this TrustPolicyRule.  # noqa: E501

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :return: The previous_name of this TrustPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._previous_name

    @previous_name.setter
    def previous_name(self, previous_name):
        """Sets the previous_name of this TrustPolicyRule.

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :param previous_name: The previous_name of this TrustPolicyRule.  # noqa: E501
        :type previous_name: str
        """

        self._previous_name = previous_name

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
        if not isinstance(other, TrustPolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrustPolicyRule):
            return True

        return self.to_dict() != other.to_dict()
