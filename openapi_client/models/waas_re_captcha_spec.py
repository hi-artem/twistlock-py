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


class WaasReCAPTCHASpec(object):
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
        'all_sessions': 'bool',
        'enabled': 'bool',
        'secret_key': 'CommonSecret',
        'site_key': 'str',
        'success_expiration_hours': 'int',
        'type': 'WaasReCAPTCHAType'
    }

    attribute_map = {
        'all_sessions': 'allSessions',
        'enabled': 'enabled',
        'secret_key': 'secretKey',
        'site_key': 'siteKey',
        'success_expiration_hours': 'successExpirationHours',
        'type': 'type'
    }

    def __init__(self, all_sessions=None, enabled=None, secret_key=None, site_key=None, success_expiration_hours=None, type=None, local_vars_configuration=None):  # noqa: E501
        """WaasReCAPTCHASpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._all_sessions = None
        self._enabled = None
        self._secret_key = None
        self._site_key = None
        self._success_expiration_hours = None
        self._type = None
        self.discriminator = None

        if all_sessions is not None:
            self.all_sessions = all_sessions
        if enabled is not None:
            self.enabled = enabled
        if secret_key is not None:
            self.secret_key = secret_key
        if site_key is not None:
            self.site_key = site_key
        if success_expiration_hours is not None:
            self.success_expiration_hours = success_expiration_hours
        if type is not None:
            self.type = type

    @property
    def all_sessions(self):
        """Gets the all_sessions of this WaasReCAPTCHASpec.  # noqa: E501

        Indicates if the reCAPTCHA page is served at the start of every new session (true) or not (false).   # noqa: E501

        :return: The all_sessions of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: bool
        """
        return self._all_sessions

    @all_sessions.setter
    def all_sessions(self, all_sessions):
        """Sets the all_sessions of this WaasReCAPTCHASpec.

        Indicates if the reCAPTCHA page is served at the start of every new session (true) or not (false).   # noqa: E501

        :param all_sessions: The all_sessions of this WaasReCAPTCHASpec.  # noqa: E501
        :type all_sessions: bool
        """

        self._all_sessions = all_sessions

    @property
    def enabled(self):
        """Gets the enabled of this WaasReCAPTCHASpec.  # noqa: E501

        Indicates if reCAPTCHA integration is enabled (true) or not (false).   # noqa: E501

        :return: The enabled of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WaasReCAPTCHASpec.

        Indicates if reCAPTCHA integration is enabled (true) or not (false).   # noqa: E501

        :param enabled: The enabled of this WaasReCAPTCHASpec.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def secret_key(self):
        """Gets the secret_key of this WaasReCAPTCHASpec.  # noqa: E501


        :return: The secret_key of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this WaasReCAPTCHASpec.


        :param secret_key: The secret_key of this WaasReCAPTCHASpec.  # noqa: E501
        :type secret_key: CommonSecret
        """

        self._secret_key = secret_key

    @property
    def site_key(self):
        """Gets the site_key of this WaasReCAPTCHASpec.  # noqa: E501

        ReCAPTCHA site key to use when invoking the reCAPTCHA service.   # noqa: E501

        :return: The site_key of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: str
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this WaasReCAPTCHASpec.

        ReCAPTCHA site key to use when invoking the reCAPTCHA service.   # noqa: E501

        :param site_key: The site_key of this WaasReCAPTCHASpec.  # noqa: E501
        :type site_key: str
        """

        self._site_key = site_key

    @property
    def success_expiration_hours(self):
        """Gets the success_expiration_hours of this WaasReCAPTCHASpec.  # noqa: E501

        Duration for which the indication of reCAPTCHA success is kept. Maximum value is 30 days * 24 = 720 hours.   # noqa: E501

        :return: The success_expiration_hours of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: int
        """
        return self._success_expiration_hours

    @success_expiration_hours.setter
    def success_expiration_hours(self, success_expiration_hours):
        """Sets the success_expiration_hours of this WaasReCAPTCHASpec.

        Duration for which the indication of reCAPTCHA success is kept. Maximum value is 30 days * 24 = 720 hours.   # noqa: E501

        :param success_expiration_hours: The success_expiration_hours of this WaasReCAPTCHASpec.  # noqa: E501
        :type success_expiration_hours: int
        """

        self._success_expiration_hours = success_expiration_hours

    @property
    def type(self):
        """Gets the type of this WaasReCAPTCHASpec.  # noqa: E501


        :return: The type of this WaasReCAPTCHASpec.  # noqa: E501
        :rtype: WaasReCAPTCHAType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WaasReCAPTCHASpec.


        :param type: The type of this WaasReCAPTCHASpec.  # noqa: E501
        :type type: WaasReCAPTCHAType
        """

        self._type = type

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
        if not isinstance(other, WaasReCAPTCHASpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaasReCAPTCHASpec):
            return True

        return self.to_dict() != other.to_dict()
