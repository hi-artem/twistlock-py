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


class SharedSecretsStore(object):
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
        'ca_cert': 'CommonSecret',
        'client_cert': 'CommonSecret',
        'credential_id': 'str',
        'name': 'str',
        'region': 'str',
        'type': 'SharedSecretStoreType',
        'url': 'str'
    }

    attribute_map = {
        'app_id': 'appID',
        'ca_cert': 'caCert',
        'client_cert': 'clientCert',
        'credential_id': 'credentialId',
        'name': 'name',
        'region': 'region',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, app_id=None, ca_cert=None, client_cert=None, credential_id=None, name=None, region=None, type=None, url=None, local_vars_configuration=None):  # noqa: E501
        """SharedSecretsStore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._ca_cert = None
        self._client_cert = None
        self._credential_id = None
        self._name = None
        self._region = None
        self._type = None
        self._url = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if ca_cert is not None:
            self.ca_cert = ca_cert
        if client_cert is not None:
            self.client_cert = client_cert
        if credential_id is not None:
            self.credential_id = credential_id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def app_id(self):
        """Gets the app_id of this SharedSecretsStore.  # noqa: E501

        AppID is the twistlock application id, as set in Cyberark store.   # noqa: E501

        :return: The app_id of this SharedSecretsStore.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SharedSecretsStore.

        AppID is the twistlock application id, as set in Cyberark store.   # noqa: E501

        :param app_id: The app_id of this SharedSecretsStore.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def ca_cert(self):
        """Gets the ca_cert of this SharedSecretsStore.  # noqa: E501


        :return: The ca_cert of this SharedSecretsStore.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this SharedSecretsStore.


        :param ca_cert: The ca_cert of this SharedSecretsStore.  # noqa: E501
        :type ca_cert: CommonSecret
        """

        self._ca_cert = ca_cert

    @property
    def client_cert(self):
        """Gets the client_cert of this SharedSecretsStore.  # noqa: E501


        :return: The client_cert of this SharedSecretsStore.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this SharedSecretsStore.


        :param client_cert: The client_cert of this SharedSecretsStore.  # noqa: E501
        :type client_cert: CommonSecret
        """

        self._client_cert = client_cert

    @property
    def credential_id(self):
        """Gets the credential_id of this SharedSecretsStore.  # noqa: E501

        CredentialID is the authentication credential id.   # noqa: E501

        :return: The credential_id of this SharedSecretsStore.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this SharedSecretsStore.

        CredentialID is the authentication credential id.   # noqa: E501

        :param credential_id: The credential_id of this SharedSecretsStore.  # noqa: E501
        :type credential_id: str
        """

        self._credential_id = credential_id

    @property
    def name(self):
        """Gets the name of this SharedSecretsStore.  # noqa: E501

        Name is the name of the secret store defined by the user.   # noqa: E501

        :return: The name of this SharedSecretsStore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedSecretsStore.

        Name is the name of the secret store defined by the user.   # noqa: E501

        :param name: The name of this SharedSecretsStore.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this SharedSecretsStore.  # noqa: E501

        Region is the secrets store's region.   # noqa: E501

        :return: The region of this SharedSecretsStore.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SharedSecretsStore.

        Region is the secrets store's region.   # noqa: E501

        :param region: The region of this SharedSecretsStore.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def type(self):
        """Gets the type of this SharedSecretsStore.  # noqa: E501


        :return: The type of this SharedSecretsStore.  # noqa: E501
        :rtype: SharedSecretStoreType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SharedSecretsStore.


        :param type: The type of this SharedSecretsStore.  # noqa: E501
        :type type: SharedSecretStoreType
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this SharedSecretsStore.  # noqa: E501

        URL is the secrets store's endpoint point.   # noqa: E501

        :return: The url of this SharedSecretsStore.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SharedSecretsStore.

        URL is the secrets store's endpoint point.   # noqa: E501

        :param url: The url of this SharedSecretsStore.  # noqa: E501
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
        if not isinstance(other, SharedSecretsStore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedSecretsStore):
            return True

        return self.to_dict() != other.to_dict()
