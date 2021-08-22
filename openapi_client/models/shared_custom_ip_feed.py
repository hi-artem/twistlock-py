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


class SharedCustomIPFeed(object):
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
        'feed': 'list[str]',
        'modified': 'datetime'
    }

    attribute_map = {
        'id': '_id',
        'digest': 'digest',
        'feed': 'feed',
        'modified': 'modified'
    }

    def __init__(self, id=None, digest=None, feed=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """SharedCustomIPFeed - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._digest = None
        self._feed = None
        self._modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if digest is not None:
            self.digest = digest
        if feed is not None:
            self.feed = feed
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this SharedCustomIPFeed.  # noqa: E501

        ID is the custom feed id.   # noqa: E501

        :return: The id of this SharedCustomIPFeed.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedCustomIPFeed.

        ID is the custom feed id.   # noqa: E501

        :param id: The id of this SharedCustomIPFeed.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def digest(self):
        """Gets the digest of this SharedCustomIPFeed.  # noqa: E501

        Digest is an internal digest of the custom ip feed.   # noqa: E501

        :return: The digest of this SharedCustomIPFeed.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this SharedCustomIPFeed.

        Digest is an internal digest of the custom ip feed.   # noqa: E501

        :param digest: The digest of this SharedCustomIPFeed.  # noqa: E501
        :type digest: str
        """

        self._digest = digest

    @property
    def feed(self):
        """Gets the feed of this SharedCustomIPFeed.  # noqa: E501

        IPs represents a list of IPs  # noqa: E501

        :return: The feed of this SharedCustomIPFeed.  # noqa: E501
        :rtype: list[str]
        """
        return self._feed

    @feed.setter
    def feed(self, feed):
        """Sets the feed of this SharedCustomIPFeed.

        IPs represents a list of IPs  # noqa: E501

        :param feed: The feed of this SharedCustomIPFeed.  # noqa: E501
        :type feed: list[str]
        """

        self._feed = feed

    @property
    def modified(self):
        """Gets the modified of this SharedCustomIPFeed.  # noqa: E501

        Modified is the last time the custom feed was modified.   # noqa: E501

        :return: The modified of this SharedCustomIPFeed.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SharedCustomIPFeed.

        Modified is the last time the custom feed was modified.   # noqa: E501

        :param modified: The modified of this SharedCustomIPFeed.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

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
        if not isinstance(other, SharedCustomIPFeed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedCustomIPFeed):
            return True

        return self.to_dict() != other.to_dict()
