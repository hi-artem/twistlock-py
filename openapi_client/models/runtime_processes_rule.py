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


class RuntimeProcessesRule(object):
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
        'blacklist': 'list[str]',
        'block_all_binaries': 'bool',
        'check_crypto_miners': 'bool',
        'check_lateral_movement': 'bool',
        'check_new_binaries': 'bool',
        'check_parent_child': 'bool',
        'check_suid_binaries': 'bool',
        'effect': 'RuntimeRuleEffect',
        'skip_modified': 'bool',
        'skip_reverse_shell': 'bool',
        'whitelist': 'list[str]'
    }

    attribute_map = {
        'blacklist': 'blacklist',
        'block_all_binaries': 'blockAllBinaries',
        'check_crypto_miners': 'checkCryptoMiners',
        'check_lateral_movement': 'checkLateralMovement',
        'check_new_binaries': 'checkNewBinaries',
        'check_parent_child': 'checkParentChild',
        'check_suid_binaries': 'checkSuidBinaries',
        'effect': 'effect',
        'skip_modified': 'skipModified',
        'skip_reverse_shell': 'skipReverseShell',
        'whitelist': 'whitelist'
    }

    def __init__(self, blacklist=None, block_all_binaries=None, check_crypto_miners=None, check_lateral_movement=None, check_new_binaries=None, check_parent_child=None, check_suid_binaries=None, effect=None, skip_modified=None, skip_reverse_shell=None, whitelist=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeProcessesRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._blacklist = None
        self._block_all_binaries = None
        self._check_crypto_miners = None
        self._check_lateral_movement = None
        self._check_new_binaries = None
        self._check_parent_child = None
        self._check_suid_binaries = None
        self._effect = None
        self._skip_modified = None
        self._skip_reverse_shell = None
        self._whitelist = None
        self.discriminator = None

        if blacklist is not None:
            self.blacklist = blacklist
        if block_all_binaries is not None:
            self.block_all_binaries = block_all_binaries
        if check_crypto_miners is not None:
            self.check_crypto_miners = check_crypto_miners
        if check_lateral_movement is not None:
            self.check_lateral_movement = check_lateral_movement
        if check_new_binaries is not None:
            self.check_new_binaries = check_new_binaries
        if check_parent_child is not None:
            self.check_parent_child = check_parent_child
        if check_suid_binaries is not None:
            self.check_suid_binaries = check_suid_binaries
        if effect is not None:
            self.effect = effect
        if skip_modified is not None:
            self.skip_modified = skip_modified
        if skip_reverse_shell is not None:
            self.skip_reverse_shell = skip_reverse_shell
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def blacklist(self):
        """Gets the blacklist of this RuntimeProcessesRule.  # noqa: E501

        List of processes to deny.   # noqa: E501

        :return: The blacklist of this RuntimeProcessesRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._blacklist

    @blacklist.setter
    def blacklist(self, blacklist):
        """Sets the blacklist of this RuntimeProcessesRule.

        List of processes to deny.   # noqa: E501

        :param blacklist: The blacklist of this RuntimeProcessesRule.  # noqa: E501
        :type blacklist: list[str]
        """

        self._blacklist = blacklist

    @property
    def block_all_binaries(self):
        """Gets the block_all_binaries of this RuntimeProcessesRule.  # noqa: E501

        Indicates that all processes are blocked except the main process.   # noqa: E501

        :return: The block_all_binaries of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._block_all_binaries

    @block_all_binaries.setter
    def block_all_binaries(self, block_all_binaries):
        """Sets the block_all_binaries of this RuntimeProcessesRule.

        Indicates that all processes are blocked except the main process.   # noqa: E501

        :param block_all_binaries: The block_all_binaries of this RuntimeProcessesRule.  # noqa: E501
        :type block_all_binaries: bool
        """

        self._block_all_binaries = block_all_binaries

    @property
    def check_crypto_miners(self):
        """Gets the check_crypto_miners of this RuntimeProcessesRule.  # noqa: E501

        Detect crypto miners.   # noqa: E501

        :return: The check_crypto_miners of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_crypto_miners

    @check_crypto_miners.setter
    def check_crypto_miners(self, check_crypto_miners):
        """Sets the check_crypto_miners of this RuntimeProcessesRule.

        Detect crypto miners.   # noqa: E501

        :param check_crypto_miners: The check_crypto_miners of this RuntimeProcessesRule.  # noqa: E501
        :type check_crypto_miners: bool
        """

        self._check_crypto_miners = check_crypto_miners

    @property
    def check_lateral_movement(self):
        """Gets the check_lateral_movement of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether dectection of processes that can be used for lateral movement exploits is enabled.   # noqa: E501

        :return: The check_lateral_movement of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_lateral_movement

    @check_lateral_movement.setter
    def check_lateral_movement(self, check_lateral_movement):
        """Sets the check_lateral_movement of this RuntimeProcessesRule.

        Indicates whether dectection of processes that can be used for lateral movement exploits is enabled.   # noqa: E501

        :param check_lateral_movement: The check_lateral_movement of this RuntimeProcessesRule.  # noqa: E501
        :type check_lateral_movement: bool
        """

        self._check_lateral_movement = check_lateral_movement

    @property
    def check_new_binaries(self):
        """Gets the check_new_binaries of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether binaries which do not belong to the original image are allowed to run.   # noqa: E501

        :return: The check_new_binaries of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_new_binaries

    @check_new_binaries.setter
    def check_new_binaries(self, check_new_binaries):
        """Sets the check_new_binaries of this RuntimeProcessesRule.

        Indicates whether binaries which do not belong to the original image are allowed to run.   # noqa: E501

        :param check_new_binaries: The check_new_binaries of this RuntimeProcessesRule.  # noqa: E501
        :type check_new_binaries: bool
        """

        self._check_new_binaries = check_new_binaries

    @property
    def check_parent_child(self):
        """Gets the check_parent_child of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether checking for parent child relationship when comparing spawned processes in the model is enabled.   # noqa: E501

        :return: The check_parent_child of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_parent_child

    @check_parent_child.setter
    def check_parent_child(self, check_parent_child):
        """Sets the check_parent_child of this RuntimeProcessesRule.

        Indicates whether checking for parent child relationship when comparing spawned processes in the model is enabled.   # noqa: E501

        :param check_parent_child: The check_parent_child of this RuntimeProcessesRule.  # noqa: E501
        :type check_parent_child: bool
        """

        self._check_parent_child = check_parent_child

    @property
    def check_suid_binaries(self):
        """Gets the check_suid_binaries of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether check for process elevating privileges is enabled (SUID bit).   # noqa: E501

        :return: The check_suid_binaries of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._check_suid_binaries

    @check_suid_binaries.setter
    def check_suid_binaries(self, check_suid_binaries):
        """Sets the check_suid_binaries of this RuntimeProcessesRule.

        Indicates whether check for process elevating privileges is enabled (SUID bit).   # noqa: E501

        :param check_suid_binaries: The check_suid_binaries of this RuntimeProcessesRule.  # noqa: E501
        :type check_suid_binaries: bool
        """

        self._check_suid_binaries = check_suid_binaries

    @property
    def effect(self):
        """Gets the effect of this RuntimeProcessesRule.  # noqa: E501


        :return: The effect of this RuntimeProcessesRule.  # noqa: E501
        :rtype: RuntimeRuleEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this RuntimeProcessesRule.


        :param effect: The effect of this RuntimeProcessesRule.  # noqa: E501
        :type effect: RuntimeRuleEffect
        """

        self._effect = effect

    @property
    def skip_modified(self):
        """Gets the skip_modified of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether to trigger audits/incidents when a modified proc is spawned.   # noqa: E501

        :return: The skip_modified of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._skip_modified

    @skip_modified.setter
    def skip_modified(self, skip_modified):
        """Sets the skip_modified of this RuntimeProcessesRule.

        Indicates whether to trigger audits/incidents when a modified proc is spawned.   # noqa: E501

        :param skip_modified: The skip_modified of this RuntimeProcessesRule.  # noqa: E501
        :type skip_modified: bool
        """

        self._skip_modified = skip_modified

    @property
    def skip_reverse_shell(self):
        """Gets the skip_reverse_shell of this RuntimeProcessesRule.  # noqa: E501

        Indicates whether reverse shell detection is disabled.   # noqa: E501

        :return: The skip_reverse_shell of this RuntimeProcessesRule.  # noqa: E501
        :rtype: bool
        """
        return self._skip_reverse_shell

    @skip_reverse_shell.setter
    def skip_reverse_shell(self, skip_reverse_shell):
        """Sets the skip_reverse_shell of this RuntimeProcessesRule.

        Indicates whether reverse shell detection is disabled.   # noqa: E501

        :param skip_reverse_shell: The skip_reverse_shell of this RuntimeProcessesRule.  # noqa: E501
        :type skip_reverse_shell: bool
        """

        self._skip_reverse_shell = skip_reverse_shell

    @property
    def whitelist(self):
        """Gets the whitelist of this RuntimeProcessesRule.  # noqa: E501

        List of processes to allow.   # noqa: E501

        :return: The whitelist of this RuntimeProcessesRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this RuntimeProcessesRule.

        List of processes to allow.   # noqa: E501

        :param whitelist: The whitelist of this RuntimeProcessesRule.  # noqa: E501
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
        if not isinstance(other, RuntimeProcessesRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeProcessesRule):
            return True

        return self.to_dict() != other.to_dict()