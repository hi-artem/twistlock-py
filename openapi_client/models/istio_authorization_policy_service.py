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


class IstioAuthorizationPolicyService(object):
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
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, name=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """IstioAuthorizationPolicyService - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._namespace = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def name(self):
        """Gets the name of this IstioAuthorizationPolicyService.  # noqa: E501

        Name is the service name.   # noqa: E501

        :return: The name of this IstioAuthorizationPolicyService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IstioAuthorizationPolicyService.

        Name is the service name.   # noqa: E501

        :param name: The name of this IstioAuthorizationPolicyService.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IstioAuthorizationPolicyService.  # noqa: E501

        Namespace is the service namespace.   # noqa: E501

        :return: The namespace of this IstioAuthorizationPolicyService.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IstioAuthorizationPolicyService.

        Namespace is the service namespace.   # noqa: E501

        :param namespace: The namespace of this IstioAuthorizationPolicyService.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

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
        if not isinstance(other, IstioAuthorizationPolicyService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IstioAuthorizationPolicyService):
            return True

        return self.to_dict() != other.to_dict()
