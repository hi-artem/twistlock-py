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


class SharedAllowedCVE(object):
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
        'cve': 'str',
        'description': 'str',
        'expiration': 'datetime'
    }

    attribute_map = {
        'cve': 'cve',
        'description': 'description',
        'expiration': 'expiration'
    }

    def __init__(self, cve=None, description=None, expiration=None, local_vars_configuration=None):  # noqa: E501
        """SharedAllowedCVE - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cve = None
        self._description = None
        self._expiration = None
        self.discriminator = None

        if cve is not None:
            self.cve = cve
        if description is not None:
            self.description = description
        if expiration is not None:
            self.expiration = expiration

    @property
    def cve(self):
        """Gets the cve of this SharedAllowedCVE.  # noqa: E501

        CVE is the CVE to allow.   # noqa: E501

        :return: The cve of this SharedAllowedCVE.  # noqa: E501
        :rtype: str
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this SharedAllowedCVE.

        CVE is the CVE to allow.   # noqa: E501

        :param cve: The cve of this SharedAllowedCVE.  # noqa: E501
        :type cve: str
        """

        self._cve = cve

    @property
    def description(self):
        """Gets the description of this SharedAllowedCVE.  # noqa: E501

        Description is the description of why this CVE is allowed.   # noqa: E501

        :return: The description of this SharedAllowedCVE.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SharedAllowedCVE.

        Description is the description of why this CVE is allowed.   # noqa: E501

        :param description: The description of this SharedAllowedCVE.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def expiration(self):
        """Gets the expiration of this SharedAllowedCVE.  # noqa: E501

        Expiration is the expiration date for the allowed CVE.   # noqa: E501

        :return: The expiration of this SharedAllowedCVE.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this SharedAllowedCVE.

        Expiration is the expiration date for the allowed CVE.   # noqa: E501

        :param expiration: The expiration of this SharedAllowedCVE.  # noqa: E501
        :type expiration: datetime
        """

        self._expiration = expiration

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
        if not isinstance(other, SharedAllowedCVE):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedAllowedCVE):
            return True

        return self.to_dict() != other.to_dict()
