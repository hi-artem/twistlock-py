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


class TypesServerlessAutoDeployStatus(object):
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
        'errors': 'list[str]',
        'scanning': 'bool',
        'specs': 'list[TypesServerlessAutoDeploySpecStatus]'
    }

    attribute_map = {
        'errors': 'errors',
        'scanning': 'scanning',
        'specs': 'specs'
    }

    def __init__(self, errors=None, scanning=None, specs=None, local_vars_configuration=None):  # noqa: E501
        """TypesServerlessAutoDeployStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._scanning = None
        self._specs = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if scanning is not None:
            self.scanning = scanning
        if specs is not None:
            self.specs = specs

    @property
    def errors(self):
        """Gets the errors of this TypesServerlessAutoDeployStatus.  # noqa: E501

        Errors is the collection of errors for the auto-deploy scan.   # noqa: E501

        :return: The errors of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this TypesServerlessAutoDeployStatus.

        Errors is the collection of errors for the auto-deploy scan.   # noqa: E501

        :param errors: The errors of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :type errors: list[str]
        """

        self._errors = errors

    @property
    def scanning(self):
        """Gets the scanning of this TypesServerlessAutoDeployStatus.  # noqa: E501

        Scanning indicates whether scanning is running.   # noqa: E501

        :return: The scanning of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        """Sets the scanning of this TypesServerlessAutoDeployStatus.

        Scanning indicates whether scanning is running.   # noqa: E501

        :param scanning: The scanning of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :type scanning: bool
        """

        self._scanning = scanning

    @property
    def specs(self):
        """Gets the specs of this TypesServerlessAutoDeployStatus.  # noqa: E501

        Specs contains the status for each spec.   # noqa: E501

        :return: The specs of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :rtype: list[TypesServerlessAutoDeploySpecStatus]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this TypesServerlessAutoDeployStatus.

        Specs contains the status for each spec.   # noqa: E501

        :param specs: The specs of this TypesServerlessAutoDeployStatus.  # noqa: E501
        :type specs: list[TypesServerlessAutoDeploySpecStatus]
        """

        self._specs = specs

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
        if not isinstance(other, TypesServerlessAutoDeployStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesServerlessAutoDeployStatus):
            return True

        return self.to_dict() != other.to_dict()
