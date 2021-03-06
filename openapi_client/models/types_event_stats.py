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


class TypesEventStats(object):
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
        'admission_audits': 'int',
        'app_embedded_app_firewall': 'int',
        'app_embedded_runtime': 'int',
        'container_app_firewall': 'int',
        'container_network_firewall': 'int',
        'container_runtime': 'int',
        'docker_access': 'int',
        'file_integrity': 'int',
        'host_activities': 'int',
        'host_app_firewall': 'int',
        'host_network_firewall': 'int',
        'host_runtime': 'int',
        'kubernetes_audits': 'int',
        'log_inspection': 'int',
        'serverless_app_firewall': 'int',
        'serverless_runtime': 'int',
        'trust_audits': 'int'
    }

    attribute_map = {
        'admission_audits': 'admissionAudits',
        'app_embedded_app_firewall': 'appEmbeddedAppFirewall',
        'app_embedded_runtime': 'appEmbeddedRuntime',
        'container_app_firewall': 'containerAppFirewall',
        'container_network_firewall': 'containerNetworkFirewall',
        'container_runtime': 'containerRuntime',
        'docker_access': 'dockerAccess',
        'file_integrity': 'fileIntegrity',
        'host_activities': 'hostActivities',
        'host_app_firewall': 'hostAppFirewall',
        'host_network_firewall': 'hostNetworkFirewall',
        'host_runtime': 'hostRuntime',
        'kubernetes_audits': 'kubernetesAudits',
        'log_inspection': 'logInspection',
        'serverless_app_firewall': 'serverlessAppFirewall',
        'serverless_runtime': 'serverlessRuntime',
        'trust_audits': 'trustAudits'
    }

    def __init__(self, admission_audits=None, app_embedded_app_firewall=None, app_embedded_runtime=None, container_app_firewall=None, container_network_firewall=None, container_runtime=None, docker_access=None, file_integrity=None, host_activities=None, host_app_firewall=None, host_network_firewall=None, host_runtime=None, kubernetes_audits=None, log_inspection=None, serverless_app_firewall=None, serverless_runtime=None, trust_audits=None, local_vars_configuration=None):  # noqa: E501
        """TypesEventStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._admission_audits = None
        self._app_embedded_app_firewall = None
        self._app_embedded_runtime = None
        self._container_app_firewall = None
        self._container_network_firewall = None
        self._container_runtime = None
        self._docker_access = None
        self._file_integrity = None
        self._host_activities = None
        self._host_app_firewall = None
        self._host_network_firewall = None
        self._host_runtime = None
        self._kubernetes_audits = None
        self._log_inspection = None
        self._serverless_app_firewall = None
        self._serverless_runtime = None
        self._trust_audits = None
        self.discriminator = None

        if admission_audits is not None:
            self.admission_audits = admission_audits
        if app_embedded_app_firewall is not None:
            self.app_embedded_app_firewall = app_embedded_app_firewall
        if app_embedded_runtime is not None:
            self.app_embedded_runtime = app_embedded_runtime
        if container_app_firewall is not None:
            self.container_app_firewall = container_app_firewall
        if container_network_firewall is not None:
            self.container_network_firewall = container_network_firewall
        if container_runtime is not None:
            self.container_runtime = container_runtime
        if docker_access is not None:
            self.docker_access = docker_access
        if file_integrity is not None:
            self.file_integrity = file_integrity
        if host_activities is not None:
            self.host_activities = host_activities
        if host_app_firewall is not None:
            self.host_app_firewall = host_app_firewall
        if host_network_firewall is not None:
            self.host_network_firewall = host_network_firewall
        if host_runtime is not None:
            self.host_runtime = host_runtime
        if kubernetes_audits is not None:
            self.kubernetes_audits = kubernetes_audits
        if log_inspection is not None:
            self.log_inspection = log_inspection
        if serverless_app_firewall is not None:
            self.serverless_app_firewall = serverless_app_firewall
        if serverless_runtime is not None:
            self.serverless_runtime = serverless_runtime
        if trust_audits is not None:
            self.trust_audits = trust_audits

    @property
    def admission_audits(self):
        """Gets the admission_audits of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The admission_audits of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._admission_audits

    @admission_audits.setter
    def admission_audits(self, admission_audits):
        """Sets the admission_audits of this TypesEventStats.

        .   # noqa: E501

        :param admission_audits: The admission_audits of this TypesEventStats.  # noqa: E501
        :type admission_audits: int
        """

        self._admission_audits = admission_audits

    @property
    def app_embedded_app_firewall(self):
        """Gets the app_embedded_app_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The app_embedded_app_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._app_embedded_app_firewall

    @app_embedded_app_firewall.setter
    def app_embedded_app_firewall(self, app_embedded_app_firewall):
        """Sets the app_embedded_app_firewall of this TypesEventStats.

        .   # noqa: E501

        :param app_embedded_app_firewall: The app_embedded_app_firewall of this TypesEventStats.  # noqa: E501
        :type app_embedded_app_firewall: int
        """

        self._app_embedded_app_firewall = app_embedded_app_firewall

    @property
    def app_embedded_runtime(self):
        """Gets the app_embedded_runtime of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The app_embedded_runtime of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._app_embedded_runtime

    @app_embedded_runtime.setter
    def app_embedded_runtime(self, app_embedded_runtime):
        """Sets the app_embedded_runtime of this TypesEventStats.

        .   # noqa: E501

        :param app_embedded_runtime: The app_embedded_runtime of this TypesEventStats.  # noqa: E501
        :type app_embedded_runtime: int
        """

        self._app_embedded_runtime = app_embedded_runtime

    @property
    def container_app_firewall(self):
        """Gets the container_app_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The container_app_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._container_app_firewall

    @container_app_firewall.setter
    def container_app_firewall(self, container_app_firewall):
        """Sets the container_app_firewall of this TypesEventStats.

        .   # noqa: E501

        :param container_app_firewall: The container_app_firewall of this TypesEventStats.  # noqa: E501
        :type container_app_firewall: int
        """

        self._container_app_firewall = container_app_firewall

    @property
    def container_network_firewall(self):
        """Gets the container_network_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The container_network_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._container_network_firewall

    @container_network_firewall.setter
    def container_network_firewall(self, container_network_firewall):
        """Sets the container_network_firewall of this TypesEventStats.

        .   # noqa: E501

        :param container_network_firewall: The container_network_firewall of this TypesEventStats.  # noqa: E501
        :type container_network_firewall: int
        """

        self._container_network_firewall = container_network_firewall

    @property
    def container_runtime(self):
        """Gets the container_runtime of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The container_runtime of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._container_runtime

    @container_runtime.setter
    def container_runtime(self, container_runtime):
        """Sets the container_runtime of this TypesEventStats.

        .   # noqa: E501

        :param container_runtime: The container_runtime of this TypesEventStats.  # noqa: E501
        :type container_runtime: int
        """

        self._container_runtime = container_runtime

    @property
    def docker_access(self):
        """Gets the docker_access of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The docker_access of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._docker_access

    @docker_access.setter
    def docker_access(self, docker_access):
        """Sets the docker_access of this TypesEventStats.

        .   # noqa: E501

        :param docker_access: The docker_access of this TypesEventStats.  # noqa: E501
        :type docker_access: int
        """

        self._docker_access = docker_access

    @property
    def file_integrity(self):
        """Gets the file_integrity of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The file_integrity of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._file_integrity

    @file_integrity.setter
    def file_integrity(self, file_integrity):
        """Sets the file_integrity of this TypesEventStats.

        .   # noqa: E501

        :param file_integrity: The file_integrity of this TypesEventStats.  # noqa: E501
        :type file_integrity: int
        """

        self._file_integrity = file_integrity

    @property
    def host_activities(self):
        """Gets the host_activities of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The host_activities of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._host_activities

    @host_activities.setter
    def host_activities(self, host_activities):
        """Sets the host_activities of this TypesEventStats.

        .   # noqa: E501

        :param host_activities: The host_activities of this TypesEventStats.  # noqa: E501
        :type host_activities: int
        """

        self._host_activities = host_activities

    @property
    def host_app_firewall(self):
        """Gets the host_app_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The host_app_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._host_app_firewall

    @host_app_firewall.setter
    def host_app_firewall(self, host_app_firewall):
        """Sets the host_app_firewall of this TypesEventStats.

        .   # noqa: E501

        :param host_app_firewall: The host_app_firewall of this TypesEventStats.  # noqa: E501
        :type host_app_firewall: int
        """

        self._host_app_firewall = host_app_firewall

    @property
    def host_network_firewall(self):
        """Gets the host_network_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The host_network_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._host_network_firewall

    @host_network_firewall.setter
    def host_network_firewall(self, host_network_firewall):
        """Sets the host_network_firewall of this TypesEventStats.

        .   # noqa: E501

        :param host_network_firewall: The host_network_firewall of this TypesEventStats.  # noqa: E501
        :type host_network_firewall: int
        """

        self._host_network_firewall = host_network_firewall

    @property
    def host_runtime(self):
        """Gets the host_runtime of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The host_runtime of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._host_runtime

    @host_runtime.setter
    def host_runtime(self, host_runtime):
        """Sets the host_runtime of this TypesEventStats.

        .   # noqa: E501

        :param host_runtime: The host_runtime of this TypesEventStats.  # noqa: E501
        :type host_runtime: int
        """

        self._host_runtime = host_runtime

    @property
    def kubernetes_audits(self):
        """Gets the kubernetes_audits of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The kubernetes_audits of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._kubernetes_audits

    @kubernetes_audits.setter
    def kubernetes_audits(self, kubernetes_audits):
        """Sets the kubernetes_audits of this TypesEventStats.

        .   # noqa: E501

        :param kubernetes_audits: The kubernetes_audits of this TypesEventStats.  # noqa: E501
        :type kubernetes_audits: int
        """

        self._kubernetes_audits = kubernetes_audits

    @property
    def log_inspection(self):
        """Gets the log_inspection of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The log_inspection of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._log_inspection

    @log_inspection.setter
    def log_inspection(self, log_inspection):
        """Sets the log_inspection of this TypesEventStats.

        .   # noqa: E501

        :param log_inspection: The log_inspection of this TypesEventStats.  # noqa: E501
        :type log_inspection: int
        """

        self._log_inspection = log_inspection

    @property
    def serverless_app_firewall(self):
        """Gets the serverless_app_firewall of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The serverless_app_firewall of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._serverless_app_firewall

    @serverless_app_firewall.setter
    def serverless_app_firewall(self, serverless_app_firewall):
        """Sets the serverless_app_firewall of this TypesEventStats.

        .   # noqa: E501

        :param serverless_app_firewall: The serverless_app_firewall of this TypesEventStats.  # noqa: E501
        :type serverless_app_firewall: int
        """

        self._serverless_app_firewall = serverless_app_firewall

    @property
    def serverless_runtime(self):
        """Gets the serverless_runtime of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The serverless_runtime of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._serverless_runtime

    @serverless_runtime.setter
    def serverless_runtime(self, serverless_runtime):
        """Sets the serverless_runtime of this TypesEventStats.

        .   # noqa: E501

        :param serverless_runtime: The serverless_runtime of this TypesEventStats.  # noqa: E501
        :type serverless_runtime: int
        """

        self._serverless_runtime = serverless_runtime

    @property
    def trust_audits(self):
        """Gets the trust_audits of this TypesEventStats.  # noqa: E501

        .   # noqa: E501

        :return: The trust_audits of this TypesEventStats.  # noqa: E501
        :rtype: int
        """
        return self._trust_audits

    @trust_audits.setter
    def trust_audits(self, trust_audits):
        """Sets the trust_audits of this TypesEventStats.

        .   # noqa: E501

        :param trust_audits: The trust_audits of this TypesEventStats.  # noqa: E501
        :type trust_audits: int
        """

        self._trust_audits = trust_audits

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
        if not isinstance(other, TypesEventStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesEventStats):
            return True

        return self.to_dict() != other.to_dict()
