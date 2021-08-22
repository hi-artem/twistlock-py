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


class RuntimeApp(object):
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
        'listening_ports': 'list[RuntimeHostProfileListeningPort]',
        'name': 'str',
        'outgoing_ports': 'list[RuntimeHostProfileOutgoingPort]',
        'processes': 'list[RuntimeProfileProcess]',
        'startup_process': 'RuntimeProfileProcess'
    }

    attribute_map = {
        'listening_ports': 'listeningPorts',
        'name': 'name',
        'outgoing_ports': 'outgoingPorts',
        'processes': 'processes',
        'startup_process': 'startupProcess'
    }

    def __init__(self, listening_ports=None, name=None, outgoing_ports=None, processes=None, startup_process=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._listening_ports = None
        self._name = None
        self._outgoing_ports = None
        self._processes = None
        self._startup_process = None
        self.discriminator = None

        if listening_ports is not None:
            self.listening_ports = listening_ports
        if name is not None:
            self.name = name
        if outgoing_ports is not None:
            self.outgoing_ports = outgoing_ports
        if processes is not None:
            self.processes = processes
        if startup_process is not None:
            self.startup_process = startup_process

    @property
    def listening_ports(self):
        """Gets the listening_ports of this RuntimeApp.  # noqa: E501

        ListeningPorts represents the applications listening ports.   # noqa: E501

        :return: The listening_ports of this RuntimeApp.  # noqa: E501
        :rtype: list[RuntimeHostProfileListeningPort]
        """
        return self._listening_ports

    @listening_ports.setter
    def listening_ports(self, listening_ports):
        """Sets the listening_ports of this RuntimeApp.

        ListeningPorts represents the applications listening ports.   # noqa: E501

        :param listening_ports: The listening_ports of this RuntimeApp.  # noqa: E501
        :type listening_ports: list[RuntimeHostProfileListeningPort]
        """

        self._listening_ports = listening_ports

    @property
    def name(self):
        """Gets the name of this RuntimeApp.  # noqa: E501

        Name is the app name.   # noqa: E501

        :return: The name of this RuntimeApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuntimeApp.

        Name is the app name.   # noqa: E501

        :param name: The name of this RuntimeApp.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def outgoing_ports(self):
        """Gets the outgoing_ports of this RuntimeApp.  # noqa: E501

        OutgoingPorts represents the applications outgoing ports.   # noqa: E501

        :return: The outgoing_ports of this RuntimeApp.  # noqa: E501
        :rtype: list[RuntimeHostProfileOutgoingPort]
        """
        return self._outgoing_ports

    @outgoing_ports.setter
    def outgoing_ports(self, outgoing_ports):
        """Sets the outgoing_ports of this RuntimeApp.

        OutgoingPorts represents the applications outgoing ports.   # noqa: E501

        :param outgoing_ports: The outgoing_ports of this RuntimeApp.  # noqa: E501
        :type outgoing_ports: list[RuntimeHostProfileOutgoingPort]
        """

        self._outgoing_ports = outgoing_ports

    @property
    def processes(self):
        """Gets the processes of this RuntimeApp.  # noqa: E501

        Processes is a list of the app's descendant processes.   # noqa: E501

        :return: The processes of this RuntimeApp.  # noqa: E501
        :rtype: list[RuntimeProfileProcess]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this RuntimeApp.

        Processes is a list of the app's descendant processes.   # noqa: E501

        :param processes: The processes of this RuntimeApp.  # noqa: E501
        :type processes: list[RuntimeProfileProcess]
        """

        self._processes = processes

    @property
    def startup_process(self):
        """Gets the startup_process of this RuntimeApp.  # noqa: E501


        :return: The startup_process of this RuntimeApp.  # noqa: E501
        :rtype: RuntimeProfileProcess
        """
        return self._startup_process

    @startup_process.setter
    def startup_process(self, startup_process):
        """Sets the startup_process of this RuntimeApp.


        :param startup_process: The startup_process of this RuntimeApp.  # noqa: E501
        :type startup_process: RuntimeProfileProcess
        """

        self._startup_process = startup_process

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
        if not isinstance(other, RuntimeApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeApp):
            return True

        return self.to_dict() != other.to_dict()