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


class TypesLogonSettings(object):
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
        'basic_auth_disabled': 'bool',
        'include_tls': 'bool',
        'session_timeout_sec': 'int',
        'strong_password': 'bool',
        'use_support_credentials': 'bool'
    }

    attribute_map = {
        'basic_auth_disabled': 'basicAuthDisabled',
        'include_tls': 'includeTLS',
        'session_timeout_sec': 'sessionTimeoutSec',
        'strong_password': 'strongPassword',
        'use_support_credentials': 'useSupportCredentials'
    }

    def __init__(self, basic_auth_disabled=None, include_tls=None, session_timeout_sec=None, strong_password=None, use_support_credentials=None, local_vars_configuration=None):  # noqa: E501
        """TypesLogonSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._basic_auth_disabled = None
        self._include_tls = None
        self._session_timeout_sec = None
        self._strong_password = None
        self._use_support_credentials = None
        self.discriminator = None

        if basic_auth_disabled is not None:
            self.basic_auth_disabled = basic_auth_disabled
        if include_tls is not None:
            self.include_tls = include_tls
        if session_timeout_sec is not None:
            self.session_timeout_sec = session_timeout_sec
        if strong_password is not None:
            self.strong_password = strong_password
        if use_support_credentials is not None:
            self.use_support_credentials = use_support_credentials

    @property
    def basic_auth_disabled(self):
        """Gets the basic_auth_disabled of this TypesLogonSettings.  # noqa: E501

        Indicates whether the user can use basic auth.   # noqa: E501

        :return: The basic_auth_disabled of this TypesLogonSettings.  # noqa: E501
        :rtype: bool
        """
        return self._basic_auth_disabled

    @basic_auth_disabled.setter
    def basic_auth_disabled(self, basic_auth_disabled):
        """Sets the basic_auth_disabled of this TypesLogonSettings.

        Indicates whether the user can use basic auth.   # noqa: E501

        :param basic_auth_disabled: The basic_auth_disabled of this TypesLogonSettings.  # noqa: E501
        :type basic_auth_disabled: bool
        """

        self._basic_auth_disabled = basic_auth_disabled

    @property
    def include_tls(self):
        """Gets the include_tls of this TypesLogonSettings.  # noqa: E501

        IncludeTLS indicates that TLS checks should be included in copy links.   # noqa: E501

        :return: The include_tls of this TypesLogonSettings.  # noqa: E501
        :rtype: bool
        """
        return self._include_tls

    @include_tls.setter
    def include_tls(self, include_tls):
        """Sets the include_tls of this TypesLogonSettings.

        IncludeTLS indicates that TLS checks should be included in copy links.   # noqa: E501

        :param include_tls: The include_tls of this TypesLogonSettings.  # noqa: E501
        :type include_tls: bool
        """

        self._include_tls = include_tls

    @property
    def session_timeout_sec(self):
        """Gets the session_timeout_sec of this TypesLogonSettings.  # noqa: E501

        SessionTimeoutSec defines the session timeout in seconds.   # noqa: E501

        :return: The session_timeout_sec of this TypesLogonSettings.  # noqa: E501
        :rtype: int
        """
        return self._session_timeout_sec

    @session_timeout_sec.setter
    def session_timeout_sec(self, session_timeout_sec):
        """Sets the session_timeout_sec of this TypesLogonSettings.

        SessionTimeoutSec defines the session timeout in seconds.   # noqa: E501

        :param session_timeout_sec: The session_timeout_sec of this TypesLogonSettings.  # noqa: E501
        :type session_timeout_sec: int
        """

        self._session_timeout_sec = session_timeout_sec

    @property
    def strong_password(self):
        """Gets the strong_password of this TypesLogonSettings.  # noqa: E501

        StrongPassword indicates whether strong password enforcement is applied.   # noqa: E501

        :return: The strong_password of this TypesLogonSettings.  # noqa: E501
        :rtype: bool
        """
        return self._strong_password

    @strong_password.setter
    def strong_password(self, strong_password):
        """Sets the strong_password of this TypesLogonSettings.

        StrongPassword indicates whether strong password enforcement is applied.   # noqa: E501

        :param strong_password: The strong_password of this TypesLogonSettings.  # noqa: E501
        :type strong_password: bool
        """

        self._strong_password = strong_password

    @property
    def use_support_credentials(self):
        """Gets the use_support_credentials of this TypesLogonSettings.  # noqa: E501

        UseSupportCredentials indicates whether to include credentials in the URL.   # noqa: E501

        :return: The use_support_credentials of this TypesLogonSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_support_credentials

    @use_support_credentials.setter
    def use_support_credentials(self, use_support_credentials):
        """Sets the use_support_credentials of this TypesLogonSettings.

        UseSupportCredentials indicates whether to include credentials in the URL.   # noqa: E501

        :param use_support_credentials: The use_support_credentials of this TypesLogonSettings.  # noqa: E501
        :type use_support_credentials: bool
        """

        self._use_support_credentials = use_support_credentials

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
        if not isinstance(other, TypesLogonSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesLogonSettings):
            return True

        return self.to_dict() != other.to_dict()
