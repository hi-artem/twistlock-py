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


class CodereposPkgDependency(object):
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
        'dev_dependency': 'bool',
        'last_resolved': 'datetime',
        'license_severity': 'str',
        'licenses': 'list[LicenseSPDXLicense]',
        'name': 'str',
        'raw_requirement': 'str',
        'unsupported': 'bool',
        'version': 'str',
        'vulnerabilities': 'list[VulnVulnerability]'
    }

    attribute_map = {
        'dev_dependency': 'devDependency',
        'last_resolved': 'lastResolved',
        'license_severity': 'licenseSeverity',
        'licenses': 'licenses',
        'name': 'name',
        'raw_requirement': 'rawRequirement',
        'unsupported': 'unsupported',
        'version': 'version',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, dev_dependency=None, last_resolved=None, license_severity=None, licenses=None, name=None, raw_requirement=None, unsupported=None, version=None, vulnerabilities=None, local_vars_configuration=None):  # noqa: E501
        """CodereposPkgDependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dev_dependency = None
        self._last_resolved = None
        self._license_severity = None
        self._licenses = None
        self._name = None
        self._raw_requirement = None
        self._unsupported = None
        self._version = None
        self._vulnerabilities = None
        self.discriminator = None

        if dev_dependency is not None:
            self.dev_dependency = dev_dependency
        if last_resolved is not None:
            self.last_resolved = last_resolved
        if license_severity is not None:
            self.license_severity = license_severity
        if licenses is not None:
            self.licenses = licenses
        if name is not None:
            self.name = name
        if raw_requirement is not None:
            self.raw_requirement = raw_requirement
        if unsupported is not None:
            self.unsupported = unsupported
        if version is not None:
            self.version = version
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def dev_dependency(self):
        """Gets the dev_dependency of this CodereposPkgDependency.  # noqa: E501

        Indicates if this dependency is used only for the development of the package (true) or not (false).   # noqa: E501

        :return: The dev_dependency of this CodereposPkgDependency.  # noqa: E501
        :rtype: bool
        """
        return self._dev_dependency

    @dev_dependency.setter
    def dev_dependency(self, dev_dependency):
        """Sets the dev_dependency of this CodereposPkgDependency.

        Indicates if this dependency is used only for the development of the package (true) or not (false).   # noqa: E501

        :param dev_dependency: The dev_dependency of this CodereposPkgDependency.  # noqa: E501
        :type dev_dependency: bool
        """

        self._dev_dependency = dev_dependency

    @property
    def last_resolved(self):
        """Gets the last_resolved of this CodereposPkgDependency.  # noqa: E501

        Date/time of the last version resolution. If the value is zero, it means the version is explicit and does not require resolving.   # noqa: E501

        :return: The last_resolved of this CodereposPkgDependency.  # noqa: E501
        :rtype: datetime
        """
        return self._last_resolved

    @last_resolved.setter
    def last_resolved(self, last_resolved):
        """Sets the last_resolved of this CodereposPkgDependency.

        Date/time of the last version resolution. If the value is zero, it means the version is explicit and does not require resolving.   # noqa: E501

        :param last_resolved: The last_resolved of this CodereposPkgDependency.  # noqa: E501
        :type last_resolved: datetime
        """

        self._last_resolved = last_resolved

    @property
    def license_severity(self):
        """Gets the license_severity of this CodereposPkgDependency.  # noqa: E501

        Maximum severity of the detected licenses according to the compliance policy.   # noqa: E501

        :return: The license_severity of this CodereposPkgDependency.  # noqa: E501
        :rtype: str
        """
        return self._license_severity

    @license_severity.setter
    def license_severity(self, license_severity):
        """Sets the license_severity of this CodereposPkgDependency.

        Maximum severity of the detected licenses according to the compliance policy.   # noqa: E501

        :param license_severity: The license_severity of this CodereposPkgDependency.  # noqa: E501
        :type license_severity: str
        """

        self._license_severity = license_severity

    @property
    def licenses(self):
        """Gets the licenses of this CodereposPkgDependency.  # noqa: E501

        Detected licenses of the dependant package.   # noqa: E501

        :return: The licenses of this CodereposPkgDependency.  # noqa: E501
        :rtype: list[LicenseSPDXLicense]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this CodereposPkgDependency.

        Detected licenses of the dependant package.   # noqa: E501

        :param licenses: The licenses of this CodereposPkgDependency.  # noqa: E501
        :type licenses: list[LicenseSPDXLicense]
        """

        self._licenses = licenses

    @property
    def name(self):
        """Gets the name of this CodereposPkgDependency.  # noqa: E501

        Package name that the dependency refers to.   # noqa: E501

        :return: The name of this CodereposPkgDependency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodereposPkgDependency.

        Package name that the dependency refers to.   # noqa: E501

        :param name: The name of this CodereposPkgDependency.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def raw_requirement(self):
        """Gets the raw_requirement of this CodereposPkgDependency.  # noqa: E501

        Line in which the package is declared.   # noqa: E501

        :return: The raw_requirement of this CodereposPkgDependency.  # noqa: E501
        :rtype: str
        """
        return self._raw_requirement

    @raw_requirement.setter
    def raw_requirement(self, raw_requirement):
        """Sets the raw_requirement of this CodereposPkgDependency.

        Line in which the package is declared.   # noqa: E501

        :param raw_requirement: The raw_requirement of this CodereposPkgDependency.  # noqa: E501
        :type raw_requirement: str
        """

        self._raw_requirement = raw_requirement

    @property
    def unsupported(self):
        """Gets the unsupported of this CodereposPkgDependency.  # noqa: E501

        Indicates if this package is unsupported by the remote package manager DB (e.g., due to a bad name or private package) (true) or not (false).   # noqa: E501

        :return: The unsupported of this CodereposPkgDependency.  # noqa: E501
        :rtype: bool
        """
        return self._unsupported

    @unsupported.setter
    def unsupported(self, unsupported):
        """Sets the unsupported of this CodereposPkgDependency.

        Indicates if this package is unsupported by the remote package manager DB (e.g., due to a bad name or private package) (true) or not (false).   # noqa: E501

        :param unsupported: The unsupported of this CodereposPkgDependency.  # noqa: E501
        :type unsupported: bool
        """

        self._unsupported = unsupported

    @property
    def version(self):
        """Gets the version of this CodereposPkgDependency.  # noqa: E501

        Package version, either explicitly specified in a manifest or resolved by the scanner.   # noqa: E501

        :return: The version of this CodereposPkgDependency.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CodereposPkgDependency.

        Package version, either explicitly specified in a manifest or resolved by the scanner.   # noqa: E501

        :param version: The version of this CodereposPkgDependency.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this CodereposPkgDependency.  # noqa: E501

        Vulnerabilities in the package.   # noqa: E501

        :return: The vulnerabilities of this CodereposPkgDependency.  # noqa: E501
        :rtype: list[VulnVulnerability]
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this CodereposPkgDependency.

        Vulnerabilities in the package.   # noqa: E501

        :param vulnerabilities: The vulnerabilities of this CodereposPkgDependency.  # noqa: E501
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
        if not isinstance(other, CodereposPkgDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CodereposPkgDependency):
            return True

        return self.to_dict() != other.to_dict()
