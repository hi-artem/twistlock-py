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


class TypesUserProject(object):
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
        'address': 'str',
        'connected': 'bool',
        'creation_time': 'datetime'
    }

    attribute_map = {
        'id': '_id',
        'address': 'address',
        'connected': 'connected',
        'creation_time': 'creationTime'
    }

    def __init__(self, id=None, address=None, connected=None, creation_time=None, local_vars_configuration=None):  # noqa: E501
        """TypesUserProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._address = None
        self._connected = None
        self._creation_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if connected is not None:
            self.connected = connected
        if creation_time is not None:
            self.creation_time = creation_time

    @property
    def id(self):
        """Gets the id of this TypesUserProject.  # noqa: E501

        ID is the project id.   # noqa: E501

        :return: The id of this TypesUserProject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TypesUserProject.

        ID is the project id.   # noqa: E501

        :param id: The id of this TypesUserProject.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this TypesUserProject.  # noqa: E501

        Address is project address.   # noqa: E501

        :return: The address of this TypesUserProject.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this TypesUserProject.

        Address is project address.   # noqa: E501

        :param address: The address of this TypesUserProject.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def connected(self):
        """Gets the connected of this TypesUserProject.  # noqa: E501

        Connected indicates if the project is currently disconnected due to an error.   # noqa: E501

        :return: The connected of this TypesUserProject.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this TypesUserProject.

        Connected indicates if the project is currently disconnected due to an error.   # noqa: E501

        :param connected: The connected of this TypesUserProject.  # noqa: E501
        :type connected: bool
        """

        self._connected = connected

    @property
    def creation_time(self):
        """Gets the creation_time of this TypesUserProject.  # noqa: E501

        CreationTime is the project creation time.   # noqa: E501

        :return: The creation_time of this TypesUserProject.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TypesUserProject.

        CreationTime is the project creation time.   # noqa: E501

        :param creation_time: The creation_time of this TypesUserProject.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

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
        if not isinstance(other, TypesUserProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesUserProject):
            return True

        return self.to_dict() != other.to_dict()