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


class IdentityLdapSettings(object):
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
        'account_password': 'CommonSecret',
        'account_upn': 'str',
        'ca_cert': 'str',
        'enabled': 'bool',
        'group_search_base': 'str',
        'search_base': 'str',
        'type': 'str',
        'url': 'str',
        'user_search_base': 'str',
        'user_search_identifier': 'str'
    }

    attribute_map = {
        'account_password': 'accountPassword',
        'account_upn': 'accountUpn',
        'ca_cert': 'caCert',
        'enabled': 'enabled',
        'group_search_base': 'groupSearchBase',
        'search_base': 'searchBase',
        'type': 'type',
        'url': 'url',
        'user_search_base': 'userSearchBase',
        'user_search_identifier': 'userSearchIdentifier'
    }

    def __init__(self, account_password=None, account_upn=None, ca_cert=None, enabled=None, group_search_base=None, search_base=None, type=None, url=None, user_search_base=None, user_search_identifier=None, local_vars_configuration=None):  # noqa: E501
        """IdentityLdapSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_password = None
        self._account_upn = None
        self._ca_cert = None
        self._enabled = None
        self._group_search_base = None
        self._search_base = None
        self._type = None
        self._url = None
        self._user_search_base = None
        self._user_search_identifier = None
        self.discriminator = None

        if account_password is not None:
            self.account_password = account_password
        if account_upn is not None:
            self.account_upn = account_upn
        if ca_cert is not None:
            self.ca_cert = ca_cert
        if enabled is not None:
            self.enabled = enabled
        if group_search_base is not None:
            self.group_search_base = group_search_base
        if search_base is not None:
            self.search_base = search_base
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if user_search_base is not None:
            self.user_search_base = user_search_base
        if user_search_identifier is not None:
            self.user_search_identifier = user_search_identifier

    @property
    def account_password(self):
        """Gets the account_password of this IdentityLdapSettings.  # noqa: E501


        :return: The account_password of this IdentityLdapSettings.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._account_password

    @account_password.setter
    def account_password(self, account_password):
        """Sets the account_password of this IdentityLdapSettings.


        :param account_password: The account_password of this IdentityLdapSettings.  # noqa: E501
        :type account_password: CommonSecret
        """

        self._account_password = account_password

    @property
    def account_upn(self):
        """Gets the account_upn of this IdentityLdapSettings.  # noqa: E501

        AccountUpn is the user principle name used to connect to the active directory server.   # noqa: E501

        :return: The account_upn of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._account_upn

    @account_upn.setter
    def account_upn(self, account_upn):
        """Sets the account_upn of this IdentityLdapSettings.

        AccountUpn is the user principle name used to connect to the active directory server.   # noqa: E501

        :param account_upn: The account_upn of this IdentityLdapSettings.  # noqa: E501
        :type account_upn: str
        """

        self._account_upn = account_upn

    @property
    def ca_cert(self):
        """Gets the ca_cert of this IdentityLdapSettings.  # noqa: E501

        CaCert is cert in PEM format (optional, if not specified, skip_verify flag will be used).   # noqa: E501

        :return: The ca_cert of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this IdentityLdapSettings.

        CaCert is cert in PEM format (optional, if not specified, skip_verify flag will be used).   # noqa: E501

        :param ca_cert: The ca_cert of this IdentityLdapSettings.  # noqa: E501
        :type ca_cert: str
        """

        self._ca_cert = ca_cert

    @property
    def enabled(self):
        """Gets the enabled of this IdentityLdapSettings.  # noqa: E501

        Enabled indicates whether LDAP is enabled.   # noqa: E501

        :return: The enabled of this IdentityLdapSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityLdapSettings.

        Enabled indicates whether LDAP is enabled.   # noqa: E501

        :param enabled: The enabled of this IdentityLdapSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def group_search_base(self):
        """Gets the group_search_base of this IdentityLdapSettings.  # noqa: E501

        GroupSearchBase is the LDAP search pattern for groups.   # noqa: E501

        :return: The group_search_base of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._group_search_base

    @group_search_base.setter
    def group_search_base(self, group_search_base):
        """Sets the group_search_base of this IdentityLdapSettings.

        GroupSearchBase is the LDAP search pattern for groups.   # noqa: E501

        :param group_search_base: The group_search_base of this IdentityLdapSettings.  # noqa: E501
        :type group_search_base: str
        """

        self._group_search_base = group_search_base

    @property
    def search_base(self):
        """Gets the search_base of this IdentityLdapSettings.  # noqa: E501

        SearchBase is the LDAP search pattern.   # noqa: E501

        :return: The search_base of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._search_base

    @search_base.setter
    def search_base(self, search_base):
        """Sets the search_base of this IdentityLdapSettings.

        SearchBase is the LDAP search pattern.   # noqa: E501

        :param search_base: The search_base of this IdentityLdapSettings.  # noqa: E501
        :type search_base: str
        """

        self._search_base = search_base

    @property
    def type(self):
        """Gets the type of this IdentityLdapSettings.  # noqa: E501

        Type specifies the LDAP server type (AD or OpenLDAP).   # noqa: E501

        :return: The type of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityLdapSettings.

        Type specifies the LDAP server type (AD or OpenLDAP).   # noqa: E501

        :param type: The type of this IdentityLdapSettings.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this IdentityLdapSettings.  # noqa: E501

        Url is the ldap server url.   # noqa: E501

        :return: The url of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdentityLdapSettings.

        Url is the ldap server url.   # noqa: E501

        :param url: The url of this IdentityLdapSettings.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def user_search_base(self):
        """Gets the user_search_base of this IdentityLdapSettings.  # noqa: E501

        UserSearchBase is the LDAP search pattern for users.   # noqa: E501

        :return: The user_search_base of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._user_search_base

    @user_search_base.setter
    def user_search_base(self, user_search_base):
        """Sets the user_search_base of this IdentityLdapSettings.

        UserSearchBase is the LDAP search pattern for users.   # noqa: E501

        :param user_search_base: The user_search_base of this IdentityLdapSettings.  # noqa: E501
        :type user_search_base: str
        """

        self._user_search_base = user_search_base

    @property
    def user_search_identifier(self):
        """Gets the user_search_identifier of this IdentityLdapSettings.  # noqa: E501

        UserSearchIdentifier is the user identifier to use for querying open ldap (e.g., cn -> cn=user).   # noqa: E501

        :return: The user_search_identifier of this IdentityLdapSettings.  # noqa: E501
        :rtype: str
        """
        return self._user_search_identifier

    @user_search_identifier.setter
    def user_search_identifier(self, user_search_identifier):
        """Sets the user_search_identifier of this IdentityLdapSettings.

        UserSearchIdentifier is the user identifier to use for querying open ldap (e.g., cn -> cn=user).   # noqa: E501

        :param user_search_identifier: The user_search_identifier of this IdentityLdapSettings.  # noqa: E501
        :type user_search_identifier: str
        """

        self._user_search_identifier = user_search_identifier

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
        if not isinstance(other, IdentityLdapSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityLdapSettings):
            return True

        return self.to_dict() != other.to_dict()
