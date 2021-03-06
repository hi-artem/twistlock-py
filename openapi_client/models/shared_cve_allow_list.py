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


class SharedCVEAllowList(object):
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
        'id': 'str',
        'digest': 'str',
        'rules': 'list[SharedAllowedCVE]'
    }

    attribute_map = {
        'id': '_id',
        'digest': 'digest',
        'rules': 'rules'
    }

    def __init__(self, id=None, digest=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """SharedCVEAllowList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._digest = None
        self._rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if digest is not None:
            self.digest = digest
        if rules is not None:
            self.rules = rules

    @property
    def id(self):
        """Gets the id of this SharedCVEAllowList.  # noqa: E501

        ID is the id of the feed.   # noqa: E501

        :return: The id of this SharedCVEAllowList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedCVEAllowList.

        ID is the id of the feed.   # noqa: E501

        :param id: The id of this SharedCVEAllowList.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def digest(self):
        """Gets the digest of this SharedCVEAllowList.  # noqa: E501

        Digest is the feed digest.   # noqa: E501

        :return: The digest of this SharedCVEAllowList.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this SharedCVEAllowList.

        Digest is the feed digest.   # noqa: E501

        :param digest: The digest of this SharedCVEAllowList.  # noqa: E501
        :type digest: str
        """

        self._digest = digest

    @property
    def rules(self):
        """Gets the rules of this SharedCVEAllowList.  # noqa: E501

        Rules is the list of allowed CVEs.   # noqa: E501

        :return: The rules of this SharedCVEAllowList.  # noqa: E501
        :rtype: list[SharedAllowedCVE]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this SharedCVEAllowList.

        Rules is the list of allowed CVEs.   # noqa: E501

        :param rules: The rules of this SharedCVEAllowList.  # noqa: E501
        :type rules: list[SharedAllowedCVE]
        """

        self._rules = rules

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
        if not isinstance(other, SharedCVEAllowList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedCVEAllowList):
            return True

        return self.to_dict() != other.to_dict()
