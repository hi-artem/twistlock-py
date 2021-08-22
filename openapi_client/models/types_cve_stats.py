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


class TypesCVEStats(object):
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
        'count': 'int',
        'distro': 'str',
        'distro_release': 'str',
        'modified': 'int',
        'type': 'str'
    }

    attribute_map = {
        'count': 'count',
        'distro': 'distro',
        'distro_release': 'distro_release',
        'modified': 'modified',
        'type': 'type'
    }

    def __init__(self, count=None, distro=None, distro_release=None, modified=None, type=None, local_vars_configuration=None):  # noqa: E501
        """TypesCVEStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._distro = None
        self._distro_release = None
        self._modified = None
        self._type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if distro is not None:
            self.distro = distro
        if distro_release is not None:
            self.distro_release = distro_release
        if modified is not None:
            self.modified = modified
        if type is not None:
            self.type = type

    @property
    def count(self):
        """Gets the count of this TypesCVEStats.  # noqa: E501

        Count is the number of CVEs from the specific type.   # noqa: E501

        :return: The count of this TypesCVEStats.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TypesCVEStats.

        Count is the number of CVEs from the specific type.   # noqa: E501

        :param count: The count of this TypesCVEStats.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def distro(self):
        """Gets the distro of this TypesCVEStats.  # noqa: E501

        Distro is the impacted image distro (e.g., ubuntu).   # noqa: E501

        :return: The distro of this TypesCVEStats.  # noqa: E501
        :rtype: str
        """
        return self._distro

    @distro.setter
    def distro(self, distro):
        """Sets the distro of this TypesCVEStats.

        Distro is the impacted image distro (e.g., ubuntu).   # noqa: E501

        :param distro: The distro of this TypesCVEStats.  # noqa: E501
        :type distro: str
        """

        self._distro = distro

    @property
    def distro_release(self):
        """Gets the distro_release of this TypesCVEStats.  # noqa: E501

        DistroRelase is the impacted image distro release (bionic).   # noqa: E501

        :return: The distro_release of this TypesCVEStats.  # noqa: E501
        :rtype: str
        """
        return self._distro_release

    @distro_release.setter
    def distro_release(self, distro_release):
        """Sets the distro_release of this TypesCVEStats.

        DistroRelase is the impacted image distro release (bionic).   # noqa: E501

        :param distro_release: The distro_release of this TypesCVEStats.  # noqa: E501
        :type distro_release: str
        """

        self._distro_release = distro_release

    @property
    def modified(self):
        """Gets the modified of this TypesCVEStats.  # noqa: E501

        Modified is the max unix timestamp for the specific CVE.   # noqa: E501

        :return: The modified of this TypesCVEStats.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this TypesCVEStats.

        Modified is the max unix timestamp for the specific CVE.   # noqa: E501

        :param modified: The modified of this TypesCVEStats.  # noqa: E501
        :type modified: int
        """

        self._modified = modified

    @property
    def type(self):
        """Gets the type of this TypesCVEStats.  # noqa: E501

        Type is the vulnerability type.   # noqa: E501

        :return: The type of this TypesCVEStats.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TypesCVEStats.

        Type is the vulnerability type.   # noqa: E501

        :param type: The type of this TypesCVEStats.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, TypesCVEStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesCVEStats):
            return True

        return self.to_dict() != other.to_dict()