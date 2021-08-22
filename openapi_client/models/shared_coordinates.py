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


class SharedCoordinates(object):
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
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """SharedCoordinates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this SharedCoordinates.  # noqa: E501

        Latitude coordinate.   # noqa: E501

        :return: The latitude of this SharedCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this SharedCoordinates.

        Latitude coordinate.   # noqa: E501

        :param latitude: The latitude of this SharedCoordinates.  # noqa: E501
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this SharedCoordinates.  # noqa: E501

        Longitude coordinate.   # noqa: E501

        :return: The longitude of this SharedCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this SharedCoordinates.

        Longitude coordinate.   # noqa: E501

        :param longitude: The longitude of this SharedCoordinates.  # noqa: E501
        :type longitude: float
        """

        self._longitude = longitude

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
        if not isinstance(other, SharedCoordinates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedCoordinates):
            return True

        return self.to_dict() != other.to_dict()
