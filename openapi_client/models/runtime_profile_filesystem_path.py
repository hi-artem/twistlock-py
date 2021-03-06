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


class RuntimeProfileFilesystemPath(object):
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
        'mount': 'bool',
        'path': 'str',
        'process': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'mount': 'mount',
        'path': 'path',
        'process': 'process',
        'time': 'time'
    }

    def __init__(self, mount=None, path=None, process=None, time=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeProfileFilesystemPath - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._mount = None
        self._path = None
        self._process = None
        self._time = None
        self.discriminator = None

        if mount is not None:
            self.mount = mount
        if path is not None:
            self.path = path
        if process is not None:
            self.process = process
        if time is not None:
            self.time = time

    @property
    def mount(self):
        """Gets the mount of this RuntimeProfileFilesystemPath.  # noqa: E501

        Mount indicates whether the given folder is a mount.   # noqa: E501

        :return: The mount of this RuntimeProfileFilesystemPath.  # noqa: E501
        :rtype: bool
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this RuntimeProfileFilesystemPath.

        Mount indicates whether the given folder is a mount.   # noqa: E501

        :param mount: The mount of this RuntimeProfileFilesystemPath.  # noqa: E501
        :type mount: bool
        """

        self._mount = mount

    @property
    def path(self):
        """Gets the path of this RuntimeProfileFilesystemPath.  # noqa: E501

        Path is the file path.   # noqa: E501

        :return: The path of this RuntimeProfileFilesystemPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RuntimeProfileFilesystemPath.

        Path is the file path.   # noqa: E501

        :param path: The path of this RuntimeProfileFilesystemPath.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def process(self):
        """Gets the process of this RuntimeProfileFilesystemPath.  # noqa: E501

        Process is the process that accessed the file.   # noqa: E501

        :return: The process of this RuntimeProfileFilesystemPath.  # noqa: E501
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this RuntimeProfileFilesystemPath.

        Process is the process that accessed the file.   # noqa: E501

        :param process: The process of this RuntimeProfileFilesystemPath.  # noqa: E501
        :type process: str
        """

        self._process = process

    @property
    def time(self):
        """Gets the time of this RuntimeProfileFilesystemPath.  # noqa: E501

        Time is the time in which the file was added.   # noqa: E501

        :return: The time of this RuntimeProfileFilesystemPath.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RuntimeProfileFilesystemPath.

        Time is the time in which the file was added.   # noqa: E501

        :param time: The time of this RuntimeProfileFilesystemPath.  # noqa: E501
        :type time: datetime
        """

        self._time = time

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
        if not isinstance(other, RuntimeProfileFilesystemPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeProfileFilesystemPath):
            return True

        return self.to_dict() != other.to_dict()
