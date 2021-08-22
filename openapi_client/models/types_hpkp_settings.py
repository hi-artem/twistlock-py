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


class TypesHPKPSettings(object):
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
        'certs': 'str',
        'enabled': 'bool',
        'fingerprints': 'list[str]'
    }

    attribute_map = {
        'certs': 'certs',
        'enabled': 'enabled',
        'fingerprints': 'fingerprints'
    }

    def __init__(self, certs=None, enabled=None, fingerprints=None, local_vars_configuration=None):  # noqa: E501
        """TypesHPKPSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._certs = None
        self._enabled = None
        self._fingerprints = None
        self.discriminator = None

        if certs is not None:
            self.certs = certs
        if enabled is not None:
            self.enabled = enabled
        if fingerprints is not None:
            self.fingerprints = fingerprints

    @property
    def certs(self):
        """Gets the certs of this TypesHPKPSettings.  # noqa: E501

        Certs are the public certs used for fingerprinting.   # noqa: E501

        :return: The certs of this TypesHPKPSettings.  # noqa: E501
        :rtype: str
        """
        return self._certs

    @certs.setter
    def certs(self, certs):
        """Sets the certs of this TypesHPKPSettings.

        Certs are the public certs used for fingerprinting.   # noqa: E501

        :param certs: The certs of this TypesHPKPSettings.  # noqa: E501
        :type certs: str
        """

        self._certs = certs

    @property
    def enabled(self):
        """Gets the enabled of this TypesHPKPSettings.  # noqa: E501

        .   # noqa: E501

        :return: The enabled of this TypesHPKPSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TypesHPKPSettings.

        .   # noqa: E501

        :param enabled: The enabled of this TypesHPKPSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def fingerprints(self):
        """Gets the fingerprints of this TypesHPKPSettings.  # noqa: E501

        SHA256 fingerprints of the certificates.   # noqa: E501

        :return: The fingerprints of this TypesHPKPSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._fingerprints

    @fingerprints.setter
    def fingerprints(self, fingerprints):
        """Sets the fingerprints of this TypesHPKPSettings.

        SHA256 fingerprints of the certificates.   # noqa: E501

        :param fingerprints: The fingerprints of this TypesHPKPSettings.  # noqa: E501
        :type fingerprints: list[str]
        """

        self._fingerprints = fingerprints

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
        if not isinstance(other, TypesHPKPSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesHPKPSettings):
            return True

        return self.to_dict() != other.to_dict()
