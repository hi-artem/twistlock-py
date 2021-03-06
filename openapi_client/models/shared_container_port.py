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


class SharedContainerPort(object):
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
        'container': 'int',
        'host': 'int',
        'host_ip': 'str',
        'listening': 'bool',
        'nat': 'bool'
    }

    attribute_map = {
        'container': 'container',
        'host': 'host',
        'host_ip': 'hostIP',
        'listening': 'listening',
        'nat': 'nat'
    }

    def __init__(self, container=None, host=None, host_ip=None, listening=None, nat=None, local_vars_configuration=None):  # noqa: E501
        """SharedContainerPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._container = None
        self._host = None
        self._host_ip = None
        self._listening = None
        self._nat = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if host is not None:
            self.host = host
        if host_ip is not None:
            self.host_ip = host_ip
        if listening is not None:
            self.listening = listening
        if nat is not None:
            self.nat = nat

    @property
    def container(self):
        """Gets the container of this SharedContainerPort.  # noqa: E501

        Container is the mapped port inside the container.   # noqa: E501

        :return: The container of this SharedContainerPort.  # noqa: E501
        :rtype: int
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this SharedContainerPort.

        Container is the mapped port inside the container.   # noqa: E501

        :param container: The container of this SharedContainerPort.  # noqa: E501
        :type container: int
        """

        self._container = container

    @property
    def host(self):
        """Gets the host of this SharedContainerPort.  # noqa: E501

        Host is the host port number.   # noqa: E501

        :return: The host of this SharedContainerPort.  # noqa: E501
        :rtype: int
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SharedContainerPort.

        Host is the host port number.   # noqa: E501

        :param host: The host of this SharedContainerPort.  # noqa: E501
        :type host: int
        """

        self._host = host

    @property
    def host_ip(self):
        """Gets the host_ip of this SharedContainerPort.  # noqa: E501

        HostIP is the host IP.   # noqa: E501

        :return: The host_ip of this SharedContainerPort.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this SharedContainerPort.

        HostIP is the host IP.   # noqa: E501

        :param host_ip: The host_ip of this SharedContainerPort.  # noqa: E501
        :type host_ip: str
        """

        self._host_ip = host_ip

    @property
    def listening(self):
        """Gets the listening of this SharedContainerPort.  # noqa: E501

        Listening indicates whether the port is in listening mode.   # noqa: E501

        :return: The listening of this SharedContainerPort.  # noqa: E501
        :rtype: bool
        """
        return self._listening

    @listening.setter
    def listening(self, listening):
        """Sets the listening of this SharedContainerPort.

        Listening indicates whether the port is in listening mode.   # noqa: E501

        :param listening: The listening of this SharedContainerPort.  # noqa: E501
        :type listening: bool
        """

        self._listening = listening

    @property
    def nat(self):
        """Gets the nat of this SharedContainerPort.  # noqa: E501

        NAT indicates the port is exposed using NAT.   # noqa: E501

        :return: The nat of this SharedContainerPort.  # noqa: E501
        :rtype: bool
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        """Sets the nat of this SharedContainerPort.

        NAT indicates the port is exposed using NAT.   # noqa: E501

        :param nat: The nat of this SharedContainerPort.  # noqa: E501
        :type nat: bool
        """

        self._nat = nat

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
        if not isinstance(other, SharedContainerPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedContainerPort):
            return True

        return self.to_dict() != other.to_dict()
