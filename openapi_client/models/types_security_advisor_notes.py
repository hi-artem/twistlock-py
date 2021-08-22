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


class TypesSecurityAdvisorNotes(object):
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
        'changed_since': 'str'
    }

    attribute_map = {
        'changed_since': 'changedSince'
    }

    def __init__(self, changed_since=None, local_vars_configuration=None):  # noqa: E501
        """TypesSecurityAdvisorNotes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._changed_since = None
        self.discriminator = None

        if changed_since is not None:
            self.changed_since = changed_since

    @property
    def changed_since(self):
        """Gets the changed_since of this TypesSecurityAdvisorNotes.  # noqa: E501

        ChangedSince is the last time entries were modified.   # noqa: E501

        :return: The changed_since of this TypesSecurityAdvisorNotes.  # noqa: E501
        :rtype: str
        """
        return self._changed_since

    @changed_since.setter
    def changed_since(self, changed_since):
        """Sets the changed_since of this TypesSecurityAdvisorNotes.

        ChangedSince is the last time entries were modified.   # noqa: E501

        :param changed_since: The changed_since of this TypesSecurityAdvisorNotes.  # noqa: E501
        :type changed_since: str
        """

        self._changed_since = changed_since

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
        if not isinstance(other, TypesSecurityAdvisorNotes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesSecurityAdvisorNotes):
            return True

        return self.to_dict() != other.to_dict()
