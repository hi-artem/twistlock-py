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


class RuntimeFileIntegrityRule(object):
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
        'dir': 'bool',
        'exclusions': 'list[str]',
        'metadata': 'bool',
        'path': 'str',
        'proc_whitelist': 'list[str]',
        'read': 'bool',
        'recursive': 'bool',
        'write': 'bool'
    }

    attribute_map = {
        'dir': 'dir',
        'exclusions': 'exclusions',
        'metadata': 'metadata',
        'path': 'path',
        'proc_whitelist': 'procWhitelist',
        'read': 'read',
        'recursive': 'recursive',
        'write': 'write'
    }

    def __init__(self, dir=None, exclusions=None, metadata=None, path=None, proc_whitelist=None, read=None, recursive=None, write=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeFileIntegrityRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dir = None
        self._exclusions = None
        self._metadata = None
        self._path = None
        self._proc_whitelist = None
        self._read = None
        self._recursive = None
        self._write = None
        self.discriminator = None

        if dir is not None:
            self.dir = dir
        if exclusions is not None:
            self.exclusions = exclusions
        if metadata is not None:
            self.metadata = metadata
        if path is not None:
            self.path = path
        if proc_whitelist is not None:
            self.proc_whitelist = proc_whitelist
        if read is not None:
            self.read = read
        if recursive is not None:
            self.recursive = recursive
        if write is not None:
            self.write = write

    @property
    def dir(self):
        """Gets the dir of this RuntimeFileIntegrityRule.  # noqa: E501

        Dir indicates that the path is a directory.   # noqa: E501

        :return: The dir of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: bool
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """Sets the dir of this RuntimeFileIntegrityRule.

        Dir indicates that the path is a directory.   # noqa: E501

        :param dir: The dir of this RuntimeFileIntegrityRule.  # noqa: E501
        :type dir: bool
        """

        self._dir = dir

    @property
    def exclusions(self):
        """Gets the exclusions of this RuntimeFileIntegrityRule.  # noqa: E501

        Exclusions are filenames that should be ignored while generating audits These filenames may contain a wildcard regex pattern, e.g. foo*.log, *.cache.   # noqa: E501

        :return: The exclusions of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """Sets the exclusions of this RuntimeFileIntegrityRule.

        Exclusions are filenames that should be ignored while generating audits These filenames may contain a wildcard regex pattern, e.g. foo*.log, *.cache.   # noqa: E501

        :param exclusions: The exclusions of this RuntimeFileIntegrityRule.  # noqa: E501
        :type exclusions: list[str]
        """

        self._exclusions = exclusions

    @property
    def metadata(self):
        """Gets the metadata of this RuntimeFileIntegrityRule.  # noqa: E501

        Metadata indicates that metadata changes should be monitored (e.g. chmod, chown).   # noqa: E501

        :return: The metadata of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: bool
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RuntimeFileIntegrityRule.

        Metadata indicates that metadata changes should be monitored (e.g. chmod, chown).   # noqa: E501

        :param metadata: The metadata of this RuntimeFileIntegrityRule.  # noqa: E501
        :type metadata: bool
        """

        self._metadata = metadata

    @property
    def path(self):
        """Gets the path of this RuntimeFileIntegrityRule.  # noqa: E501

        Path is the path to monitor.   # noqa: E501

        :return: The path of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RuntimeFileIntegrityRule.

        Path is the path to monitor.   # noqa: E501

        :param path: The path of this RuntimeFileIntegrityRule.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def proc_whitelist(self):
        """Gets the proc_whitelist of this RuntimeFileIntegrityRule.  # noqa: E501

        ProcWhitelist are the processes to ignore Filesystem events caused by these processes DO NOT generate file integrity events.   # noqa: E501

        :return: The proc_whitelist of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._proc_whitelist

    @proc_whitelist.setter
    def proc_whitelist(self, proc_whitelist):
        """Sets the proc_whitelist of this RuntimeFileIntegrityRule.

        ProcWhitelist are the processes to ignore Filesystem events caused by these processes DO NOT generate file integrity events.   # noqa: E501

        :param proc_whitelist: The proc_whitelist of this RuntimeFileIntegrityRule.  # noqa: E501
        :type proc_whitelist: list[str]
        """

        self._proc_whitelist = proc_whitelist

    @property
    def read(self):
        """Gets the read of this RuntimeFileIntegrityRule.  # noqa: E501

        Read indicates that reads operations should be monitored.   # noqa: E501

        :return: The read of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this RuntimeFileIntegrityRule.

        Read indicates that reads operations should be monitored.   # noqa: E501

        :param read: The read of this RuntimeFileIntegrityRule.  # noqa: E501
        :type read: bool
        """

        self._read = read

    @property
    def recursive(self):
        """Gets the recursive of this RuntimeFileIntegrityRule.  # noqa: E501

        Recursive indicates that monitoring should be recursive.   # noqa: E501

        :return: The recursive of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        """Sets the recursive of this RuntimeFileIntegrityRule.

        Recursive indicates that monitoring should be recursive.   # noqa: E501

        :param recursive: The recursive of this RuntimeFileIntegrityRule.  # noqa: E501
        :type recursive: bool
        """

        self._recursive = recursive

    @property
    def write(self):
        """Gets the write of this RuntimeFileIntegrityRule.  # noqa: E501

        Write indicates that write operations should be monitored.   # noqa: E501

        :return: The write of this RuntimeFileIntegrityRule.  # noqa: E501
        :rtype: bool
        """
        return self._write

    @write.setter
    def write(self, write):
        """Sets the write of this RuntimeFileIntegrityRule.

        Write indicates that write operations should be monitored.   # noqa: E501

        :param write: The write of this RuntimeFileIntegrityRule.  # noqa: E501
        :type write: bool
        """

        self._write = write

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
        if not isinstance(other, RuntimeFileIntegrityRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeFileIntegrityRule):
            return True

        return self.to_dict() != other.to_dict()
