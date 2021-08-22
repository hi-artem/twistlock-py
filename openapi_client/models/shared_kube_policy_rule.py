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


class SharedKubePolicyRule(object):
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
        'api_groups': 'list[str]',
        'non_resource_urls': 'list[str]',
        'resource_names': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'non_resource_urls': 'nonResourceURLs',
        'resource_names': 'resourceNames',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, non_resource_urls=None, resource_names=None, resources=None, verbs=None, local_vars_configuration=None):  # noqa: E501
        """SharedKubePolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api_groups = None
        self._non_resource_urls = None
        self._resource_names = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        if api_groups is not None:
            self.api_groups = api_groups
        if non_resource_urls is not None:
            self.non_resource_urls = non_resource_urls
        if resource_names is not None:
            self.resource_names = resource_names
        if resources is not None:
            self.resources = resources
        if verbs is not None:
            self.verbs = verbs

    @property
    def api_groups(self):
        """Gets the api_groups of this SharedKubePolicyRule.  # noqa: E501

        .   # noqa: E501

        :return: The api_groups of this SharedKubePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """Sets the api_groups of this SharedKubePolicyRule.

        .   # noqa: E501

        :param api_groups: The api_groups of this SharedKubePolicyRule.  # noqa: E501
        :type api_groups: list[str]
        """

        self._api_groups = api_groups

    @property
    def non_resource_urls(self):
        """Gets the non_resource_urls of this SharedKubePolicyRule.  # noqa: E501

        .   # noqa: E501

        :return: The non_resource_urls of this SharedKubePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._non_resource_urls

    @non_resource_urls.setter
    def non_resource_urls(self, non_resource_urls):
        """Sets the non_resource_urls of this SharedKubePolicyRule.

        .   # noqa: E501

        :param non_resource_urls: The non_resource_urls of this SharedKubePolicyRule.  # noqa: E501
        :type non_resource_urls: list[str]
        """

        self._non_resource_urls = non_resource_urls

    @property
    def resource_names(self):
        """Gets the resource_names of this SharedKubePolicyRule.  # noqa: E501

        .   # noqa: E501

        :return: The resource_names of this SharedKubePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """Sets the resource_names of this SharedKubePolicyRule.

        .   # noqa: E501

        :param resource_names: The resource_names of this SharedKubePolicyRule.  # noqa: E501
        :type resource_names: list[str]
        """

        self._resource_names = resource_names

    @property
    def resources(self):
        """Gets the resources of this SharedKubePolicyRule.  # noqa: E501

        .   # noqa: E501

        :return: The resources of this SharedKubePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this SharedKubePolicyRule.

        .   # noqa: E501

        :param resources: The resources of this SharedKubePolicyRule.  # noqa: E501
        :type resources: list[str]
        """

        self._resources = resources

    @property
    def verbs(self):
        """Gets the verbs of this SharedKubePolicyRule.  # noqa: E501

        .   # noqa: E501

        :return: The verbs of this SharedKubePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this SharedKubePolicyRule.

        .   # noqa: E501

        :param verbs: The verbs of this SharedKubePolicyRule.  # noqa: E501
        :type verbs: list[str]
        """

        self._verbs = verbs

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
        if not isinstance(other, SharedKubePolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedKubePolicyRule):
            return True

        return self.to_dict() != other.to_dict()