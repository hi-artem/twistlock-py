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


class ServerlessTriggers(object):
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
        'service': 'str',
        'triggers': 'list[ServerlessTrigger]'
    }

    attribute_map = {
        'service': 'service',
        'triggers': 'triggers'
    }

    def __init__(self, service=None, triggers=None, local_vars_configuration=None):  # noqa: E501
        """ServerlessTriggers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._service = None
        self._triggers = None
        self.discriminator = None

        if service is not None:
            self.service = service
        if triggers is not None:
            self.triggers = triggers

    @property
    def service(self):
        """Gets the service of this ServerlessTriggers.  # noqa: E501

        Service is the service name.   # noqa: E501

        :return: The service of this ServerlessTriggers.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ServerlessTriggers.

        Service is the service name.   # noqa: E501

        :param service: The service of this ServerlessTriggers.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def triggers(self):
        """Gets the triggers of this ServerlessTriggers.  # noqa: E501

        Triggers are the function invocation paths from the service.   # noqa: E501

        :return: The triggers of this ServerlessTriggers.  # noqa: E501
        :rtype: list[ServerlessTrigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ServerlessTriggers.

        Triggers are the function invocation paths from the service.   # noqa: E501

        :param triggers: The triggers of this ServerlessTriggers.  # noqa: E501
        :type triggers: list[ServerlessTrigger]
        """

        self._triggers = triggers

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
        if not isinstance(other, ServerlessTriggers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerlessTriggers):
            return True

        return self.to_dict() != other.to_dict()