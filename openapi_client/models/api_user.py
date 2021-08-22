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


class ApiUser(object):
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
        'auth_type': 'ApiAuthType',
        'last_modified': 'datetime',
        'password': 'str',
        'permissions': 'list[ApiPermission]',
        'role': 'str',
        'username': 'str'
    }

    attribute_map = {
        'auth_type': 'authType',
        'last_modified': 'lastModified',
        'password': 'password',
        'permissions': 'permissions',
        'role': 'role',
        'username': 'username'
    }

    def __init__(self, auth_type=None, last_modified=None, password=None, permissions=None, role=None, username=None, local_vars_configuration=None):  # noqa: E501
        """ApiUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._auth_type = None
        self._last_modified = None
        self._password = None
        self._permissions = None
        self._role = None
        self._username = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if last_modified is not None:
            self.last_modified = last_modified
        if password is not None:
            self.password = password
        if permissions is not None:
            self.permissions = permissions
        if role is not None:
            self.role = role
        if username is not None:
            self.username = username

    @property
    def auth_type(self):
        """Gets the auth_type of this ApiUser.  # noqa: E501


        :return: The auth_type of this ApiUser.  # noqa: E501
        :rtype: ApiAuthType
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ApiUser.


        :param auth_type: The auth_type of this ApiUser.  # noqa: E501
        :type auth_type: ApiAuthType
        """

        self._auth_type = auth_type

    @property
    def last_modified(self):
        """Gets the last_modified of this ApiUser.  # noqa: E501

        Datetime when the user was created or last modified.   # noqa: E501

        :return: The last_modified of this ApiUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ApiUser.

        Datetime when the user was created or last modified.   # noqa: E501

        :param last_modified: The last_modified of this ApiUser.  # noqa: E501
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def password(self):
        """Gets the password of this ApiUser.  # noqa: E501

        Password for authentication.   # noqa: E501

        :return: The password of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ApiUser.

        Password for authentication.   # noqa: E501

        :param password: The password of this ApiUser.  # noqa: E501
        :type password: str
        """

        self._password = password

    @property
    def permissions(self):
        """Gets the permissions of this ApiUser.  # noqa: E501

        Permissions is a list of permissions  # noqa: E501

        :return: The permissions of this ApiUser.  # noqa: E501
        :rtype: list[ApiPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ApiUser.

        Permissions is a list of permissions  # noqa: E501

        :param permissions: The permissions of this ApiUser.  # noqa: E501
        :type permissions: list[ApiPermission]
        """

        self._permissions = permissions

    @property
    def role(self):
        """Gets the role of this ApiUser.  # noqa: E501

        User role.   # noqa: E501

        :return: The role of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ApiUser.

        User role.   # noqa: E501

        :param role: The role of this ApiUser.  # noqa: E501
        :type role: str
        """

        self._role = role

    @property
    def username(self):
        """Gets the username of this ApiUser.  # noqa: E501

        Username for authentication.   # noqa: E501

        :return: The username of this ApiUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ApiUser.

        Username for authentication.   # noqa: E501

        :param username: The username of this ApiUser.  # noqa: E501
        :type username: str
        """

        self._username = username

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
        if not isinstance(other, ApiUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiUser):
            return True

        return self.to_dict() != other.to_dict()