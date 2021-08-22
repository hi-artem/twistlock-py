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


class DeploymentDaemonSet(object):
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
        'address': 'str',
        'cluster': 'str',
        'credential_id': 'str',
        'defenders_version': 'str',
        'desired_defenders': 'int',
        'error': 'str',
        'has_defender': 'bool',
        'region': 'str',
        'running_defenders': 'int',
        'upgradable': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'cluster': 'cluster',
        'credential_id': 'credentialID',
        'defenders_version': 'defendersVersion',
        'desired_defenders': 'desiredDefenders',
        'error': 'error',
        'has_defender': 'hasDefender',
        'region': 'region',
        'running_defenders': 'runningDefenders',
        'upgradable': 'upgradable'
    }

    def __init__(self, address=None, cluster=None, credential_id=None, defenders_version=None, desired_defenders=None, error=None, has_defender=None, region=None, running_defenders=None, upgradable=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentDaemonSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._cluster = None
        self._credential_id = None
        self._defenders_version = None
        self._desired_defenders = None
        self._error = None
        self._has_defender = None
        self._region = None
        self._running_defenders = None
        self._upgradable = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if cluster is not None:
            self.cluster = cluster
        if credential_id is not None:
            self.credential_id = credential_id
        if defenders_version is not None:
            self.defenders_version = defenders_version
        if desired_defenders is not None:
            self.desired_defenders = desired_defenders
        if error is not None:
            self.error = error
        if has_defender is not None:
            self.has_defender = has_defender
        if region is not None:
            self.region = region
        if running_defenders is not None:
            self.running_defenders = running_defenders
        if upgradable is not None:
            self.upgradable = upgradable

    @property
    def address(self):
        """Gets the address of this DeploymentDaemonSet.  # noqa: E501

        Address is the kubernetes cluster address.   # noqa: E501

        :return: The address of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DeploymentDaemonSet.

        Address is the kubernetes cluster address.   # noqa: E501

        :param address: The address of this DeploymentDaemonSet.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def cluster(self):
        """Gets the cluster of this DeploymentDaemonSet.  # noqa: E501

        Cluster is the kubernetes cluster name.   # noqa: E501

        :return: The cluster of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DeploymentDaemonSet.

        Cluster is the kubernetes cluster name.   # noqa: E501

        :param cluster: The cluster of this DeploymentDaemonSet.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def credential_id(self):
        """Gets the credential_id of this DeploymentDaemonSet.  # noqa: E501

        CredentialID is the name of the credential used.   # noqa: E501

        :return: The credential_id of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this DeploymentDaemonSet.

        CredentialID is the name of the credential used.   # noqa: E501

        :param credential_id: The credential_id of this DeploymentDaemonSet.  # noqa: E501
        :type credential_id: str
        """

        self._credential_id = credential_id

    @property
    def defenders_version(self):
        """Gets the defenders_version of this DeploymentDaemonSet.  # noqa: E501

        DefendersVersion is the version of the defenders deployed.   # noqa: E501

        :return: The defenders_version of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._defenders_version

    @defenders_version.setter
    def defenders_version(self, defenders_version):
        """Sets the defenders_version of this DeploymentDaemonSet.

        DefendersVersion is the version of the defenders deployed.   # noqa: E501

        :param defenders_version: The defenders_version of this DeploymentDaemonSet.  # noqa: E501
        :type defenders_version: str
        """

        self._defenders_version = defenders_version

    @property
    def desired_defenders(self):
        """Gets the desired_defenders of this DeploymentDaemonSet.  # noqa: E501

        DesiredDefenders is the number of desired defenders.   # noqa: E501

        :return: The desired_defenders of this DeploymentDaemonSet.  # noqa: E501
        :rtype: int
        """
        return self._desired_defenders

    @desired_defenders.setter
    def desired_defenders(self, desired_defenders):
        """Sets the desired_defenders of this DeploymentDaemonSet.

        DesiredDefenders is the number of desired defenders.   # noqa: E501

        :param desired_defenders: The desired_defenders of this DeploymentDaemonSet.  # noqa: E501
        :type desired_defenders: int
        """

        self._desired_defenders = desired_defenders

    @property
    def error(self):
        """Gets the error of this DeploymentDaemonSet.  # noqa: E501

        Error indicates any related errors found.   # noqa: E501

        :return: The error of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DeploymentDaemonSet.

        Error indicates any related errors found.   # noqa: E501

        :param error: The error of this DeploymentDaemonSet.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def has_defender(self):
        """Gets the has_defender of this DeploymentDaemonSet.  # noqa: E501

        HasDefender indicates if the cluster has at least one running defender.   # noqa: E501

        :return: The has_defender of this DeploymentDaemonSet.  # noqa: E501
        :rtype: bool
        """
        return self._has_defender

    @has_defender.setter
    def has_defender(self, has_defender):
        """Sets the has_defender of this DeploymentDaemonSet.

        HasDefender indicates if the cluster has at least one running defender.   # noqa: E501

        :param has_defender: The has_defender of this DeploymentDaemonSet.  # noqa: E501
        :type has_defender: bool
        """

        self._has_defender = has_defender

    @property
    def region(self):
        """Gets the region of this DeploymentDaemonSet.  # noqa: E501

        Region is the kubernetes cluster location region.   # noqa: E501

        :return: The region of this DeploymentDaemonSet.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DeploymentDaemonSet.

        Region is the kubernetes cluster location region.   # noqa: E501

        :param region: The region of this DeploymentDaemonSet.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def running_defenders(self):
        """Gets the running_defenders of this DeploymentDaemonSet.  # noqa: E501

        RunningDefenders is the number of defenders running.   # noqa: E501

        :return: The running_defenders of this DeploymentDaemonSet.  # noqa: E501
        :rtype: int
        """
        return self._running_defenders

    @running_defenders.setter
    def running_defenders(self, running_defenders):
        """Sets the running_defenders of this DeploymentDaemonSet.

        RunningDefenders is the number of defenders running.   # noqa: E501

        :param running_defenders: The running_defenders of this DeploymentDaemonSet.  # noqa: E501
        :type running_defenders: int
        """

        self._running_defenders = running_defenders

    @property
    def upgradable(self):
        """Gets the upgradable of this DeploymentDaemonSet.  # noqa: E501

        Upgradable indicates if the cluster is upgradable.   # noqa: E501

        :return: The upgradable of this DeploymentDaemonSet.  # noqa: E501
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        """Sets the upgradable of this DeploymentDaemonSet.

        Upgradable indicates if the cluster is upgradable.   # noqa: E501

        :param upgradable: The upgradable of this DeploymentDaemonSet.  # noqa: E501
        :type upgradable: bool
        """

        self._upgradable = upgradable

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
        if not isinstance(other, DeploymentDaemonSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentDaemonSet):
            return True

        return self.to_dict() != other.to_dict()
