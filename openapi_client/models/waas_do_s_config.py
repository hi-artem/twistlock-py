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


class WaasDoSConfig(object):
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
        'alert': 'WaasDoSRates',
        'ban': 'WaasDoSRates',
        'enabled': 'bool',
        'excluded_network_lists': 'list[str]',
        'match_conditions': 'list[WaasDoSMatchCondition]',
        'track_session': 'bool'
    }

    attribute_map = {
        'alert': 'alert',
        'ban': 'ban',
        'enabled': 'enabled',
        'excluded_network_lists': 'excludedNetworkLists',
        'match_conditions': 'matchConditions',
        'track_session': 'trackSession'
    }

    def __init__(self, alert=None, ban=None, enabled=None, excluded_network_lists=None, match_conditions=None, track_session=None, local_vars_configuration=None):  # noqa: E501
        """WaasDoSConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._alert = None
        self._ban = None
        self._enabled = None
        self._excluded_network_lists = None
        self._match_conditions = None
        self._track_session = None
        self.discriminator = None

        if alert is not None:
            self.alert = alert
        if ban is not None:
            self.ban = ban
        if enabled is not None:
            self.enabled = enabled
        if excluded_network_lists is not None:
            self.excluded_network_lists = excluded_network_lists
        if match_conditions is not None:
            self.match_conditions = match_conditions
        if track_session is not None:
            self.track_session = track_session

    @property
    def alert(self):
        """Gets the alert of this WaasDoSConfig.  # noqa: E501


        :return: The alert of this WaasDoSConfig.  # noqa: E501
        :rtype: WaasDoSRates
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this WaasDoSConfig.


        :param alert: The alert of this WaasDoSConfig.  # noqa: E501
        :type alert: WaasDoSRates
        """

        self._alert = alert

    @property
    def ban(self):
        """Gets the ban of this WaasDoSConfig.  # noqa: E501


        :return: The ban of this WaasDoSConfig.  # noqa: E501
        :rtype: WaasDoSRates
        """
        return self._ban

    @ban.setter
    def ban(self, ban):
        """Sets the ban of this WaasDoSConfig.


        :param ban: The ban of this WaasDoSConfig.  # noqa: E501
        :type ban: WaasDoSRates
        """

        self._ban = ban

    @property
    def enabled(self):
        """Gets the enabled of this WaasDoSConfig.  # noqa: E501

        Enabled indicates if dos protection is enabled.   # noqa: E501

        :return: The enabled of this WaasDoSConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WaasDoSConfig.

        Enabled indicates if dos protection is enabled.   # noqa: E501

        :param enabled: The enabled of this WaasDoSConfig.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def excluded_network_lists(self):
        """Gets the excluded_network_lists of this WaasDoSConfig.  # noqa: E501

        Network IPs to exclude from DoS tracking.   # noqa: E501

        :return: The excluded_network_lists of this WaasDoSConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_network_lists

    @excluded_network_lists.setter
    def excluded_network_lists(self, excluded_network_lists):
        """Sets the excluded_network_lists of this WaasDoSConfig.

        Network IPs to exclude from DoS tracking.   # noqa: E501

        :param excluded_network_lists: The excluded_network_lists of this WaasDoSConfig.  # noqa: E501
        :type excluded_network_lists: list[str]
        """

        self._excluded_network_lists = excluded_network_lists

    @property
    def match_conditions(self):
        """Gets the match_conditions of this WaasDoSConfig.  # noqa: E501

        Conditions on which to match to track a request. The conditions are \\\"OR\\\"'d together during the check.   # noqa: E501

        :return: The match_conditions of this WaasDoSConfig.  # noqa: E501
        :rtype: list[WaasDoSMatchCondition]
        """
        return self._match_conditions

    @match_conditions.setter
    def match_conditions(self, match_conditions):
        """Sets the match_conditions of this WaasDoSConfig.

        Conditions on which to match to track a request. The conditions are \\\"OR\\\"'d together during the check.   # noqa: E501

        :param match_conditions: The match_conditions of this WaasDoSConfig.  # noqa: E501
        :type match_conditions: list[WaasDoSMatchCondition]
        """

        self._match_conditions = match_conditions

    @property
    def track_session(self):
        """Gets the track_session of this WaasDoSConfig.  # noqa: E501

        Indicates if the custom session ID generated during bot protection flow is tracked (true) or not (false).   # noqa: E501

        :return: The track_session of this WaasDoSConfig.  # noqa: E501
        :rtype: bool
        """
        return self._track_session

    @track_session.setter
    def track_session(self, track_session):
        """Sets the track_session of this WaasDoSConfig.

        Indicates if the custom session ID generated during bot protection flow is tracked (true) or not (false).   # noqa: E501

        :param track_session: The track_session of this WaasDoSConfig.  # noqa: E501
        :type track_session: bool
        """

        self._track_session = track_session

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
        if not isinstance(other, WaasDoSConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaasDoSConfig):
            return True

        return self.to_dict() != other.to_dict()
