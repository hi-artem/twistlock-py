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


class RuntimeContainerPolicyRule(object):
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
        'advanced_protection': 'bool',
        'cloud_metadata_enforcement': 'bool',
        'collections': 'list[CollectionCollection]',
        'custom_rules': 'list[CustomrulesRef]',
        'disabled': 'bool',
        'dns': 'RuntimeDNSRule',
        'filesystem': 'RuntimeFilesystemRule',
        'kubernetes_enforcement': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'network': 'RuntimeContainerNetworkRule',
        'notes': 'str',
        'owner': 'str',
        'previous_name': 'str',
        'processes': 'RuntimeProcessesRule',
        'wild_fire_analysis': 'RuntimeRuleEffect'
    }

    attribute_map = {
        'advanced_protection': 'advancedProtection',
        'cloud_metadata_enforcement': 'cloudMetadataEnforcement',
        'collections': 'collections',
        'custom_rules': 'customRules',
        'disabled': 'disabled',
        'dns': 'dns',
        'filesystem': 'filesystem',
        'kubernetes_enforcement': 'kubernetesEnforcement',
        'modified': 'modified',
        'name': 'name',
        'network': 'network',
        'notes': 'notes',
        'owner': 'owner',
        'previous_name': 'previousName',
        'processes': 'processes',
        'wild_fire_analysis': 'wildFireAnalysis'
    }

    def __init__(self, advanced_protection=None, cloud_metadata_enforcement=None, collections=None, custom_rules=None, disabled=None, dns=None, filesystem=None, kubernetes_enforcement=None, modified=None, name=None, network=None, notes=None, owner=None, previous_name=None, processes=None, wild_fire_analysis=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeContainerPolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._advanced_protection = None
        self._cloud_metadata_enforcement = None
        self._collections = None
        self._custom_rules = None
        self._disabled = None
        self._dns = None
        self._filesystem = None
        self._kubernetes_enforcement = None
        self._modified = None
        self._name = None
        self._network = None
        self._notes = None
        self._owner = None
        self._previous_name = None
        self._processes = None
        self._wild_fire_analysis = None
        self.discriminator = None

        if advanced_protection is not None:
            self.advanced_protection = advanced_protection
        if cloud_metadata_enforcement is not None:
            self.cloud_metadata_enforcement = cloud_metadata_enforcement
        if collections is not None:
            self.collections = collections
        if custom_rules is not None:
            self.custom_rules = custom_rules
        if disabled is not None:
            self.disabled = disabled
        if dns is not None:
            self.dns = dns
        if filesystem is not None:
            self.filesystem = filesystem
        if kubernetes_enforcement is not None:
            self.kubernetes_enforcement = kubernetes_enforcement
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if network is not None:
            self.network = network
        if notes is not None:
            self.notes = notes
        if owner is not None:
            self.owner = owner
        if previous_name is not None:
            self.previous_name = previous_name
        if processes is not None:
            self.processes = processes
        if wild_fire_analysis is not None:
            self.wild_fire_analysis = wild_fire_analysis

    @property
    def advanced_protection(self):
        """Gets the advanced_protection of this RuntimeContainerPolicyRule.  # noqa: E501

        Indicates whether advanced protection (e.g., custom or premium feeds for container, added whitelist rules for serverless) is enabled (true) or not (false).   # noqa: E501

        :return: The advanced_protection of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._advanced_protection

    @advanced_protection.setter
    def advanced_protection(self, advanced_protection):
        """Sets the advanced_protection of this RuntimeContainerPolicyRule.

        Indicates whether advanced protection (e.g., custom or premium feeds for container, added whitelist rules for serverless) is enabled (true) or not (false).   # noqa: E501

        :param advanced_protection: The advanced_protection of this RuntimeContainerPolicyRule.  # noqa: E501
        :type advanced_protection: bool
        """

        self._advanced_protection = advanced_protection

    @property
    def cloud_metadata_enforcement(self):
        """Gets the cloud_metadata_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501

        Catches containers that access the cloud provider metadata API.   # noqa: E501

        :return: The cloud_metadata_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_metadata_enforcement

    @cloud_metadata_enforcement.setter
    def cloud_metadata_enforcement(self, cloud_metadata_enforcement):
        """Sets the cloud_metadata_enforcement of this RuntimeContainerPolicyRule.

        Catches containers that access the cloud provider metadata API.   # noqa: E501

        :param cloud_metadata_enforcement: The cloud_metadata_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501
        :type cloud_metadata_enforcement: bool
        """

        self._cloud_metadata_enforcement = cloud_metadata_enforcement

    @property
    def collections(self):
        """Gets the collections of this RuntimeContainerPolicyRule.  # noqa: E501

        List of collections. Used to scope the rule.   # noqa: E501

        :return: The collections of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: list[CollectionCollection]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this RuntimeContainerPolicyRule.

        List of collections. Used to scope the rule.   # noqa: E501

        :param collections: The collections of this RuntimeContainerPolicyRule.  # noqa: E501
        :type collections: list[CollectionCollection]
        """

        self._collections = collections

    @property
    def custom_rules(self):
        """Gets the custom_rules of this RuntimeContainerPolicyRule.  # noqa: E501

        List of custom runtime rules.   # noqa: E501

        :return: The custom_rules of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: list[CustomrulesRef]
        """
        return self._custom_rules

    @custom_rules.setter
    def custom_rules(self, custom_rules):
        """Sets the custom_rules of this RuntimeContainerPolicyRule.

        List of custom runtime rules.   # noqa: E501

        :param custom_rules: The custom_rules of this RuntimeContainerPolicyRule.  # noqa: E501
        :type custom_rules: list[CustomrulesRef]
        """

        self._custom_rules = custom_rules

    @property
    def disabled(self):
        """Gets the disabled of this RuntimeContainerPolicyRule.  # noqa: E501

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :return: The disabled of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this RuntimeContainerPolicyRule.

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :param disabled: The disabled of this RuntimeContainerPolicyRule.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def dns(self):
        """Gets the dns of this RuntimeContainerPolicyRule.  # noqa: E501


        :return: The dns of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: RuntimeDNSRule
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this RuntimeContainerPolicyRule.


        :param dns: The dns of this RuntimeContainerPolicyRule.  # noqa: E501
        :type dns: RuntimeDNSRule
        """

        self._dns = dns

    @property
    def filesystem(self):
        """Gets the filesystem of this RuntimeContainerPolicyRule.  # noqa: E501


        :return: The filesystem of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: RuntimeFilesystemRule
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this RuntimeContainerPolicyRule.


        :param filesystem: The filesystem of this RuntimeContainerPolicyRule.  # noqa: E501
        :type filesystem: RuntimeFilesystemRule
        """

        self._filesystem = filesystem

    @property
    def kubernetes_enforcement(self):
        """Gets the kubernetes_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501

        Detects containers that attempt to compromise the orchestrator.   # noqa: E501

        :return: The kubernetes_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._kubernetes_enforcement

    @kubernetes_enforcement.setter
    def kubernetes_enforcement(self, kubernetes_enforcement):
        """Sets the kubernetes_enforcement of this RuntimeContainerPolicyRule.

        Detects containers that attempt to compromise the orchestrator.   # noqa: E501

        :param kubernetes_enforcement: The kubernetes_enforcement of this RuntimeContainerPolicyRule.  # noqa: E501
        :type kubernetes_enforcement: bool
        """

        self._kubernetes_enforcement = kubernetes_enforcement

    @property
    def modified(self):
        """Gets the modified of this RuntimeContainerPolicyRule.  # noqa: E501

        Datetime when the rule was last modified.   # noqa: E501

        :return: The modified of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this RuntimeContainerPolicyRule.

        Datetime when the rule was last modified.   # noqa: E501

        :param modified: The modified of this RuntimeContainerPolicyRule.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this RuntimeContainerPolicyRule.  # noqa: E501

        Name of the rule.   # noqa: E501

        :return: The name of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuntimeContainerPolicyRule.

        Name of the rule.   # noqa: E501

        :param name: The name of this RuntimeContainerPolicyRule.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def network(self):
        """Gets the network of this RuntimeContainerPolicyRule.  # noqa: E501


        :return: The network of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: RuntimeContainerNetworkRule
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this RuntimeContainerPolicyRule.


        :param network: The network of this RuntimeContainerPolicyRule.  # noqa: E501
        :type network: RuntimeContainerNetworkRule
        """

        self._network = network

    @property
    def notes(self):
        """Gets the notes of this RuntimeContainerPolicyRule.  # noqa: E501

        Free-form text.   # noqa: E501

        :return: The notes of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this RuntimeContainerPolicyRule.

        Free-form text.   # noqa: E501

        :param notes: The notes of this RuntimeContainerPolicyRule.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def owner(self):
        """Gets the owner of this RuntimeContainerPolicyRule.  # noqa: E501

        User who created or last modified the rule.   # noqa: E501

        :return: The owner of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RuntimeContainerPolicyRule.

        User who created or last modified the rule.   # noqa: E501

        :param owner: The owner of this RuntimeContainerPolicyRule.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def previous_name(self):
        """Gets the previous_name of this RuntimeContainerPolicyRule.  # noqa: E501

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :return: The previous_name of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._previous_name

    @previous_name.setter
    def previous_name(self, previous_name):
        """Sets the previous_name of this RuntimeContainerPolicyRule.

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :param previous_name: The previous_name of this RuntimeContainerPolicyRule.  # noqa: E501
        :type previous_name: str
        """

        self._previous_name = previous_name

    @property
    def processes(self):
        """Gets the processes of this RuntimeContainerPolicyRule.  # noqa: E501


        :return: The processes of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: RuntimeProcessesRule
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this RuntimeContainerPolicyRule.


        :param processes: The processes of this RuntimeContainerPolicyRule.  # noqa: E501
        :type processes: RuntimeProcessesRule
        """

        self._processes = processes

    @property
    def wild_fire_analysis(self):
        """Gets the wild_fire_analysis of this RuntimeContainerPolicyRule.  # noqa: E501


        :return: The wild_fire_analysis of this RuntimeContainerPolicyRule.  # noqa: E501
        :rtype: RuntimeRuleEffect
        """
        return self._wild_fire_analysis

    @wild_fire_analysis.setter
    def wild_fire_analysis(self, wild_fire_analysis):
        """Sets the wild_fire_analysis of this RuntimeContainerPolicyRule.


        :param wild_fire_analysis: The wild_fire_analysis of this RuntimeContainerPolicyRule.  # noqa: E501
        :type wild_fire_analysis: RuntimeRuleEffect
        """

        self._wild_fire_analysis = wild_fire_analysis

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
        if not isinstance(other, RuntimeContainerPolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeContainerPolicyRule):
            return True

        return self.to_dict() != other.to_dict()
