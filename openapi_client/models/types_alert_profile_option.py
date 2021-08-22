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


class TypesAlertProfileOption(object):
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
        'alert_type': 'ApiAlertType',
        'has_policy': 'bool',
        'name': 'str',
        'rules': 'list[str]',
        'supported_clients': 'list[str]'
    }

    attribute_map = {
        'alert_type': 'alertType',
        'has_policy': 'hasPolicy',
        'name': 'name',
        'rules': 'rules',
        'supported_clients': 'supportedClients'
    }

    def __init__(self, alert_type=None, has_policy=None, name=None, rules=None, supported_clients=None, local_vars_configuration=None):  # noqa: E501
        """TypesAlertProfileOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._alert_type = None
        self._has_policy = None
        self._name = None
        self._rules = None
        self._supported_clients = None
        self.discriminator = None

        if alert_type is not None:
            self.alert_type = alert_type
        if has_policy is not None:
            self.has_policy = has_policy
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules
        if supported_clients is not None:
            self.supported_clients = supported_clients

    @property
    def alert_type(self):
        """Gets the alert_type of this TypesAlertProfileOption.  # noqa: E501


        :return: The alert_type of this TypesAlertProfileOption.  # noqa: E501
        :rtype: ApiAlertType
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this TypesAlertProfileOption.


        :param alert_type: The alert_type of this TypesAlertProfileOption.  # noqa: E501
        :type alert_type: ApiAlertType
        """

        self._alert_type = alert_type

    @property
    def has_policy(self):
        """Gets the has_policy of this TypesAlertProfileOption.  # noqa: E501

        HasPolicy defines whether the alerts are triggered by policy (e.g., this is false for defender alerts).   # noqa: E501

        :return: The has_policy of this TypesAlertProfileOption.  # noqa: E501
        :rtype: bool
        """
        return self._has_policy

    @has_policy.setter
    def has_policy(self, has_policy):
        """Sets the has_policy of this TypesAlertProfileOption.

        HasPolicy defines whether the alerts are triggered by policy (e.g., this is false for defender alerts).   # noqa: E501

        :param has_policy: The has_policy of this TypesAlertProfileOption.  # noqa: E501
        :type has_policy: bool
        """

        self._has_policy = has_policy

    @property
    def name(self):
        """Gets the name of this TypesAlertProfileOption.  # noqa: E501

        Name is the display name for the option.   # noqa: E501

        :return: The name of this TypesAlertProfileOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TypesAlertProfileOption.

        Name is the display name for the option.   # noqa: E501

        :param name: The name of this TypesAlertProfileOption.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this TypesAlertProfileOption.  # noqa: E501

        Rules are the rule names for the policy associated with this alert type (only relevant if HasPolicy is true).   # noqa: E501

        :return: The rules of this TypesAlertProfileOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this TypesAlertProfileOption.

        Rules are the rule names for the policy associated with this alert type (only relevant if HasPolicy is true).   # noqa: E501

        :param rules: The rules of this TypesAlertProfileOption.  # noqa: E501
        :type rules: list[str]
        """

        self._rules = rules

    @property
    def supported_clients(self):
        """Gets the supported_clients of this TypesAlertProfileOption.  # noqa: E501

        SupportedClients are the supported alert clients for this alert (e.g., jira, email).   # noqa: E501

        :return: The supported_clients of this TypesAlertProfileOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_clients

    @supported_clients.setter
    def supported_clients(self, supported_clients):
        """Sets the supported_clients of this TypesAlertProfileOption.

        SupportedClients are the supported alert clients for this alert (e.g., jira, email).   # noqa: E501

        :param supported_clients: The supported_clients of this TypesAlertProfileOption.  # noqa: E501
        :type supported_clients: list[str]
        """

        self._supported_clients = supported_clients

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
        if not isinstance(other, TypesAlertProfileOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesAlertProfileOption):
            return True

        return self.to_dict() != other.to_dict()