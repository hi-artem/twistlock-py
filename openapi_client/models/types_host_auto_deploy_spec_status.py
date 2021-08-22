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


class TypesHostAutoDeploySpecStatus(object):
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
        'defended': 'int',
        'discovered': 'int',
        'error': 'str',
        'errors': 'list[DeploymentCommandError]',
        'failed': 'int',
        'missing_permissions': 'int',
        'name': 'str',
        'unsupported': 'int'
    }

    attribute_map = {
        'defended': 'defended',
        'discovered': 'discovered',
        'error': 'error',
        'errors': 'errors',
        'failed': 'failed',
        'missing_permissions': 'missingPermissions',
        'name': 'name',
        'unsupported': 'unsupported'
    }

    def __init__(self, defended=None, discovered=None, error=None, errors=None, failed=None, missing_permissions=None, name=None, unsupported=None, local_vars_configuration=None):  # noqa: E501
        """TypesHostAutoDeploySpecStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._defended = None
        self._discovered = None
        self._error = None
        self._errors = None
        self._failed = None
        self._missing_permissions = None
        self._name = None
        self._unsupported = None
        self.discriminator = None

        if defended is not None:
            self.defended = defended
        if discovered is not None:
            self.discovered = discovered
        if error is not None:
            self.error = error
        if errors is not None:
            self.errors = errors
        if failed is not None:
            self.failed = failed
        if missing_permissions is not None:
            self.missing_permissions = missing_permissions
        if name is not None:
            self.name = name
        if unsupported is not None:
            self.unsupported = unsupported

    @property
    def defended(self):
        """Gets the defended of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Defended is the number of already defended VMs.   # noqa: E501

        :return: The defended of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._defended

    @defended.setter
    def defended(self, defended):
        """Sets the defended of this TypesHostAutoDeploySpecStatus.

        Defended is the number of already defended VMs.   # noqa: E501

        :param defended: The defended of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type defended: int
        """

        self._defended = defended

    @property
    def discovered(self):
        """Gets the discovered of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Discovered is the number of discovered unprodected VMs.   # noqa: E501

        :return: The discovered of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this TypesHostAutoDeploySpecStatus.

        Discovered is the number of discovered unprodected VMs.   # noqa: E501

        :param discovered: The discovered of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type discovered: int
        """

        self._discovered = discovered

    @property
    def error(self):
        """Gets the error of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Error is an error logged during the the auto-deploy scan (if occurred).   # noqa: E501

        :return: The error of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TypesHostAutoDeploySpecStatus.

        Error is an error logged during the the auto-deploy scan (if occurred).   # noqa: E501

        :param error: The error of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def errors(self):
        """Gets the errors of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Errors are the errors occurred in the command invocations.   # noqa: E501

        :return: The errors of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: list[DeploymentCommandError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this TypesHostAutoDeploySpecStatus.

        Errors are the errors occurred in the command invocations.   # noqa: E501

        :param errors: The errors of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type errors: list[DeploymentCommandError]
        """

        self._errors = errors

    @property
    def failed(self):
        """Gets the failed of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Failed is the number of instances where deployment failed.   # noqa: E501

        :return: The failed of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TypesHostAutoDeploySpecStatus.

        Failed is the number of instances where deployment failed.   # noqa: E501

        :param failed: The failed of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type failed: int
        """

        self._failed = failed

    @property
    def missing_permissions(self):
        """Gets the missing_permissions of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        MissingPermissions is the number of instances in regions that the credential don't have permissions to them.   # noqa: E501

        :return: The missing_permissions of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._missing_permissions

    @missing_permissions.setter
    def missing_permissions(self, missing_permissions):
        """Sets the missing_permissions of this TypesHostAutoDeploySpecStatus.

        MissingPermissions is the number of instances in regions that the credential don't have permissions to them.   # noqa: E501

        :param missing_permissions: The missing_permissions of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type missing_permissions: int
        """

        self._missing_permissions = missing_permissions

    @property
    def name(self):
        """Gets the name of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Name is the spec name.   # noqa: E501

        :return: The name of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TypesHostAutoDeploySpecStatus.

        Name is the spec name.   # noqa: E501

        :param name: The name of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def unsupported(self):
        """Gets the unsupported of this TypesHostAutoDeploySpecStatus.  # noqa: E501

        Unsupported is the number of instances with missing prerequisites.   # noqa: E501

        :return: The unsupported of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :rtype: int
        """
        return self._unsupported

    @unsupported.setter
    def unsupported(self, unsupported):
        """Sets the unsupported of this TypesHostAutoDeploySpecStatus.

        Unsupported is the number of instances with missing prerequisites.   # noqa: E501

        :param unsupported: The unsupported of this TypesHostAutoDeploySpecStatus.  # noqa: E501
        :type unsupported: int
        """

        self._unsupported = unsupported

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
        if not isinstance(other, TypesHostAutoDeploySpecStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesHostAutoDeploySpecStatus):
            return True

        return self.to_dict() != other.to_dict()
