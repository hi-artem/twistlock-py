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


class RuntimeFilesystemRule(object):
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
        'backdoor_files': 'bool',
        'blacklist': 'list[str]',
        'check_new_files': 'bool',
        'effect': 'RuntimeRuleEffect',
        'skip_encrypted_binaries': 'bool',
        'suspicious_elf_headers': 'bool',
        'whitelist': 'list[str]'
    }

    attribute_map = {
        'backdoor_files': 'backdoorFiles',
        'blacklist': 'blacklist',
        'check_new_files': 'checkNewFiles',
        'effect': 'effect',
        'skip_encrypted_binaries': 'skipEncryptedBinaries',
        'suspicious_elf_headers': 'suspiciousELFHeaders',
        'whitelist': 'whitelist'
    }

    def __init__(self, backdoor_files=None, blacklist=None, check_new_files=None, effect=None, skip_encrypted_binaries=None, suspicious_elf_headers=None, whitelist=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeFilesystemRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._backdoor_files = None
        self._blacklist = None
        self._check_new_files = None
        self._effect = None
        self._skip_encrypted_binaries = None
        self._suspicious_elf_headers = None
        self._whitelist = None
        self.discriminator = None

        if backdoor_files is not None:
            self.backdoor_files = backdoor_files
        if blacklist is not None:
            self.blacklist = blacklist
        if check_new_files is not None:
            self.check_new_files = check_new_files
        if effect is not None:
            self.effect = effect
        if skip_encrypted_binaries is not None:
            self.skip_encrypted_binaries = skip_encrypted_binaries
        if suspicious_elf_headers is not None:
            self.suspicious_elf_headers = suspicious_elf_headers
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def backdoor_files(self):
        """Gets the backdoor_files of this RuntimeFilesystemRule.  # noqa: E501

        Monitors files that can create and/or persist backdoors (currently SSH and admin account config files) (true).   # noqa: E501

        :return: The backdoor_files of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: bool
        """
        return self._backdoor_files

    @backdoor_files.setter
    def backdoor_files(self, backdoor_files):
        """Sets the backdoor_files of this RuntimeFilesystemRule.

        Monitors files that can create and/or persist backdoors (currently SSH and admin account config files) (true).   # noqa: E501

        :param backdoor_files: The backdoor_files of this RuntimeFilesystemRule.  # noqa: E501
        :type backdoor_files: bool
        """

        self._backdoor_files = backdoor_files

    @property
    def blacklist(self):
        """Gets the blacklist of this RuntimeFilesystemRule.  # noqa: E501

        List of denied file system path.   # noqa: E501

        :return: The blacklist of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._blacklist

    @blacklist.setter
    def blacklist(self, blacklist):
        """Sets the blacklist of this RuntimeFilesystemRule.

        List of denied file system path.   # noqa: E501

        :param blacklist: The blacklist of this RuntimeFilesystemRule.  # noqa: E501
        :type blacklist: list[str]
        """

        self._blacklist = blacklist

    @property
    def check_new_files(self):
        """Gets the check_new_files of this RuntimeFilesystemRule.  # noqa: E501

        Detects changes to binaries and certificates (true).   # noqa: E501

        :return: The check_new_files of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_new_files

    @check_new_files.setter
    def check_new_files(self, check_new_files):
        """Sets the check_new_files of this RuntimeFilesystemRule.

        Detects changes to binaries and certificates (true).   # noqa: E501

        :param check_new_files: The check_new_files of this RuntimeFilesystemRule.  # noqa: E501
        :type check_new_files: bool
        """

        self._check_new_files = check_new_files

    @property
    def effect(self):
        """Gets the effect of this RuntimeFilesystemRule.  # noqa: E501


        :return: The effect of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: RuntimeRuleEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this RuntimeFilesystemRule.


        :param effect: The effect of this RuntimeFilesystemRule.  # noqa: E501
        :type effect: RuntimeRuleEffect
        """

        self._effect = effect

    @property
    def skip_encrypted_binaries(self):
        """Gets the skip_encrypted_binaries of this RuntimeFilesystemRule.  # noqa: E501

        Indicates that encrypted binaries check should be skipped.   # noqa: E501

        :return: The skip_encrypted_binaries of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: bool
        """
        return self._skip_encrypted_binaries

    @skip_encrypted_binaries.setter
    def skip_encrypted_binaries(self, skip_encrypted_binaries):
        """Sets the skip_encrypted_binaries of this RuntimeFilesystemRule.

        Indicates that encrypted binaries check should be skipped.   # noqa: E501

        :param skip_encrypted_binaries: The skip_encrypted_binaries of this RuntimeFilesystemRule.  # noqa: E501
        :type skip_encrypted_binaries: bool
        """

        self._skip_encrypted_binaries = skip_encrypted_binaries

    @property
    def suspicious_elf_headers(self):
        """Gets the suspicious_elf_headers of this RuntimeFilesystemRule.  # noqa: E501

        Indicates whether malware detection based on suspicious ELF headers is enabled.   # noqa: E501

        :return: The suspicious_elf_headers of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: bool
        """
        return self._suspicious_elf_headers

    @suspicious_elf_headers.setter
    def suspicious_elf_headers(self, suspicious_elf_headers):
        """Sets the suspicious_elf_headers of this RuntimeFilesystemRule.

        Indicates whether malware detection based on suspicious ELF headers is enabled.   # noqa: E501

        :param suspicious_elf_headers: The suspicious_elf_headers of this RuntimeFilesystemRule.  # noqa: E501
        :type suspicious_elf_headers: bool
        """

        self._suspicious_elf_headers = suspicious_elf_headers

    @property
    def whitelist(self):
        """Gets the whitelist of this RuntimeFilesystemRule.  # noqa: E501

        List of allowed file system path.   # noqa: E501

        :return: The whitelist of this RuntimeFilesystemRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this RuntimeFilesystemRule.

        List of allowed file system path.   # noqa: E501

        :param whitelist: The whitelist of this RuntimeFilesystemRule.  # noqa: E501
        :type whitelist: list[str]
        """

        self._whitelist = whitelist

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
        if not isinstance(other, RuntimeFilesystemRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeFilesystemRule):
            return True

        return self.to_dict() != other.to_dict()
