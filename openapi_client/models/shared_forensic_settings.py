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


class SharedForensicSettings(object):
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
        'collect_network_firewall': 'bool',
        'collect_network_snapshot': 'bool',
        'container_disk_usage_mb': 'int',
        'enabled': 'bool',
        'host_disk_usage_mb': 'int',
        'incident_snapshots_cap': 'int'
    }

    attribute_map = {
        'collect_network_firewall': 'collectNetworkFirewall',
        'collect_network_snapshot': 'collectNetworkSnapshot',
        'container_disk_usage_mb': 'containerDiskUsageMb',
        'enabled': 'enabled',
        'host_disk_usage_mb': 'hostDiskUsageMb',
        'incident_snapshots_cap': 'incidentSnapshotsCap'
    }

    def __init__(self, collect_network_firewall=None, collect_network_snapshot=None, container_disk_usage_mb=None, enabled=None, host_disk_usage_mb=None, incident_snapshots_cap=None, local_vars_configuration=None):  # noqa: E501
        """SharedForensicSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._collect_network_firewall = None
        self._collect_network_snapshot = None
        self._container_disk_usage_mb = None
        self._enabled = None
        self._host_disk_usage_mb = None
        self._incident_snapshots_cap = None
        self.discriminator = None

        if collect_network_firewall is not None:
            self.collect_network_firewall = collect_network_firewall
        if collect_network_snapshot is not None:
            self.collect_network_snapshot = collect_network_snapshot
        if container_disk_usage_mb is not None:
            self.container_disk_usage_mb = container_disk_usage_mb
        if enabled is not None:
            self.enabled = enabled
        if host_disk_usage_mb is not None:
            self.host_disk_usage_mb = host_disk_usage_mb
        if incident_snapshots_cap is not None:
            self.incident_snapshots_cap = incident_snapshots_cap

    @property
    def collect_network_firewall(self):
        """Gets the collect_network_firewall of this SharedForensicSettings.  # noqa: E501

        CollectNetworkFirewall indicates whether network firewall collection is enabled.   # noqa: E501

        :return: The collect_network_firewall of this SharedForensicSettings.  # noqa: E501
        :rtype: bool
        """
        return self._collect_network_firewall

    @collect_network_firewall.setter
    def collect_network_firewall(self, collect_network_firewall):
        """Sets the collect_network_firewall of this SharedForensicSettings.

        CollectNetworkFirewall indicates whether network firewall collection is enabled.   # noqa: E501

        :param collect_network_firewall: The collect_network_firewall of this SharedForensicSettings.  # noqa: E501
        :type collect_network_firewall: bool
        """

        self._collect_network_firewall = collect_network_firewall

    @property
    def collect_network_snapshot(self):
        """Gets the collect_network_snapshot of this SharedForensicSettings.  # noqa: E501

        CollectNetworkSnapshot indicates whether network snapshot collection is enabled.   # noqa: E501

        :return: The collect_network_snapshot of this SharedForensicSettings.  # noqa: E501
        :rtype: bool
        """
        return self._collect_network_snapshot

    @collect_network_snapshot.setter
    def collect_network_snapshot(self, collect_network_snapshot):
        """Sets the collect_network_snapshot of this SharedForensicSettings.

        CollectNetworkSnapshot indicates whether network snapshot collection is enabled.   # noqa: E501

        :param collect_network_snapshot: The collect_network_snapshot of this SharedForensicSettings.  # noqa: E501
        :type collect_network_snapshot: bool
        """

        self._collect_network_snapshot = collect_network_snapshot

    @property
    def container_disk_usage_mb(self):
        """Gets the container_disk_usage_mb of this SharedForensicSettings.  # noqa: E501

        ContainerDiskUsageMb is the maximum amount of disk space used to store the container historical forensic events.   # noqa: E501

        :return: The container_disk_usage_mb of this SharedForensicSettings.  # noqa: E501
        :rtype: int
        """
        return self._container_disk_usage_mb

    @container_disk_usage_mb.setter
    def container_disk_usage_mb(self, container_disk_usage_mb):
        """Sets the container_disk_usage_mb of this SharedForensicSettings.

        ContainerDiskUsageMb is the maximum amount of disk space used to store the container historical forensic events.   # noqa: E501

        :param container_disk_usage_mb: The container_disk_usage_mb of this SharedForensicSettings.  # noqa: E501
        :type container_disk_usage_mb: int
        """

        self._container_disk_usage_mb = container_disk_usage_mb

    @property
    def enabled(self):
        """Gets the enabled of this SharedForensicSettings.  # noqa: E501

        Enabled indicates whether host and container forensic data collection is enabled.   # noqa: E501

        :return: The enabled of this SharedForensicSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SharedForensicSettings.

        Enabled indicates whether host and container forensic data collection is enabled.   # noqa: E501

        :param enabled: The enabled of this SharedForensicSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def host_disk_usage_mb(self):
        """Gets the host_disk_usage_mb of this SharedForensicSettings.  # noqa: E501

        HostDiskUsageMb is the maximum amount of disk space used to store the host historical forensic events.   # noqa: E501

        :return: The host_disk_usage_mb of this SharedForensicSettings.  # noqa: E501
        :rtype: int
        """
        return self._host_disk_usage_mb

    @host_disk_usage_mb.setter
    def host_disk_usage_mb(self, host_disk_usage_mb):
        """Sets the host_disk_usage_mb of this SharedForensicSettings.

        HostDiskUsageMb is the maximum amount of disk space used to store the host historical forensic events.   # noqa: E501

        :param host_disk_usage_mb: The host_disk_usage_mb of this SharedForensicSettings.  # noqa: E501
        :type host_disk_usage_mb: int
        """

        self._host_disk_usage_mb = host_disk_usage_mb

    @property
    def incident_snapshots_cap(self):
        """Gets the incident_snapshots_cap of this SharedForensicSettings.  # noqa: E501

        IncidentSnapshotCap is the maximum amount of incident snapshots we store.   # noqa: E501

        :return: The incident_snapshots_cap of this SharedForensicSettings.  # noqa: E501
        :rtype: int
        """
        return self._incident_snapshots_cap

    @incident_snapshots_cap.setter
    def incident_snapshots_cap(self, incident_snapshots_cap):
        """Sets the incident_snapshots_cap of this SharedForensicSettings.

        IncidentSnapshotCap is the maximum amount of incident snapshots we store.   # noqa: E501

        :param incident_snapshots_cap: The incident_snapshots_cap of this SharedForensicSettings.  # noqa: E501
        :type incident_snapshots_cap: int
        """

        self._incident_snapshots_cap = incident_snapshots_cap

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
        if not isinstance(other, SharedForensicSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedForensicSettings):
            return True

        return self.to_dict() != other.to_dict()
