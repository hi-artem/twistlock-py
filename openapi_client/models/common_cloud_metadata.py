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


class CommonCloudMetadata(object):
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
        'account_id': 'str',
        'image': 'str',
        'labels': 'list[CommonExternalLabel]',
        'name': 'str',
        'provider': 'CommonCloudProvider',
        'region': 'str',
        'resource_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'account_id': 'accountID',
        'image': 'image',
        'labels': 'labels',
        'name': 'name',
        'provider': 'provider',
        'region': 'region',
        'resource_id': 'resourceID',
        'type': 'type'
    }

    def __init__(self, account_id=None, image=None, labels=None, name=None, provider=None, region=None, resource_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CommonCloudMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._image = None
        self._labels = None
        self._name = None
        self._provider = None
        self._region = None
        self._resource_id = None
        self._type = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if image is not None:
            self.image = image
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if region is not None:
            self.region = region
        if resource_id is not None:
            self.resource_id = resource_id
        if type is not None:
            self.type = type

    @property
    def account_id(self):
        """Gets the account_id of this CommonCloudMetadata.  # noqa: E501

        Cloud account ID.   # noqa: E501

        :return: The account_id of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CommonCloudMetadata.

        Cloud account ID.   # noqa: E501

        :param account_id: The account_id of this CommonCloudMetadata.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def image(self):
        """Gets the image of this CommonCloudMetadata.  # noqa: E501

        Image name.   # noqa: E501

        :return: The image of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CommonCloudMetadata.

        Image name.   # noqa: E501

        :param image: The image of this CommonCloudMetadata.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def labels(self):
        """Gets the labels of this CommonCloudMetadata.  # noqa: E501

        Cloud provider metadata labels.   # noqa: E501

        :return: The labels of this CommonCloudMetadata.  # noqa: E501
        :rtype: list[CommonExternalLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CommonCloudMetadata.

        Cloud provider metadata labels.   # noqa: E501

        :param labels: The labels of this CommonCloudMetadata.  # noqa: E501
        :type labels: list[CommonExternalLabel]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this CommonCloudMetadata.  # noqa: E501

        Instance name.   # noqa: E501

        :return: The name of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommonCloudMetadata.

        Instance name.   # noqa: E501

        :param name: The name of this CommonCloudMetadata.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this CommonCloudMetadata.  # noqa: E501


        :return: The provider of this CommonCloudMetadata.  # noqa: E501
        :rtype: CommonCloudProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CommonCloudMetadata.


        :param provider: The provider of this CommonCloudMetadata.  # noqa: E501
        :type provider: CommonCloudProvider
        """

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this CommonCloudMetadata.  # noqa: E501

        Instance region.   # noqa: E501

        :return: The region of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CommonCloudMetadata.

        Instance region.   # noqa: E501

        :param region: The region of this CommonCloudMetadata.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def resource_id(self):
        """Gets the resource_id of this CommonCloudMetadata.  # noqa: E501

        Unique ID of the resource.   # noqa: E501

        :return: The resource_id of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CommonCloudMetadata.

        Unique ID of the resource.   # noqa: E501

        :param resource_id: The resource_id of this CommonCloudMetadata.  # noqa: E501
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def type(self):
        """Gets the type of this CommonCloudMetadata.  # noqa: E501

        Instance type.   # noqa: E501

        :return: The type of this CommonCloudMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CommonCloudMetadata.

        Instance type.   # noqa: E501

        :param type: The type of this CommonCloudMetadata.  # noqa: E501
        :type type: str
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
        if not isinstance(other, CommonCloudMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommonCloudMetadata):
            return True

        return self.to_dict() != other.to_dict()