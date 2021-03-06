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


class TypesHostAutoDeployStatus(object):
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
        'scanning': 'bool',
        'status': 'list[TypesHostAutoDeploySpecStatus]'
    }

    attribute_map = {
        'scanning': 'scanning',
        'status': 'status'
    }

    def __init__(self, scanning=None, status=None, local_vars_configuration=None):  # noqa: E501
        """TypesHostAutoDeployStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scanning = None
        self._status = None
        self.discriminator = None

        if scanning is not None:
            self.scanning = scanning
        if status is not None:
            self.status = status

    @property
    def scanning(self):
        """Gets the scanning of this TypesHostAutoDeployStatus.  # noqa: E501

        Scanning indicates whether scanning is running.   # noqa: E501

        :return: The scanning of this TypesHostAutoDeployStatus.  # noqa: E501
        :rtype: bool
        """
        return self._scanning

    @scanning.setter
    def scanning(self, scanning):
        """Sets the scanning of this TypesHostAutoDeployStatus.

        Scanning indicates whether scanning is running.   # noqa: E501

        :param scanning: The scanning of this TypesHostAutoDeployStatus.  # noqa: E501
        :type scanning: bool
        """

        self._scanning = scanning

    @property
    def status(self):
        """Gets the status of this TypesHostAutoDeployStatus.  # noqa: E501

        Status contains the deploy status for each spec.   # noqa: E501

        :return: The status of this TypesHostAutoDeployStatus.  # noqa: E501
        :rtype: list[TypesHostAutoDeploySpecStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TypesHostAutoDeployStatus.

        Status contains the deploy status for each spec.   # noqa: E501

        :param status: The status of this TypesHostAutoDeployStatus.  # noqa: E501
        :type status: list[TypesHostAutoDeploySpecStatus]
        """

        self._status = status

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
        if not isinstance(other, TypesHostAutoDeployStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesHostAutoDeployStatus):
            return True

        return self.to_dict() != other.to_dict()
