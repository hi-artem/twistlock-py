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


class SharedScanSettings(object):
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
        'cloud_platforms_scan_period_ms': 'int',
        'code_repos_scan_period_ms': 'int',
        'containers_scan_period_ms': 'int',
        'extract_archive': 'bool',
        'images_scan_period_ms': 'int',
        'include_js_dependencies': 'bool',
        'registry_scan_period_ms': 'int',
        'registry_scan_retention_days': 'int',
        'scan_running_images': 'bool',
        'serverless_scan_period_ms': 'int',
        'show_infra_containers': 'bool',
        'show_negligible_vulnerabilities': 'bool',
        'system_scan_period_ms': 'int',
        'tas_droplets_scan_period_ms': 'int',
        'vm_scan_period_ms': 'int'
    }

    attribute_map = {
        'cloud_platforms_scan_period_ms': 'cloudPlatformsScanPeriodMs',
        'code_repos_scan_period_ms': 'codeReposScanPeriodMs',
        'containers_scan_period_ms': 'containersScanPeriodMs',
        'extract_archive': 'extractArchive',
        'images_scan_period_ms': 'imagesScanPeriodMs',
        'include_js_dependencies': 'includeJsDependencies',
        'registry_scan_period_ms': 'registryScanPeriodMs',
        'registry_scan_retention_days': 'registryScanRetentionDays',
        'scan_running_images': 'scanRunningImages',
        'serverless_scan_period_ms': 'serverlessScanPeriodMs',
        'show_infra_containers': 'showInfraContainers',
        'show_negligible_vulnerabilities': 'showNegligibleVulnerabilities',
        'system_scan_period_ms': 'systemScanPeriodMs',
        'tas_droplets_scan_period_ms': 'tasDropletsScanPeriodMs',
        'vm_scan_period_ms': 'vmScanPeriodMs'
    }

    def __init__(self, cloud_platforms_scan_period_ms=None, code_repos_scan_period_ms=None, containers_scan_period_ms=None, extract_archive=None, images_scan_period_ms=None, include_js_dependencies=None, registry_scan_period_ms=None, registry_scan_retention_days=None, scan_running_images=None, serverless_scan_period_ms=None, show_infra_containers=None, show_negligible_vulnerabilities=None, system_scan_period_ms=None, tas_droplets_scan_period_ms=None, vm_scan_period_ms=None, local_vars_configuration=None):  # noqa: E501
        """SharedScanSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_platforms_scan_period_ms = None
        self._code_repos_scan_period_ms = None
        self._containers_scan_period_ms = None
        self._extract_archive = None
        self._images_scan_period_ms = None
        self._include_js_dependencies = None
        self._registry_scan_period_ms = None
        self._registry_scan_retention_days = None
        self._scan_running_images = None
        self._serverless_scan_period_ms = None
        self._show_infra_containers = None
        self._show_negligible_vulnerabilities = None
        self._system_scan_period_ms = None
        self._tas_droplets_scan_period_ms = None
        self._vm_scan_period_ms = None
        self.discriminator = None

        if cloud_platforms_scan_period_ms is not None:
            self.cloud_platforms_scan_period_ms = cloud_platforms_scan_period_ms
        if code_repos_scan_period_ms is not None:
            self.code_repos_scan_period_ms = code_repos_scan_period_ms
        if containers_scan_period_ms is not None:
            self.containers_scan_period_ms = containers_scan_period_ms
        if extract_archive is not None:
            self.extract_archive = extract_archive
        if images_scan_period_ms is not None:
            self.images_scan_period_ms = images_scan_period_ms
        if include_js_dependencies is not None:
            self.include_js_dependencies = include_js_dependencies
        if registry_scan_period_ms is not None:
            self.registry_scan_period_ms = registry_scan_period_ms
        if registry_scan_retention_days is not None:
            self.registry_scan_retention_days = registry_scan_retention_days
        if scan_running_images is not None:
            self.scan_running_images = scan_running_images
        if serverless_scan_period_ms is not None:
            self.serverless_scan_period_ms = serverless_scan_period_ms
        if show_infra_containers is not None:
            self.show_infra_containers = show_infra_containers
        if show_negligible_vulnerabilities is not None:
            self.show_negligible_vulnerabilities = show_negligible_vulnerabilities
        if system_scan_period_ms is not None:
            self.system_scan_period_ms = system_scan_period_ms
        if tas_droplets_scan_period_ms is not None:
            self.tas_droplets_scan_period_ms = tas_droplets_scan_period_ms
        if vm_scan_period_ms is not None:
            self.vm_scan_period_ms = vm_scan_period_ms

    @property
    def cloud_platforms_scan_period_ms(self):
        """Gets the cloud_platforms_scan_period_ms of this SharedScanSettings.  # noqa: E501

        CloudPlatformsScanPeriodMS is the cloud platforms scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The cloud_platforms_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._cloud_platforms_scan_period_ms

    @cloud_platforms_scan_period_ms.setter
    def cloud_platforms_scan_period_ms(self, cloud_platforms_scan_period_ms):
        """Sets the cloud_platforms_scan_period_ms of this SharedScanSettings.

        CloudPlatformsScanPeriodMS is the cloud platforms scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param cloud_platforms_scan_period_ms: The cloud_platforms_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type cloud_platforms_scan_period_ms: int
        """

        self._cloud_platforms_scan_period_ms = cloud_platforms_scan_period_ms

    @property
    def code_repos_scan_period_ms(self):
        """Gets the code_repos_scan_period_ms of this SharedScanSettings.  # noqa: E501

        CodeReposScanPeriodMS is the code repository scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The code_repos_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._code_repos_scan_period_ms

    @code_repos_scan_period_ms.setter
    def code_repos_scan_period_ms(self, code_repos_scan_period_ms):
        """Sets the code_repos_scan_period_ms of this SharedScanSettings.

        CodeReposScanPeriodMS is the code repository scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param code_repos_scan_period_ms: The code_repos_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type code_repos_scan_period_ms: int
        """

        self._code_repos_scan_period_ms = code_repos_scan_period_ms

    @property
    def containers_scan_period_ms(self):
        """Gets the containers_scan_period_ms of this SharedScanSettings.  # noqa: E501

        ContainersScanPeriodMS is the container scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The containers_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._containers_scan_period_ms

    @containers_scan_period_ms.setter
    def containers_scan_period_ms(self, containers_scan_period_ms):
        """Sets the containers_scan_period_ms of this SharedScanSettings.

        ContainersScanPeriodMS is the container scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param containers_scan_period_ms: The containers_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type containers_scan_period_ms: int
        """

        self._containers_scan_period_ms = containers_scan_period_ms

    @property
    def extract_archive(self):
        """Gets the extract_archive of this SharedScanSettings.  # noqa: E501

        ExtractArchive indicates whether to search within archive during scan is enabled.   # noqa: E501

        :return: The extract_archive of this SharedScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._extract_archive

    @extract_archive.setter
    def extract_archive(self, extract_archive):
        """Sets the extract_archive of this SharedScanSettings.

        ExtractArchive indicates whether to search within archive during scan is enabled.   # noqa: E501

        :param extract_archive: The extract_archive of this SharedScanSettings.  # noqa: E501
        :type extract_archive: bool
        """

        self._extract_archive = extract_archive

    @property
    def images_scan_period_ms(self):
        """Gets the images_scan_period_ms of this SharedScanSettings.  # noqa: E501

        ImageScanPeriodMS is the image scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The images_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._images_scan_period_ms

    @images_scan_period_ms.setter
    def images_scan_period_ms(self, images_scan_period_ms):
        """Sets the images_scan_period_ms of this SharedScanSettings.

        ImageScanPeriodMS is the image scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param images_scan_period_ms: The images_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type images_scan_period_ms: int
        """

        self._images_scan_period_ms = images_scan_period_ms

    @property
    def include_js_dependencies(self):
        """Gets the include_js_dependencies of this SharedScanSettings.  # noqa: E501

        IncludeJsDependencies indicates whether to include packages from the \"dependencies\".   # noqa: E501

        :return: The include_js_dependencies of this SharedScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._include_js_dependencies

    @include_js_dependencies.setter
    def include_js_dependencies(self, include_js_dependencies):
        """Sets the include_js_dependencies of this SharedScanSettings.

        IncludeJsDependencies indicates whether to include packages from the \"dependencies\".   # noqa: E501

        :param include_js_dependencies: The include_js_dependencies of this SharedScanSettings.  # noqa: E501
        :type include_js_dependencies: bool
        """

        self._include_js_dependencies = include_js_dependencies

    @property
    def registry_scan_period_ms(self):
        """Gets the registry_scan_period_ms of this SharedScanSettings.  # noqa: E501

        RegistryScanPeriodMS is the registry scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The registry_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._registry_scan_period_ms

    @registry_scan_period_ms.setter
    def registry_scan_period_ms(self, registry_scan_period_ms):
        """Sets the registry_scan_period_ms of this SharedScanSettings.

        RegistryScanPeriodMS is the registry scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param registry_scan_period_ms: The registry_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type registry_scan_period_ms: int
        """

        self._registry_scan_period_ms = registry_scan_period_ms

    @property
    def registry_scan_retention_days(self):
        """Gets the registry_scan_retention_days of this SharedScanSettings.  # noqa: E501

        RegistryScanRetentionDays is the number of days to keep deleted registry images.   # noqa: E501

        :return: The registry_scan_retention_days of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._registry_scan_retention_days

    @registry_scan_retention_days.setter
    def registry_scan_retention_days(self, registry_scan_retention_days):
        """Sets the registry_scan_retention_days of this SharedScanSettings.

        RegistryScanRetentionDays is the number of days to keep deleted registry images.   # noqa: E501

        :param registry_scan_retention_days: The registry_scan_retention_days of this SharedScanSettings.  # noqa: E501
        :type registry_scan_retention_days: int
        """

        self._registry_scan_retention_days = registry_scan_retention_days

    @property
    def scan_running_images(self):
        """Gets the scan_running_images of this SharedScanSettings.  # noqa: E501

        ScanRunningImages indicates only images that are used by containers should be used.   # noqa: E501

        :return: The scan_running_images of this SharedScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._scan_running_images

    @scan_running_images.setter
    def scan_running_images(self, scan_running_images):
        """Sets the scan_running_images of this SharedScanSettings.

        ScanRunningImages indicates only images that are used by containers should be used.   # noqa: E501

        :param scan_running_images: The scan_running_images of this SharedScanSettings.  # noqa: E501
        :type scan_running_images: bool
        """

        self._scan_running_images = scan_running_images

    @property
    def serverless_scan_period_ms(self):
        """Gets the serverless_scan_period_ms of this SharedScanSettings.  # noqa: E501

        ServerlessScanPeriodMS is the serverless vulnerability scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The serverless_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._serverless_scan_period_ms

    @serverless_scan_period_ms.setter
    def serverless_scan_period_ms(self, serverless_scan_period_ms):
        """Sets the serverless_scan_period_ms of this SharedScanSettings.

        ServerlessScanPeriodMS is the serverless vulnerability scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param serverless_scan_period_ms: The serverless_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type serverless_scan_period_ms: int
        """

        self._serverless_scan_period_ms = serverless_scan_period_ms

    @property
    def show_infra_containers(self):
        """Gets the show_infra_containers of this SharedScanSettings.  # noqa: E501

        ShowInfraContainers indicates infra containers should be shown.   # noqa: E501

        :return: The show_infra_containers of this SharedScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_infra_containers

    @show_infra_containers.setter
    def show_infra_containers(self, show_infra_containers):
        """Sets the show_infra_containers of this SharedScanSettings.

        ShowInfraContainers indicates infra containers should be shown.   # noqa: E501

        :param show_infra_containers: The show_infra_containers of this SharedScanSettings.  # noqa: E501
        :type show_infra_containers: bool
        """

        self._show_infra_containers = show_infra_containers

    @property
    def show_negligible_vulnerabilities(self):
        """Gets the show_negligible_vulnerabilities of this SharedScanSettings.  # noqa: E501

        ShowNegligibleVulnerabilities indicates whether to display negligible vulnerabilities (low severity).   # noqa: E501

        :return: The show_negligible_vulnerabilities of this SharedScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_negligible_vulnerabilities

    @show_negligible_vulnerabilities.setter
    def show_negligible_vulnerabilities(self, show_negligible_vulnerabilities):
        """Sets the show_negligible_vulnerabilities of this SharedScanSettings.

        ShowNegligibleVulnerabilities indicates whether to display negligible vulnerabilities (low severity).   # noqa: E501

        :param show_negligible_vulnerabilities: The show_negligible_vulnerabilities of this SharedScanSettings.  # noqa: E501
        :type show_negligible_vulnerabilities: bool
        """

        self._show_negligible_vulnerabilities = show_negligible_vulnerabilities

    @property
    def system_scan_period_ms(self):
        """Gets the system_scan_period_ms of this SharedScanSettings.  # noqa: E501

        SystemScanPeriodMS is the host scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The system_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._system_scan_period_ms

    @system_scan_period_ms.setter
    def system_scan_period_ms(self, system_scan_period_ms):
        """Sets the system_scan_period_ms of this SharedScanSettings.

        SystemScanPeriodMS is the host scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param system_scan_period_ms: The system_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type system_scan_period_ms: int
        """

        self._system_scan_period_ms = system_scan_period_ms

    @property
    def tas_droplets_scan_period_ms(self):
        """Gets the tas_droplets_scan_period_ms of this SharedScanSettings.  # noqa: E501

        TASDropletsScanPeriodMS is the TAS scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The tas_droplets_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._tas_droplets_scan_period_ms

    @tas_droplets_scan_period_ms.setter
    def tas_droplets_scan_period_ms(self, tas_droplets_scan_period_ms):
        """Sets the tas_droplets_scan_period_ms of this SharedScanSettings.

        TASDropletsScanPeriodMS is the TAS scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param tas_droplets_scan_period_ms: The tas_droplets_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type tas_droplets_scan_period_ms: int
        """

        self._tas_droplets_scan_period_ms = tas_droplets_scan_period_ms

    @property
    def vm_scan_period_ms(self):
        """Gets the vm_scan_period_ms of this SharedScanSettings.  # noqa: E501

        VMScanPeriodMS is the VM image scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :return: The vm_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._vm_scan_period_ms

    @vm_scan_period_ms.setter
    def vm_scan_period_ms(self, vm_scan_period_ms):
        """Sets the vm_scan_period_ms of this SharedScanSettings.

        VMScanPeriodMS is the VM image scan period in ms - validated for minimum 1 hour or disabled with zero.   # noqa: E501

        :param vm_scan_period_ms: The vm_scan_period_ms of this SharedScanSettings.  # noqa: E501
        :type vm_scan_period_ms: int
        """

        self._vm_scan_period_ms = vm_scan_period_ms

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
        if not isinstance(other, SharedScanSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedScanSettings):
            return True

        return self.to_dict() != other.to_dict()
