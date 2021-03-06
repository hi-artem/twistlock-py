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


class SharedImageHistory(object):
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
        'base_layer': 'bool',
        'created': 'int',
        'empty_layer': 'bool',
        'id': 'str',
        'instruction': 'str',
        'size_bytes': 'int',
        'tags': 'list[str]',
        'vulnerabilities': 'list[VulnVulnerability]'
    }

    attribute_map = {
        'base_layer': 'baseLayer',
        'created': 'created',
        'empty_layer': 'emptyLayer',
        'id': 'id',
        'instruction': 'instruction',
        'size_bytes': 'sizeBytes',
        'tags': 'tags',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, base_layer=None, created=None, empty_layer=None, id=None, instruction=None, size_bytes=None, tags=None, vulnerabilities=None, local_vars_configuration=None):  # noqa: E501
        """SharedImageHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_layer = None
        self._created = None
        self._empty_layer = None
        self._id = None
        self._instruction = None
        self._size_bytes = None
        self._tags = None
        self._vulnerabilities = None
        self.discriminator = None

        if base_layer is not None:
            self.base_layer = base_layer
        if created is not None:
            self.created = created
        if empty_layer is not None:
            self.empty_layer = empty_layer
        if id is not None:
            self.id = id
        if instruction is not None:
            self.instruction = instruction
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if tags is not None:
            self.tags = tags
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def base_layer(self):
        """Gets the base_layer of this SharedImageHistory.  # noqa: E501

        Indicates if this layer originated from the base image (true) or not (false).   # noqa: E501

        :return: The base_layer of this SharedImageHistory.  # noqa: E501
        :rtype: bool
        """
        return self._base_layer

    @base_layer.setter
    def base_layer(self, base_layer):
        """Sets the base_layer of this SharedImageHistory.

        Indicates if this layer originated from the base image (true) or not (false).   # noqa: E501

        :param base_layer: The base_layer of this SharedImageHistory.  # noqa: E501
        :type base_layer: bool
        """

        self._base_layer = base_layer

    @property
    def created(self):
        """Gets the created of this SharedImageHistory.  # noqa: E501

        Date/time when the image layer was created.   # noqa: E501

        :return: The created of this SharedImageHistory.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SharedImageHistory.

        Date/time when the image layer was created.   # noqa: E501

        :param created: The created of this SharedImageHistory.  # noqa: E501
        :type created: int
        """

        self._created = created

    @property
    def empty_layer(self):
        """Gets the empty_layer of this SharedImageHistory.  # noqa: E501

        Indicates if this instruction didn't create a separate layer (true) or not (false).   # noqa: E501

        :return: The empty_layer of this SharedImageHistory.  # noqa: E501
        :rtype: bool
        """
        return self._empty_layer

    @empty_layer.setter
    def empty_layer(self, empty_layer):
        """Sets the empty_layer of this SharedImageHistory.

        Indicates if this instruction didn't create a separate layer (true) or not (false).   # noqa: E501

        :param empty_layer: The empty_layer of this SharedImageHistory.  # noqa: E501
        :type empty_layer: bool
        """

        self._empty_layer = empty_layer

    @property
    def id(self):
        """Gets the id of this SharedImageHistory.  # noqa: E501

        ID of the layer.   # noqa: E501

        :return: The id of this SharedImageHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedImageHistory.

        ID of the layer.   # noqa: E501

        :param id: The id of this SharedImageHistory.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def instruction(self):
        """Gets the instruction of this SharedImageHistory.  # noqa: E501

        Docker file instruction and arguments used to create this layer.   # noqa: E501

        :return: The instruction of this SharedImageHistory.  # noqa: E501
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this SharedImageHistory.

        Docker file instruction and arguments used to create this layer.   # noqa: E501

        :param instruction: The instruction of this SharedImageHistory.  # noqa: E501
        :type instruction: str
        """

        self._instruction = instruction

    @property
    def size_bytes(self):
        """Gets the size_bytes of this SharedImageHistory.  # noqa: E501

        Size of the layer (in bytes).   # noqa: E501

        :return: The size_bytes of this SharedImageHistory.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this SharedImageHistory.

        Size of the layer (in bytes).   # noqa: E501

        :param size_bytes: The size_bytes of this SharedImageHistory.  # noqa: E501
        :type size_bytes: int
        """

        self._size_bytes = size_bytes

    @property
    def tags(self):
        """Gets the tags of this SharedImageHistory.  # noqa: E501

        Holds the image tags.   # noqa: E501

        :return: The tags of this SharedImageHistory.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SharedImageHistory.

        Holds the image tags.   # noqa: E501

        :param tags: The tags of this SharedImageHistory.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this SharedImageHistory.  # noqa: E501

        Vulnerabilities which originated from this layer.   # noqa: E501

        :return: The vulnerabilities of this SharedImageHistory.  # noqa: E501
        :rtype: list[VulnVulnerability]
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this SharedImageHistory.

        Vulnerabilities which originated from this layer.   # noqa: E501

        :param vulnerabilities: The vulnerabilities of this SharedImageHistory.  # noqa: E501
        :type vulnerabilities: list[VulnVulnerability]
        """

        self._vulnerabilities = vulnerabilities

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
        if not isinstance(other, SharedImageHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedImageHistory):
            return True

        return self.to_dict() != other.to_dict()
