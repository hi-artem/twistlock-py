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


class DefenderStatus(object):
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
        'app_firewall': 'DefenderFeatureStatus',
        'container': 'DefenderScanStatus',
        'container_network_firewall': 'DefenderFeatureStatus',
        'features': 'DefenderFeatureStatus',
        'filesystem': 'DefenderFeatureStatus',
        'host_custom_compliance': 'DefenderFeatureStatus',
        'host_network_firewall': 'DefenderFeatureStatus',
        'image': 'DefenderScanStatus',
        'last_modified': 'datetime',
        'network': 'DefenderFeatureStatus',
        'process': 'DefenderFeatureStatus',
        'registry': 'DefenderScanStatus',
        'runc': 'DefenderFeatureStatus',
        'runtime': 'DefenderFeatureStatus',
        'tas_droplets': 'DefenderScanStatus',
        'upgrade': 'DefenderUpgradeStatus'
    }

    attribute_map = {
        'app_firewall': 'appFirewall',
        'container': 'container',
        'container_network_firewall': 'containerNetworkFirewall',
        'features': 'features',
        'filesystem': 'filesystem',
        'host_custom_compliance': 'hostCustomCompliance',
        'host_network_firewall': 'hostNetworkFirewall',
        'image': 'image',
        'last_modified': 'lastModified',
        'network': 'network',
        'process': 'process',
        'registry': 'registry',
        'runc': 'runc',
        'runtime': 'runtime',
        'tas_droplets': 'tasDroplets',
        'upgrade': 'upgrade'
    }

    def __init__(self, app_firewall=None, container=None, container_network_firewall=None, features=None, filesystem=None, host_custom_compliance=None, host_network_firewall=None, image=None, last_modified=None, network=None, process=None, registry=None, runc=None, runtime=None, tas_droplets=None, upgrade=None, local_vars_configuration=None):  # noqa: E501
        """DefenderStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_firewall = None
        self._container = None
        self._container_network_firewall = None
        self._features = None
        self._filesystem = None
        self._host_custom_compliance = None
        self._host_network_firewall = None
        self._image = None
        self._last_modified = None
        self._network = None
        self._process = None
        self._registry = None
        self._runc = None
        self._runtime = None
        self._tas_droplets = None
        self._upgrade = None
        self.discriminator = None

        if app_firewall is not None:
            self.app_firewall = app_firewall
        if container is not None:
            self.container = container
        if container_network_firewall is not None:
            self.container_network_firewall = container_network_firewall
        if features is not None:
            self.features = features
        if filesystem is not None:
            self.filesystem = filesystem
        if host_custom_compliance is not None:
            self.host_custom_compliance = host_custom_compliance
        if host_network_firewall is not None:
            self.host_network_firewall = host_network_firewall
        if image is not None:
            self.image = image
        if last_modified is not None:
            self.last_modified = last_modified
        if network is not None:
            self.network = network
        if process is not None:
            self.process = process
        if registry is not None:
            self.registry = registry
        if runc is not None:
            self.runc = runc
        if runtime is not None:
            self.runtime = runtime
        if tas_droplets is not None:
            self.tas_droplets = tas_droplets
        if upgrade is not None:
            self.upgrade = upgrade

    @property
    def app_firewall(self):
        """Gets the app_firewall of this DefenderStatus.  # noqa: E501


        :return: The app_firewall of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._app_firewall

    @app_firewall.setter
    def app_firewall(self, app_firewall):
        """Sets the app_firewall of this DefenderStatus.


        :param app_firewall: The app_firewall of this DefenderStatus.  # noqa: E501
        :type app_firewall: DefenderFeatureStatus
        """

        self._app_firewall = app_firewall

    @property
    def container(self):
        """Gets the container of this DefenderStatus.  # noqa: E501


        :return: The container of this DefenderStatus.  # noqa: E501
        :rtype: DefenderScanStatus
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this DefenderStatus.


        :param container: The container of this DefenderStatus.  # noqa: E501
        :type container: DefenderScanStatus
        """

        self._container = container

    @property
    def container_network_firewall(self):
        """Gets the container_network_firewall of this DefenderStatus.  # noqa: E501


        :return: The container_network_firewall of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._container_network_firewall

    @container_network_firewall.setter
    def container_network_firewall(self, container_network_firewall):
        """Sets the container_network_firewall of this DefenderStatus.


        :param container_network_firewall: The container_network_firewall of this DefenderStatus.  # noqa: E501
        :type container_network_firewall: DefenderFeatureStatus
        """

        self._container_network_firewall = container_network_firewall

    @property
    def features(self):
        """Gets the features of this DefenderStatus.  # noqa: E501


        :return: The features of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DefenderStatus.


        :param features: The features of this DefenderStatus.  # noqa: E501
        :type features: DefenderFeatureStatus
        """

        self._features = features

    @property
    def filesystem(self):
        """Gets the filesystem of this DefenderStatus.  # noqa: E501


        :return: The filesystem of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this DefenderStatus.


        :param filesystem: The filesystem of this DefenderStatus.  # noqa: E501
        :type filesystem: DefenderFeatureStatus
        """

        self._filesystem = filesystem

    @property
    def host_custom_compliance(self):
        """Gets the host_custom_compliance of this DefenderStatus.  # noqa: E501


        :return: The host_custom_compliance of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._host_custom_compliance

    @host_custom_compliance.setter
    def host_custom_compliance(self, host_custom_compliance):
        """Sets the host_custom_compliance of this DefenderStatus.


        :param host_custom_compliance: The host_custom_compliance of this DefenderStatus.  # noqa: E501
        :type host_custom_compliance: DefenderFeatureStatus
        """

        self._host_custom_compliance = host_custom_compliance

    @property
    def host_network_firewall(self):
        """Gets the host_network_firewall of this DefenderStatus.  # noqa: E501


        :return: The host_network_firewall of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._host_network_firewall

    @host_network_firewall.setter
    def host_network_firewall(self, host_network_firewall):
        """Sets the host_network_firewall of this DefenderStatus.


        :param host_network_firewall: The host_network_firewall of this DefenderStatus.  # noqa: E501
        :type host_network_firewall: DefenderFeatureStatus
        """

        self._host_network_firewall = host_network_firewall

    @property
    def image(self):
        """Gets the image of this DefenderStatus.  # noqa: E501


        :return: The image of this DefenderStatus.  # noqa: E501
        :rtype: DefenderScanStatus
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DefenderStatus.


        :param image: The image of this DefenderStatus.  # noqa: E501
        :type image: DefenderScanStatus
        """

        self._image = image

    @property
    def last_modified(self):
        """Gets the last_modified of this DefenderStatus.  # noqa: E501

        Datetime the status was last modified.   # noqa: E501

        :return: The last_modified of this DefenderStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this DefenderStatus.

        Datetime the status was last modified.   # noqa: E501

        :param last_modified: The last_modified of this DefenderStatus.  # noqa: E501
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def network(self):
        """Gets the network of this DefenderStatus.  # noqa: E501


        :return: The network of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this DefenderStatus.


        :param network: The network of this DefenderStatus.  # noqa: E501
        :type network: DefenderFeatureStatus
        """

        self._network = network

    @property
    def process(self):
        """Gets the process of this DefenderStatus.  # noqa: E501


        :return: The process of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this DefenderStatus.


        :param process: The process of this DefenderStatus.  # noqa: E501
        :type process: DefenderFeatureStatus
        """

        self._process = process

    @property
    def registry(self):
        """Gets the registry of this DefenderStatus.  # noqa: E501


        :return: The registry of this DefenderStatus.  # noqa: E501
        :rtype: DefenderScanStatus
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this DefenderStatus.


        :param registry: The registry of this DefenderStatus.  # noqa: E501
        :type registry: DefenderScanStatus
        """

        self._registry = registry

    @property
    def runc(self):
        """Gets the runc of this DefenderStatus.  # noqa: E501


        :return: The runc of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._runc

    @runc.setter
    def runc(self, runc):
        """Sets the runc of this DefenderStatus.


        :param runc: The runc of this DefenderStatus.  # noqa: E501
        :type runc: DefenderFeatureStatus
        """

        self._runc = runc

    @property
    def runtime(self):
        """Gets the runtime of this DefenderStatus.  # noqa: E501


        :return: The runtime of this DefenderStatus.  # noqa: E501
        :rtype: DefenderFeatureStatus
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this DefenderStatus.


        :param runtime: The runtime of this DefenderStatus.  # noqa: E501
        :type runtime: DefenderFeatureStatus
        """

        self._runtime = runtime

    @property
    def tas_droplets(self):
        """Gets the tas_droplets of this DefenderStatus.  # noqa: E501


        :return: The tas_droplets of this DefenderStatus.  # noqa: E501
        :rtype: DefenderScanStatus
        """
        return self._tas_droplets

    @tas_droplets.setter
    def tas_droplets(self, tas_droplets):
        """Sets the tas_droplets of this DefenderStatus.


        :param tas_droplets: The tas_droplets of this DefenderStatus.  # noqa: E501
        :type tas_droplets: DefenderScanStatus
        """

        self._tas_droplets = tas_droplets

    @property
    def upgrade(self):
        """Gets the upgrade of this DefenderStatus.  # noqa: E501


        :return: The upgrade of this DefenderStatus.  # noqa: E501
        :rtype: DefenderUpgradeStatus
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this DefenderStatus.


        :param upgrade: The upgrade of this DefenderStatus.  # noqa: E501
        :type upgrade: DefenderUpgradeStatus
        """

        self._upgrade = upgrade

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
        if not isinstance(other, DefenderStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefenderStatus):
            return True

        return self.to_dict() != other.to_dict()
