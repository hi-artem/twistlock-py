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


class CredCredential(object):
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
        'id': 'str',
        'account_guid': 'str',
        'account_id': 'str',
        'api_token': 'CommonSecret',
        'ca_cert': 'str',
        'description': 'str',
        'external': 'bool',
        'last_modified': 'datetime',
        'owner': 'str',
        'role_arn': 'str',
        'secret': 'CommonSecret',
        'tokens': 'CredTemporaryToken',
        'type': 'CredType',
        'use_aws_role': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'account_guid': 'accountGUID',
        'account_id': 'accountID',
        'api_token': 'apiToken',
        'ca_cert': 'caCert',
        'description': 'description',
        'external': 'external',
        'last_modified': 'lastModified',
        'owner': 'owner',
        'role_arn': 'roleArn',
        'secret': 'secret',
        'tokens': 'tokens',
        'type': 'type',
        'use_aws_role': 'useAWSRole'
    }

    def __init__(self, id=None, account_guid=None, account_id=None, api_token=None, ca_cert=None, description=None, external=None, last_modified=None, owner=None, role_arn=None, secret=None, tokens=None, type=None, use_aws_role=None, local_vars_configuration=None):  # noqa: E501
        """CredCredential - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._account_guid = None
        self._account_id = None
        self._api_token = None
        self._ca_cert = None
        self._description = None
        self._external = None
        self._last_modified = None
        self._owner = None
        self._role_arn = None
        self._secret = None
        self._tokens = None
        self._type = None
        self._use_aws_role = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_guid is not None:
            self.account_guid = account_guid
        if account_id is not None:
            self.account_id = account_id
        if api_token is not None:
            self.api_token = api_token
        if ca_cert is not None:
            self.ca_cert = ca_cert
        if description is not None:
            self.description = description
        if external is not None:
            self.external = external
        if last_modified is not None:
            self.last_modified = last_modified
        if owner is not None:
            self.owner = owner
        if role_arn is not None:
            self.role_arn = role_arn
        if secret is not None:
            self.secret = secret
        if tokens is not None:
            self.tokens = tokens
        if type is not None:
            self.type = type
        if use_aws_role is not None:
            self.use_aws_role = use_aws_role

    @property
    def id(self):
        """Gets the id of this CredCredential.  # noqa: E501

        Unique ID for the credential.   # noqa: E501

        :return: The id of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CredCredential.

        Unique ID for the credential.   # noqa: E501

        :param id: The id of this CredCredential.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def account_guid(self):
        """Gets the account_guid of this CredCredential.  # noqa: E501

        Unique ID for an IBM Cloud account.   # noqa: E501

        :return: The account_guid of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._account_guid

    @account_guid.setter
    def account_guid(self, account_guid):
        """Sets the account_guid of this CredCredential.

        Unique ID for an IBM Cloud account.   # noqa: E501

        :param account_guid: The account_guid of this CredCredential.  # noqa: E501
        :type account_guid: str
        """

        self._account_guid = account_guid

    @property
    def account_id(self):
        """Gets the account_id of this CredCredential.  # noqa: E501

        Account identifier (e.g., username, access key, account GUID, etc.).   # noqa: E501

        :return: The account_id of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CredCredential.

        Account identifier (e.g., username, access key, account GUID, etc.).   # noqa: E501

        :param account_id: The account_id of this CredCredential.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def api_token(self):
        """Gets the api_token of this CredCredential.  # noqa: E501


        :return: The api_token of this CredCredential.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this CredCredential.


        :param api_token: The api_token of this CredCredential.  # noqa: E501
        :type api_token: CommonSecret
        """

        self._api_token = api_token

    @property
    def ca_cert(self):
        """Gets the ca_cert of this CredCredential.  # noqa: E501

        CA certificate for certificate-based authentication.   # noqa: E501

        :return: The ca_cert of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this CredCredential.

        CA certificate for certificate-based authentication.   # noqa: E501

        :param ca_cert: The ca_cert of this CredCredential.  # noqa: E501
        :type ca_cert: str
        """

        self._ca_cert = ca_cert

    @property
    def description(self):
        """Gets the description of this CredCredential.  # noqa: E501

        Description of the credential.   # noqa: E501

        :return: The description of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CredCredential.

        Description of the credential.   # noqa: E501

        :param description: The description of this CredCredential.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def external(self):
        """Gets the external of this CredCredential.  # noqa: E501

        Indicates if the credential is external (true) or not (false).   # noqa: E501

        :return: The external of this CredCredential.  # noqa: E501
        :rtype: bool
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this CredCredential.

        Indicates if the credential is external (true) or not (false).   # noqa: E501

        :param external: The external of this CredCredential.  # noqa: E501
        :type external: bool
        """

        self._external = external

    @property
    def last_modified(self):
        """Gets the last_modified of this CredCredential.  # noqa: E501

        Datetime when the credential was last modified.   # noqa: E501

        :return: The last_modified of this CredCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CredCredential.

        Datetime when the credential was last modified.   # noqa: E501

        :param last_modified: The last_modified of this CredCredential.  # noqa: E501
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def owner(self):
        """Gets the owner of this CredCredential.  # noqa: E501

        User who created or modified the credential.   # noqa: E501

        :return: The owner of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CredCredential.

        User who created or modified the credential.   # noqa: E501

        :param owner: The owner of this CredCredential.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def role_arn(self):
        """Gets the role_arn of this CredCredential.  # noqa: E501

        Amazon Resource Name (ARN) of the role to assume.   # noqa: E501

        :return: The role_arn of this CredCredential.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this CredCredential.

        Amazon Resource Name (ARN) of the role to assume.   # noqa: E501

        :param role_arn: The role_arn of this CredCredential.  # noqa: E501
        :type role_arn: str
        """

        self._role_arn = role_arn

    @property
    def secret(self):
        """Gets the secret of this CredCredential.  # noqa: E501


        :return: The secret of this CredCredential.  # noqa: E501
        :rtype: CommonSecret
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this CredCredential.


        :param secret: The secret of this CredCredential.  # noqa: E501
        :type secret: CommonSecret
        """

        self._secret = secret

    @property
    def tokens(self):
        """Gets the tokens of this CredCredential.  # noqa: E501


        :return: The tokens of this CredCredential.  # noqa: E501
        :rtype: CredTemporaryToken
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this CredCredential.


        :param tokens: The tokens of this CredCredential.  # noqa: E501
        :type tokens: CredTemporaryToken
        """

        self._tokens = tokens

    @property
    def type(self):
        """Gets the type of this CredCredential.  # noqa: E501


        :return: The type of this CredCredential.  # noqa: E501
        :rtype: CredType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredCredential.


        :param type: The type of this CredCredential.  # noqa: E501
        :type type: CredType
        """

        self._type = type

    @property
    def use_aws_role(self):
        """Gets the use_aws_role of this CredCredential.  # noqa: E501

        Indicates if authentication should be done with the instance's attached credentials (EC2 IAM Role).   # noqa: E501

        :return: The use_aws_role of this CredCredential.  # noqa: E501
        :rtype: bool
        """
        return self._use_aws_role

    @use_aws_role.setter
    def use_aws_role(self, use_aws_role):
        """Sets the use_aws_role of this CredCredential.

        Indicates if authentication should be done with the instance's attached credentials (EC2 IAM Role).   # noqa: E501

        :param use_aws_role: The use_aws_role of this CredCredential.  # noqa: E501
        :type use_aws_role: bool
        """

        self._use_aws_role = use_aws_role

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
        if not isinstance(other, CredCredential):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredCredential):
            return True

        return self.to_dict() != other.to_dict()
