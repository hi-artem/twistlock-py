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


class SharedRegionData(object):
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
        'coordinates': 'SharedCoordinates',
        'name': 'str',
        'region': 'str',
        'supported_services': 'list[SharedScanResultType]'
    }

    attribute_map = {
        'coordinates': 'coordinates',
        'name': 'name',
        'region': 'region',
        'supported_services': 'supportedServices'
    }

    def __init__(self, coordinates=None, name=None, region=None, supported_services=None, local_vars_configuration=None):  # noqa: E501
        """SharedRegionData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._coordinates = None
        self._name = None
        self._region = None
        self._supported_services = None
        self.discriminator = None

        if coordinates is not None:
            self.coordinates = coordinates
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if supported_services is not None:
            self.supported_services = supported_services

    @property
    def coordinates(self):
        """Gets the coordinates of this SharedRegionData.  # noqa: E501


        :return: The coordinates of this SharedRegionData.  # noqa: E501
        :rtype: SharedCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this SharedRegionData.


        :param coordinates: The coordinates of this SharedRegionData.  # noqa: E501
        :type coordinates: SharedCoordinates
        """

        self._coordinates = coordinates

    @property
    def name(self):
        """Gets the name of this SharedRegionData.  # noqa: E501

        Name is the region display name.   # noqa: E501

        :return: The name of this SharedRegionData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedRegionData.

        Name is the region display name.   # noqa: E501

        :param name: The name of this SharedRegionData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this SharedRegionData.  # noqa: E501

        Region is the region code name.   # noqa: E501

        :return: The region of this SharedRegionData.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SharedRegionData.

        Region is the region code name.   # noqa: E501

        :param region: The region of this SharedRegionData.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def supported_services(self):
        """Gets the supported_services of this SharedRegionData.  # noqa: E501

        SupportedServices is a list of cloud service types the region supports.   # noqa: E501

        :return: The supported_services of this SharedRegionData.  # noqa: E501
        :rtype: list[SharedScanResultType]
        """
        return self._supported_services

    @supported_services.setter
    def supported_services(self, supported_services):
        """Sets the supported_services of this SharedRegionData.

        SupportedServices is a list of cloud service types the region supports.   # noqa: E501

        :param supported_services: The supported_services of this SharedRegionData.  # noqa: E501
        :type supported_services: list[SharedScanResultType]
        """

        self._supported_services = supported_services

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
        if not isinstance(other, SharedRegionData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedRegionData):
            return True

        return self.to_dict() != other.to_dict()
