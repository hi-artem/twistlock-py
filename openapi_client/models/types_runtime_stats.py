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


class TypesRuntimeStats(object):
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
        'filesystem': 'int',
        'kubernetes': 'int',
        'network': 'int',
        'processes': 'int'
    }

    attribute_map = {
        'filesystem': 'filesystem',
        'kubernetes': 'kubernetes',
        'network': 'network',
        'processes': 'processes'
    }

    def __init__(self, filesystem=None, kubernetes=None, network=None, processes=None, local_vars_configuration=None):  # noqa: E501
        """TypesRuntimeStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filesystem = None
        self._kubernetes = None
        self._network = None
        self._processes = None
        self.discriminator = None

        if filesystem is not None:
            self.filesystem = filesystem
        if kubernetes is not None:
            self.kubernetes = kubernetes
        if network is not None:
            self.network = network
        if processes is not None:
            self.processes = processes

    @property
    def filesystem(self):
        """Gets the filesystem of this TypesRuntimeStats.  # noqa: E501

        .   # noqa: E501

        :return: The filesystem of this TypesRuntimeStats.  # noqa: E501
        :rtype: int
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this TypesRuntimeStats.

        .   # noqa: E501

        :param filesystem: The filesystem of this TypesRuntimeStats.  # noqa: E501
        :type filesystem: int
        """

        self._filesystem = filesystem

    @property
    def kubernetes(self):
        """Gets the kubernetes of this TypesRuntimeStats.  # noqa: E501

        .   # noqa: E501

        :return: The kubernetes of this TypesRuntimeStats.  # noqa: E501
        :rtype: int
        """
        return self._kubernetes

    @kubernetes.setter
    def kubernetes(self, kubernetes):
        """Sets the kubernetes of this TypesRuntimeStats.

        .   # noqa: E501

        :param kubernetes: The kubernetes of this TypesRuntimeStats.  # noqa: E501
        :type kubernetes: int
        """

        self._kubernetes = kubernetes

    @property
    def network(self):
        """Gets the network of this TypesRuntimeStats.  # noqa: E501

        .   # noqa: E501

        :return: The network of this TypesRuntimeStats.  # noqa: E501
        :rtype: int
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this TypesRuntimeStats.

        .   # noqa: E501

        :param network: The network of this TypesRuntimeStats.  # noqa: E501
        :type network: int
        """

        self._network = network

    @property
    def processes(self):
        """Gets the processes of this TypesRuntimeStats.  # noqa: E501

        .   # noqa: E501

        :return: The processes of this TypesRuntimeStats.  # noqa: E501
        :rtype: int
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this TypesRuntimeStats.

        .   # noqa: E501

        :param processes: The processes of this TypesRuntimeStats.  # noqa: E501
        :type processes: int
        """

        self._processes = processes

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
        if not isinstance(other, TypesRuntimeStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesRuntimeStats):
            return True

        return self.to_dict() != other.to_dict()
