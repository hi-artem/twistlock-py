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


class DefenderSettings(object):
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
        'admission_control_enabled': 'bool',
        'admission_control_webhook_suffix': 'str',
        'automatic_upgrade': 'bool',
        'disconnect_period_days': 'int',
        'host_custom_compliance_enabled': 'bool',
        'listening_port': 'int'
    }

    attribute_map = {
        'admission_control_enabled': 'admissionControlEnabled',
        'admission_control_webhook_suffix': 'admissionControlWebhookSuffix',
        'automatic_upgrade': 'automaticUpgrade',
        'disconnect_period_days': 'disconnectPeriodDays',
        'host_custom_compliance_enabled': 'hostCustomComplianceEnabled',
        'listening_port': 'listeningPort'
    }

    def __init__(self, admission_control_enabled=None, admission_control_webhook_suffix=None, automatic_upgrade=None, disconnect_period_days=None, host_custom_compliance_enabled=None, listening_port=None, local_vars_configuration=None):  # noqa: E501
        """DefenderSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._admission_control_enabled = None
        self._admission_control_webhook_suffix = None
        self._automatic_upgrade = None
        self._disconnect_period_days = None
        self._host_custom_compliance_enabled = None
        self._listening_port = None
        self.discriminator = None

        if admission_control_enabled is not None:
            self.admission_control_enabled = admission_control_enabled
        if admission_control_webhook_suffix is not None:
            self.admission_control_webhook_suffix = admission_control_webhook_suffix
        if automatic_upgrade is not None:
            self.automatic_upgrade = automatic_upgrade
        if disconnect_period_days is not None:
            self.disconnect_period_days = disconnect_period_days
        if host_custom_compliance_enabled is not None:
            self.host_custom_compliance_enabled = host_custom_compliance_enabled
        if listening_port is not None:
            self.listening_port = listening_port

    @property
    def admission_control_enabled(self):
        """Gets the admission_control_enabled of this DefenderSettings.  # noqa: E501

        Indicates if the admission controller is enabled (true) or not (false).   # noqa: E501

        :return: The admission_control_enabled of this DefenderSettings.  # noqa: E501
        :rtype: bool
        """
        return self._admission_control_enabled

    @admission_control_enabled.setter
    def admission_control_enabled(self, admission_control_enabled):
        """Sets the admission_control_enabled of this DefenderSettings.

        Indicates if the admission controller is enabled (true) or not (false).   # noqa: E501

        :param admission_control_enabled: The admission_control_enabled of this DefenderSettings.  # noqa: E501
        :type admission_control_enabled: bool
        """

        self._admission_control_enabled = admission_control_enabled

    @property
    def admission_control_webhook_suffix(self):
        """Gets the admission_control_webhook_suffix of this DefenderSettings.  # noqa: E501

        Relative path to the admission control webhook HTTP endpoint.   # noqa: E501

        :return: The admission_control_webhook_suffix of this DefenderSettings.  # noqa: E501
        :rtype: str
        """
        return self._admission_control_webhook_suffix

    @admission_control_webhook_suffix.setter
    def admission_control_webhook_suffix(self, admission_control_webhook_suffix):
        """Sets the admission_control_webhook_suffix of this DefenderSettings.

        Relative path to the admission control webhook HTTP endpoint.   # noqa: E501

        :param admission_control_webhook_suffix: The admission_control_webhook_suffix of this DefenderSettings.  # noqa: E501
        :type admission_control_webhook_suffix: str
        """

        self._admission_control_webhook_suffix = admission_control_webhook_suffix

    @property
    def automatic_upgrade(self):
        """Gets the automatic_upgrade of this DefenderSettings.  # noqa: E501

        Indicates if Defenders should be automatically upgraded to the latest version (true) or not (false).   # noqa: E501

        :return: The automatic_upgrade of this DefenderSettings.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_upgrade

    @automatic_upgrade.setter
    def automatic_upgrade(self, automatic_upgrade):
        """Sets the automatic_upgrade of this DefenderSettings.

        Indicates if Defenders should be automatically upgraded to the latest version (true) or not (false).   # noqa: E501

        :param automatic_upgrade: The automatic_upgrade of this DefenderSettings.  # noqa: E501
        :type automatic_upgrade: bool
        """

        self._automatic_upgrade = automatic_upgrade

    @property
    def disconnect_period_days(self):
        """Gets the disconnect_period_days of this DefenderSettings.  # noqa: E501

        Number of consecutive days a Defender must remain disconnected for it to be considered decommissioned.   # noqa: E501

        :return: The disconnect_period_days of this DefenderSettings.  # noqa: E501
        :rtype: int
        """
        return self._disconnect_period_days

    @disconnect_period_days.setter
    def disconnect_period_days(self, disconnect_period_days):
        """Sets the disconnect_period_days of this DefenderSettings.

        Number of consecutive days a Defender must remain disconnected for it to be considered decommissioned.   # noqa: E501

        :param disconnect_period_days: The disconnect_period_days of this DefenderSettings.  # noqa: E501
        :type disconnect_period_days: int
        """

        self._disconnect_period_days = disconnect_period_days

    @property
    def host_custom_compliance_enabled(self):
        """Gets the host_custom_compliance_enabled of this DefenderSettings.  # noqa: E501

        Indicates if Defenders support host custom compliance checks (true) or not (false).   # noqa: E501

        :return: The host_custom_compliance_enabled of this DefenderSettings.  # noqa: E501
        :rtype: bool
        """
        return self._host_custom_compliance_enabled

    @host_custom_compliance_enabled.setter
    def host_custom_compliance_enabled(self, host_custom_compliance_enabled):
        """Sets the host_custom_compliance_enabled of this DefenderSettings.

        Indicates if Defenders support host custom compliance checks (true) or not (false).   # noqa: E501

        :param host_custom_compliance_enabled: The host_custom_compliance_enabled of this DefenderSettings.  # noqa: E501
        :type host_custom_compliance_enabled: bool
        """

        self._host_custom_compliance_enabled = host_custom_compliance_enabled

    @property
    def listening_port(self):
        """Gets the listening_port of this DefenderSettings.  # noqa: E501

        Port on which Defenders listen.   # noqa: E501

        :return: The listening_port of this DefenderSettings.  # noqa: E501
        :rtype: int
        """
        return self._listening_port

    @listening_port.setter
    def listening_port(self, listening_port):
        """Sets the listening_port of this DefenderSettings.

        Port on which Defenders listen.   # noqa: E501

        :param listening_port: The listening_port of this DefenderSettings.  # noqa: E501
        :type listening_port: int
        """

        self._listening_port = listening_port

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
        if not isinstance(other, DefenderSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefenderSettings):
            return True

        return self.to_dict() != other.to_dict()