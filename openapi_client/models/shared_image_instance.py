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


class SharedImageInstance(object):
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
        'host': 'str',
        'image': 'str',
        'modified': 'datetime',
        'registry': 'str',
        'repo': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'host': 'host',
        'image': 'image',
        'modified': 'modified',
        'registry': 'registry',
        'repo': 'repo',
        'tag': 'tag'
    }

    def __init__(self, host=None, image=None, modified=None, registry=None, repo=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """SharedImageInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._image = None
        self._modified = None
        self._registry = None
        self._repo = None
        self._tag = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if image is not None:
            self.image = image
        if modified is not None:
            self.modified = modified
        if registry is not None:
            self.registry = registry
        if repo is not None:
            self.repo = repo
        if tag is not None:
            self.tag = tag

    @property
    def host(self):
        """Gets the host of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The host of this SharedImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SharedImageInstance.

        .   # noqa: E501

        :param host: The host of this SharedImageInstance.  # noqa: E501
        :type host: str
        """

        self._host = host

    @property
    def image(self):
        """Gets the image of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The image of this SharedImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SharedImageInstance.

        .   # noqa: E501

        :param image: The image of this SharedImageInstance.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def modified(self):
        """Gets the modified of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The modified of this SharedImageInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SharedImageInstance.

        .   # noqa: E501

        :param modified: The modified of this SharedImageInstance.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def registry(self):
        """Gets the registry of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The registry of this SharedImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this SharedImageInstance.

        .   # noqa: E501

        :param registry: The registry of this SharedImageInstance.  # noqa: E501
        :type registry: str
        """

        self._registry = registry

    @property
    def repo(self):
        """Gets the repo of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The repo of this SharedImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this SharedImageInstance.

        .   # noqa: E501

        :param repo: The repo of this SharedImageInstance.  # noqa: E501
        :type repo: str
        """

        self._repo = repo

    @property
    def tag(self):
        """Gets the tag of this SharedImageInstance.  # noqa: E501

        .   # noqa: E501

        :return: The tag of this SharedImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SharedImageInstance.

        .   # noqa: E501

        :param tag: The tag of this SharedImageInstance.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

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
        if not isinstance(other, SharedImageInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedImageInstance):
            return True

        return self.to_dict() != other.to_dict()