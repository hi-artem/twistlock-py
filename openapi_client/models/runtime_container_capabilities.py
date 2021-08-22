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


class RuntimeContainerCapabilities(object):
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
        'ci': 'bool',
        'cloud_metadata': 'bool',
        'dns_cache': 'bool',
        'dynamic_dns_query': 'bool',
        'dynamic_file_creation': 'bool',
        'dynamic_process_creation': 'bool',
        'k8s': 'bool',
        'proxy': 'bool',
        'sshd': 'bool',
        'unpacker': 'bool'
    }

    attribute_map = {
        'ci': 'ci',
        'cloud_metadata': 'cloudMetadata',
        'dns_cache': 'dnsCache',
        'dynamic_dns_query': 'dynamicDNSQuery',
        'dynamic_file_creation': 'dynamicFileCreation',
        'dynamic_process_creation': 'dynamicProcessCreation',
        'k8s': 'k8s',
        'proxy': 'proxy',
        'sshd': 'sshd',
        'unpacker': 'unpacker'
    }

    def __init__(self, ci=None, cloud_metadata=None, dns_cache=None, dynamic_dns_query=None, dynamic_file_creation=None, dynamic_process_creation=None, k8s=None, proxy=None, sshd=None, unpacker=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeContainerCapabilities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ci = None
        self._cloud_metadata = None
        self._dns_cache = None
        self._dynamic_dns_query = None
        self._dynamic_file_creation = None
        self._dynamic_process_creation = None
        self._k8s = None
        self._proxy = None
        self._sshd = None
        self._unpacker = None
        self.discriminator = None

        if ci is not None:
            self.ci = ci
        if cloud_metadata is not None:
            self.cloud_metadata = cloud_metadata
        if dns_cache is not None:
            self.dns_cache = dns_cache
        if dynamic_dns_query is not None:
            self.dynamic_dns_query = dynamic_dns_query
        if dynamic_file_creation is not None:
            self.dynamic_file_creation = dynamic_file_creation
        if dynamic_process_creation is not None:
            self.dynamic_process_creation = dynamic_process_creation
        if k8s is not None:
            self.k8s = k8s
        if proxy is not None:
            self.proxy = proxy
        if sshd is not None:
            self.sshd = sshd
        if unpacker is not None:
            self.unpacker = unpacker

    @property
    def ci(self):
        """Gets the ci of this RuntimeContainerCapabilities.  # noqa: E501

        CI indicates the container allowed to write binaries to disk and run them.   # noqa: E501

        :return: The ci of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._ci

    @ci.setter
    def ci(self, ci):
        """Sets the ci of this RuntimeContainerCapabilities.

        CI indicates the container allowed to write binaries to disk and run them.   # noqa: E501

        :param ci: The ci of this RuntimeContainerCapabilities.  # noqa: E501
        :type ci: bool
        """

        self._ci = ci

    @property
    def cloud_metadata(self):
        """Gets the cloud_metadata of this RuntimeContainerCapabilities.  # noqa: E501

        CloudMetadata indicates the given container can query cloud metadata api.   # noqa: E501

        :return: The cloud_metadata of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_metadata

    @cloud_metadata.setter
    def cloud_metadata(self, cloud_metadata):
        """Sets the cloud_metadata of this RuntimeContainerCapabilities.

        CloudMetadata indicates the given container can query cloud metadata api.   # noqa: E501

        :param cloud_metadata: The cloud_metadata of this RuntimeContainerCapabilities.  # noqa: E501
        :type cloud_metadata: bool
        """

        self._cloud_metadata = cloud_metadata

    @property
    def dns_cache(self):
        """Gets the dns_cache of this RuntimeContainerCapabilities.  # noqa: E501

        DNSCache are DNS services that are used by all the pods in the cluster.   # noqa: E501

        :return: The dns_cache of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._dns_cache

    @dns_cache.setter
    def dns_cache(self, dns_cache):
        """Sets the dns_cache of this RuntimeContainerCapabilities.

        DNSCache are DNS services that are used by all the pods in the cluster.   # noqa: E501

        :param dns_cache: The dns_cache of this RuntimeContainerCapabilities.  # noqa: E501
        :type dns_cache: bool
        """

        self._dns_cache = dns_cache

    @property
    def dynamic_dns_query(self):
        """Gets the dynamic_dns_query of this RuntimeContainerCapabilities.  # noqa: E501

        DynamicDNSQuery indicates capped behavioral dns queries.   # noqa: E501

        :return: The dynamic_dns_query of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_dns_query

    @dynamic_dns_query.setter
    def dynamic_dns_query(self, dynamic_dns_query):
        """Sets the dynamic_dns_query of this RuntimeContainerCapabilities.

        DynamicDNSQuery indicates capped behavioral dns queries.   # noqa: E501

        :param dynamic_dns_query: The dynamic_dns_query of this RuntimeContainerCapabilities.  # noqa: E501
        :type dynamic_dns_query: bool
        """

        self._dynamic_dns_query = dynamic_dns_query

    @property
    def dynamic_file_creation(self):
        """Gets the dynamic_file_creation of this RuntimeContainerCapabilities.  # noqa: E501

        DynamicFileCreation indicates capped behavioral filesystem paths.   # noqa: E501

        :return: The dynamic_file_creation of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_file_creation

    @dynamic_file_creation.setter
    def dynamic_file_creation(self, dynamic_file_creation):
        """Sets the dynamic_file_creation of this RuntimeContainerCapabilities.

        DynamicFileCreation indicates capped behavioral filesystem paths.   # noqa: E501

        :param dynamic_file_creation: The dynamic_file_creation of this RuntimeContainerCapabilities.  # noqa: E501
        :type dynamic_file_creation: bool
        """

        self._dynamic_file_creation = dynamic_file_creation

    @property
    def dynamic_process_creation(self):
        """Gets the dynamic_process_creation of this RuntimeContainerCapabilities.  # noqa: E501

        DynamicProcessCreation indicates capped behavioral processes.   # noqa: E501

        :return: The dynamic_process_creation of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_process_creation

    @dynamic_process_creation.setter
    def dynamic_process_creation(self, dynamic_process_creation):
        """Sets the dynamic_process_creation of this RuntimeContainerCapabilities.

        DynamicProcessCreation indicates capped behavioral processes.   # noqa: E501

        :param dynamic_process_creation: The dynamic_process_creation of this RuntimeContainerCapabilities.  # noqa: E501
        :type dynamic_process_creation: bool
        """

        self._dynamic_process_creation = dynamic_process_creation

    @property
    def k8s(self):
        """Gets the k8s of this RuntimeContainerCapabilities.  # noqa: E501

        Kubernetes indicates the given container can perform k8s networking tasks (e.g., contact to api server).   # noqa: E501

        :return: The k8s of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._k8s

    @k8s.setter
    def k8s(self, k8s):
        """Sets the k8s of this RuntimeContainerCapabilities.

        Kubernetes indicates the given container can perform k8s networking tasks (e.g., contact to api server).   # noqa: E501

        :param k8s: The k8s of this RuntimeContainerCapabilities.  # noqa: E501
        :type k8s: bool
        """

        self._k8s = k8s

    @property
    def proxy(self):
        """Gets the proxy of this RuntimeContainerCapabilities.  # noqa: E501

        Proxy indicates the container can listen on any port and perform multiple outbound connection.   # noqa: E501

        :return: The proxy of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this RuntimeContainerCapabilities.

        Proxy indicates the container can listen on any port and perform multiple outbound connection.   # noqa: E501

        :param proxy: The proxy of this RuntimeContainerCapabilities.  # noqa: E501
        :type proxy: bool
        """

        self._proxy = proxy

    @property
    def sshd(self):
        """Gets the sshd of this RuntimeContainerCapabilities.  # noqa: E501

        Sshd indicates whether the container can run sshd process.   # noqa: E501

        :return: The sshd of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._sshd

    @sshd.setter
    def sshd(self, sshd):
        """Sets the sshd of this RuntimeContainerCapabilities.

        Sshd indicates whether the container can run sshd process.   # noqa: E501

        :param sshd: The sshd of this RuntimeContainerCapabilities.  # noqa: E501
        :type sshd: bool
        """

        self._sshd = sshd

    @property
    def unpacker(self):
        """Gets the unpacker of this RuntimeContainerCapabilities.  # noqa: E501

        Unpacker indicates the container is allowed to write shared libraries to disk.   # noqa: E501

        :return: The unpacker of this RuntimeContainerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._unpacker

    @unpacker.setter
    def unpacker(self, unpacker):
        """Sets the unpacker of this RuntimeContainerCapabilities.

        Unpacker indicates the container is allowed to write shared libraries to disk.   # noqa: E501

        :param unpacker: The unpacker of this RuntimeContainerCapabilities.  # noqa: E501
        :type unpacker: bool
        """

        self._unpacker = unpacker

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
        if not isinstance(other, RuntimeContainerCapabilities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeContainerCapabilities):
            return True

        return self.to_dict() != other.to_dict()
