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


class SharedSyslogSettings(object):
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
        'addr': 'str',
        'all_proc_events': 'bool',
        'enabled': 'bool',
        'id': 'str',
        'verbose_scan': 'bool'
    }

    attribute_map = {
        'addr': 'addr',
        'all_proc_events': 'allProcEvents',
        'enabled': 'enabled',
        'id': 'id',
        'verbose_scan': 'verboseScan'
    }

    def __init__(self, addr=None, all_proc_events=None, enabled=None, id=None, verbose_scan=None, local_vars_configuration=None):  # noqa: E501
        """SharedSyslogSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._addr = None
        self._all_proc_events = None
        self._enabled = None
        self._id = None
        self._verbose_scan = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if all_proc_events is not None:
            self.all_proc_events = all_proc_events
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if verbose_scan is not None:
            self.verbose_scan = verbose_scan

    @property
    def addr(self):
        """Gets the addr of this SharedSyslogSettings.  # noqa: E501

        Addr is the remote address for sending events.   # noqa: E501

        :return: The addr of this SharedSyslogSettings.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this SharedSyslogSettings.

        Addr is the remote address for sending events.   # noqa: E501

        :param addr: The addr of this SharedSyslogSettings.  # noqa: E501
        :type addr: str
        """

        self._addr = addr

    @property
    def all_proc_events(self):
        """Gets the all_proc_events of this SharedSyslogSettings.  # noqa: E501

        AllProcEvents indicates whether any new spawned container process should generate an event source entry.   # noqa: E501

        :return: The all_proc_events of this SharedSyslogSettings.  # noqa: E501
        :rtype: bool
        """
        return self._all_proc_events

    @all_proc_events.setter
    def all_proc_events(self, all_proc_events):
        """Sets the all_proc_events of this SharedSyslogSettings.

        AllProcEvents indicates whether any new spawned container process should generate an event source entry.   # noqa: E501

        :param all_proc_events: The all_proc_events of this SharedSyslogSettings.  # noqa: E501
        :type all_proc_events: bool
        """

        self._all_proc_events = all_proc_events

    @property
    def enabled(self):
        """Gets the enabled of this SharedSyslogSettings.  # noqa: E501

        Enabled indicates whether log feature is enabled.   # noqa: E501

        :return: The enabled of this SharedSyslogSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SharedSyslogSettings.

        Enabled indicates whether log feature is enabled.   # noqa: E501

        :param enabled: The enabled of this SharedSyslogSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this SharedSyslogSettings.  # noqa: E501

        ID represents the user's custom identifier string.   # noqa: E501

        :return: The id of this SharedSyslogSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedSyslogSettings.

        ID represents the user's custom identifier string.   # noqa: E501

        :param id: The id of this SharedSyslogSettings.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def verbose_scan(self):
        """Gets the verbose_scan of this SharedSyslogSettings.  # noqa: E501

        VerboseScan indicates whether detailed scan (Compliance/Vulnerability) result should be written to event logger.   # noqa: E501

        :return: The verbose_scan of this SharedSyslogSettings.  # noqa: E501
        :rtype: bool
        """
        return self._verbose_scan

    @verbose_scan.setter
    def verbose_scan(self, verbose_scan):
        """Sets the verbose_scan of this SharedSyslogSettings.

        VerboseScan indicates whether detailed scan (Compliance/Vulnerability) result should be written to event logger.   # noqa: E501

        :param verbose_scan: The verbose_scan of this SharedSyslogSettings.  # noqa: E501
        :type verbose_scan: bool
        """

        self._verbose_scan = verbose_scan

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
        if not isinstance(other, SharedSyslogSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedSyslogSettings):
            return True

        return self.to_dict() != other.to_dict()