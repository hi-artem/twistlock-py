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


class IstioAuthorizationPolicy(object):
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
        'effect': 'CommonEffect',
        'name': 'str',
        'namespace': 'str',
        'rules': 'list[IstioAuthorizationPolicyRule]',
        'target_services': 'list[IstioAuthorizationPolicyService]'
    }

    attribute_map = {
        'effect': 'effect',
        'name': 'name',
        'namespace': 'namespace',
        'rules': 'rules',
        'target_services': 'targetServices'
    }

    def __init__(self, effect=None, name=None, namespace=None, rules=None, target_services=None, local_vars_configuration=None):  # noqa: E501
        """IstioAuthorizationPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effect = None
        self._name = None
        self._namespace = None
        self._rules = None
        self._target_services = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if rules is not None:
            self.rules = rules
        if target_services is not None:
            self.target_services = target_services

    @property
    def effect(self):
        """Gets the effect of this IstioAuthorizationPolicy.  # noqa: E501


        :return: The effect of this IstioAuthorizationPolicy.  # noqa: E501
        :rtype: CommonEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this IstioAuthorizationPolicy.


        :param effect: The effect of this IstioAuthorizationPolicy.  # noqa: E501
        :type effect: CommonEffect
        """

        self._effect = effect

    @property
    def name(self):
        """Gets the name of this IstioAuthorizationPolicy.  # noqa: E501

        Name is the authorization policy name.   # noqa: E501

        :return: The name of this IstioAuthorizationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IstioAuthorizationPolicy.

        Name is the authorization policy name.   # noqa: E501

        :param name: The name of this IstioAuthorizationPolicy.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IstioAuthorizationPolicy.  # noqa: E501

        Namespace is the namespace of the authorization policy.   # noqa: E501

        :return: The namespace of this IstioAuthorizationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IstioAuthorizationPolicy.

        Namespace is the namespace of the authorization policy.   # noqa: E501

        :param namespace: The namespace of this IstioAuthorizationPolicy.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def rules(self):
        """Gets the rules of this IstioAuthorizationPolicy.  # noqa: E501

        Rules are the access rules this authorization policy defines.   # noqa: E501

        :return: The rules of this IstioAuthorizationPolicy.  # noqa: E501
        :rtype: list[IstioAuthorizationPolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this IstioAuthorizationPolicy.

        Rules are the access rules this authorization policy defines.   # noqa: E501

        :param rules: The rules of this IstioAuthorizationPolicy.  # noqa: E501
        :type rules: list[IstioAuthorizationPolicyRule]
        """

        self._rules = rules

    @property
    def target_services(self):
        """Gets the target_services of this IstioAuthorizationPolicy.  # noqa: E501

        TargetServices is the list of services the authorization policy applies on.   # noqa: E501

        :return: The target_services of this IstioAuthorizationPolicy.  # noqa: E501
        :rtype: list[IstioAuthorizationPolicyService]
        """
        return self._target_services

    @target_services.setter
    def target_services(self, target_services):
        """Sets the target_services of this IstioAuthorizationPolicy.

        TargetServices is the list of services the authorization policy applies on.   # noqa: E501

        :param target_services: The target_services of this IstioAuthorizationPolicy.  # noqa: E501
        :type target_services: list[IstioAuthorizationPolicyService]
        """

        self._target_services = target_services

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
        if not isinstance(other, IstioAuthorizationPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IstioAuthorizationPolicy):
            return True

        return self.to_dict() != other.to_dict()