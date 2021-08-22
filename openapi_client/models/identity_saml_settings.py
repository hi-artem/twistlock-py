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


class IdentitySamlSettings(object):
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
        'app_id': 'str',
        'app_secret': 'CommonSecret',
        'audience': 'str',
        'cert': 'str',
        'console_url': 'str',
        'enabled': 'bool',
        'issuer': 'str',
        'provider_alias': 'str',
        'skip_authn_context': 'bool',
        'tenant_id': 'str',
        'type': 'IdentitySamlType',
        'url': 'str'
    }

    attribute_map = {
        'app_id': 'appId',
        'app_secret': 'appSecret',
        'audience': 'audience',
        'cert': 'cert',
        'console_url': 'consoleURL',
        'enabled': 'enabled',
        'issuer': 'issuer',
        'provider_alias': 'providerAlias',
        'skip_authn_context': 'skipAuthnContext',
        'tenant_id': 'tenantId',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, app_id=None, app_secret=None, audience=None, cert=None, console_url=None, enabled=None, issuer=None, provider_alias=None, skip_authn_context=None, tenant_id=None, type=None, url=None, local_vars_configuration=None):  # noqa: E501
        """IdentitySamlSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._app_secret = None
        self._audience = None
        self._cert = None
        self._console_url = None
        self._enabled = None
        self._issuer = None
        self._provider_alias = None
        self._skip_authn_context = None
        self._tenant_id = None
        self._type = None
        self._url = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_secret is not None:
            self.app_secret = app_secret
        if audience is not None:
            self.audience = audience
        if cert is not None:
            self.cert = cert
        if console_url is not None:
            self.console_url = console_url
        if enabled is not None:
            self.enabled = enabled
        if issuer is not None:
            self.issuer = issuer
        if provider_alias is not None:
            self.provider_alias = provider_alias
        if skip_authn_context is not None:
            self.skip_authn_context = skip_authn_context
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def app_id(self):
        """Gets the app_id of this IdentitySamlSettings.  # noqa: E501

        AppID is the Azure application ID.   # noqa: E501

        :return: The app_id of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this IdentitySamlSettings.

        AppID is the Azure application ID.   # noqa: E501

        :param app_id: The app_id of this IdentitySamlSettings.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def app_secret(self):
        """Gets the app_secret of this IdentitySamlSettings.  # noqa: E501


        :return: The app_secret of this IdentitySamlSettings.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this IdentitySamlSettings.


        :param app_secret: The app_secret of this IdentitySamlSettings.  # noqa: E501
        :type app_secret: CommonSecret
        """

        self._app_secret = app_secret

    @property
    def audience(self):
        """Gets the audience of this IdentitySamlSettings.  # noqa: E501

        Audience specifies the SAML audience used in the verification of the SAML response.   # noqa: E501

        :return: The audience of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this IdentitySamlSettings.

        Audience specifies the SAML audience used in the verification of the SAML response.   # noqa: E501

        :param audience: The audience of this IdentitySamlSettings.  # noqa: E501
        :type audience: str
        """

        self._audience = audience

    @property
    def cert(self):
        """Gets the cert of this IdentitySamlSettings.  # noqa: E501

        Cert is idp certificate in PEM format.   # noqa: E501

        :return: The cert of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this IdentitySamlSettings.

        Cert is idp certificate in PEM format.   # noqa: E501

        :param cert: The cert of this IdentitySamlSettings.  # noqa: E501
        :type cert: str
        """

        self._cert = cert

    @property
    def console_url(self):
        """Gets the console_url of this IdentitySamlSettings.  # noqa: E501

        ConsoleURL is the external Console URL that is used by the IDP for routing the browser after login.   # noqa: E501

        :return: The console_url of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this IdentitySamlSettings.

        ConsoleURL is the external Console URL that is used by the IDP for routing the browser after login.   # noqa: E501

        :param console_url: The console_url of this IdentitySamlSettings.  # noqa: E501
        :type console_url: str
        """

        self._console_url = console_url

    @property
    def enabled(self):
        """Gets the enabled of this IdentitySamlSettings.  # noqa: E501

        Enabled indicates whether saml settings are enabled.   # noqa: E501

        :return: The enabled of this IdentitySamlSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentitySamlSettings.

        Enabled indicates whether saml settings are enabled.   # noqa: E501

        :param enabled: The enabled of this IdentitySamlSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def issuer(self):
        """Gets the issuer of this IdentitySamlSettings.  # noqa: E501

        Issuer is idp issuer id.   # noqa: E501

        :return: The issuer of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this IdentitySamlSettings.

        Issuer is idp issuer id.   # noqa: E501

        :param issuer: The issuer of this IdentitySamlSettings.  # noqa: E501
        :type issuer: str
        """

        self._issuer = issuer

    @property
    def provider_alias(self):
        """Gets the provider_alias of this IdentitySamlSettings.  # noqa: E501

        ProviderAlias is the provider alias used for display.   # noqa: E501

        :return: The provider_alias of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._provider_alias

    @provider_alias.setter
    def provider_alias(self, provider_alias):
        """Sets the provider_alias of this IdentitySamlSettings.

        ProviderAlias is the provider alias used for display.   # noqa: E501

        :param provider_alias: The provider_alias of this IdentitySamlSettings.  # noqa: E501
        :type provider_alias: str
        """

        self._provider_alias = provider_alias

    @property
    def skip_authn_context(self):
        """Gets the skip_authn_context of this IdentitySamlSettings.  # noqa: E501

        SkipAuthnContext indicates whether request authentication contexts should be skipped.   # noqa: E501

        :return: The skip_authn_context of this IdentitySamlSettings.  # noqa: E501
        :rtype: bool
        """
        return self._skip_authn_context

    @skip_authn_context.setter
    def skip_authn_context(self, skip_authn_context):
        """Sets the skip_authn_context of this IdentitySamlSettings.

        SkipAuthnContext indicates whether request authentication contexts should be skipped.   # noqa: E501

        :param skip_authn_context: The skip_authn_context of this IdentitySamlSettings.  # noqa: E501
        :type skip_authn_context: bool
        """

        self._skip_authn_context = skip_authn_context

    @property
    def tenant_id(self):
        """Gets the tenant_id of this IdentitySamlSettings.  # noqa: E501

        TenantID is the Azure Tenant ID.   # noqa: E501

        :return: The tenant_id of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this IdentitySamlSettings.

        TenantID is the Azure Tenant ID.   # noqa: E501

        :param tenant_id: The tenant_id of this IdentitySamlSettings.  # noqa: E501
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this IdentitySamlSettings.  # noqa: E501


        :return: The type of this IdentitySamlSettings.  # noqa: E501
        :rtype: IdentitySamlType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentitySamlSettings.


        :param type: The type of this IdentitySamlSettings.  # noqa: E501
        :type type: IdentitySamlType
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this IdentitySamlSettings.  # noqa: E501

        Url is idp sso url.   # noqa: E501

        :return: The url of this IdentitySamlSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdentitySamlSettings.

        Url is idp sso url.   # noqa: E501

        :param url: The url of this IdentitySamlSettings.  # noqa: E501
        :type url: str
        """

        self._url = url

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
        if not isinstance(other, IdentitySamlSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentitySamlSettings):
            return True

        return self.to_dict() != other.to_dict()