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


class SharedPort(object):
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
        'container_port': 'str',
        'host_ip': 'str',
        'host_port': 'int'
    }

    attribute_map = {
        'container_port': 'containerPort',
        'host_ip': 'hostIP',
        'host_port': 'hostPort'
    }

    def __init__(self, container_port=None, host_ip=None, host_port=None, local_vars_configuration=None):  # noqa: E501
        """SharedPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._container_port = None
        self._host_ip = None
        self._host_port = None
        self.discriminator = None

        if container_port is not None:
            self.container_port = container_port
        if host_ip is not None:
            self.host_ip = host_ip
        if host_port is not None:
            self.host_port = host_port

    @property
    def container_port(self):
        """Gets the container_port of this SharedPort.  # noqa: E501

        ContainerPort is the mapped port inside the container.   # noqa: E501

        :return: The container_port of this SharedPort.  # noqa: E501
        :rtype: str
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """Sets the container_port of this SharedPort.

        ContainerPort is the mapped port inside the container.   # noqa: E501

        :param container_port: The container_port of this SharedPort.  # noqa: E501
        :type container_port: str
        """

        self._container_port = container_port

    @property
    def host_ip(self):
        """Gets the host_ip of this SharedPort.  # noqa: E501

        HostIP is the host IP.   # noqa: E501

        :return: The host_ip of this SharedPort.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this SharedPort.

        HostIP is the host IP.   # noqa: E501

        :param host_ip: The host_ip of this SharedPort.  # noqa: E501
        :type host_ip: str
        """

        self._host_ip = host_ip

    @property
    def host_port(self):
        """Gets the host_port of this SharedPort.  # noqa: E501

        HostPort is the host port.   # noqa: E501

        :return: The host_port of this SharedPort.  # noqa: E501
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """Sets the host_port of this SharedPort.

        HostPort is the host port.   # noqa: E501

        :param host_port: The host_port of this SharedPort.  # noqa: E501
        :type host_port: int
        """

        self._host_port = host_port

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
        if not isinstance(other, SharedPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedPort):
            return True

        return self.to_dict() != other.to_dict()