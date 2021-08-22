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


class RuntimeHostProfileOutgoingPort(object):
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
        'command': 'str',
        'country': 'str',
        'ip': 'str',
        'modified': 'datetime',
        'port': 'int',
        'process_path': 'str'
    }

    attribute_map = {
        'command': 'command',
        'country': 'country',
        'ip': 'ip',
        'modified': 'modified',
        'port': 'port',
        'process_path': 'processPath'
    }

    def __init__(self, command=None, country=None, ip=None, modified=None, port=None, process_path=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeHostProfileOutgoingPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._command = None
        self._country = None
        self._ip = None
        self._modified = None
        self._port = None
        self._process_path = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if country is not None:
            self.country = country
        if ip is not None:
            self.ip = ip
        if modified is not None:
            self.modified = modified
        if port is not None:
            self.port = port
        if process_path is not None:
            self.process_path = process_path

    @property
    def command(self):
        """Gets the command of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        Command represents the command that triggered the connection.   # noqa: E501

        :return: The command of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this RuntimeHostProfileOutgoingPort.

        Command represents the command that triggered the connection.   # noqa: E501

        :param command: The command of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def country(self):
        """Gets the country of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        Country is the country ISO code for the given IP address.   # noqa: E501

        :return: The country of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this RuntimeHostProfileOutgoingPort.

        Country is the country ISO code for the given IP address.   # noqa: E501

        :param country: The country of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def ip(self):
        """Gets the ip of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        IP is the IP address captured over this port.   # noqa: E501

        :return: The ip of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this RuntimeHostProfileOutgoingPort.

        IP is the IP address captured over this port.   # noqa: E501

        :param ip: The ip of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type ip: str
        """

        self._ip = ip

    @property
    def modified(self):
        """Gets the modified of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        Modified is a timestamp of when the event occurred.   # noqa: E501

        :return: The modified of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this RuntimeHostProfileOutgoingPort.

        Modified is a timestamp of when the event occurred.   # noqa: E501

        :param modified: The modified of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def port(self):
        """Gets the port of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        Port is the port number.   # noqa: E501

        :return: The port of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RuntimeHostProfileOutgoingPort.

        Port is the port number.   # noqa: E501

        :param port: The port of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type port: int
        """

        self._port = port

    @property
    def process_path(self):
        """Gets the process_path of this RuntimeHostProfileOutgoingPort.  # noqa: E501

        ProcessPath represents the path to the process that uses the port.   # noqa: E501

        :return: The process_path of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        """Sets the process_path of this RuntimeHostProfileOutgoingPort.

        ProcessPath represents the path to the process that uses the port.   # noqa: E501

        :param process_path: The process_path of this RuntimeHostProfileOutgoingPort.  # noqa: E501
        :type process_path: str
        """

        self._process_path = process_path

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
        if not isinstance(other, RuntimeHostProfileOutgoingPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeHostProfileOutgoingPort):
            return True

        return self.to_dict() != other.to_dict()
