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


class TypesBaseImage(object):
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
        'creation_time': 'datetime',
        'image_name': 'str',
        'top_layer': 'str'
    }

    attribute_map = {
        'creation_time': 'creationTime',
        'image_name': 'imageName',
        'top_layer': 'topLayer'
    }

    def __init__(self, creation_time=None, image_name=None, top_layer=None, local_vars_configuration=None):  # noqa: E501
        """TypesBaseImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._creation_time = None
        self._image_name = None
        self._top_layer = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if image_name is not None:
            self.image_name = image_name
        if top_layer is not None:
            self.top_layer = top_layer

    @property
    def creation_time(self):
        """Gets the creation_time of this TypesBaseImage.  # noqa: E501

        CreationTime is the time when the image was created.   # noqa: E501

        :return: The creation_time of this TypesBaseImage.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TypesBaseImage.

        CreationTime is the time when the image was created.   # noqa: E501

        :param creation_time: The creation_time of this TypesBaseImage.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def image_name(self):
        """Gets the image_name of this TypesBaseImage.  # noqa: E501

        ImageName is the image name repository:tag.   # noqa: E501

        :return: The image_name of this TypesBaseImage.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this TypesBaseImage.

        ImageName is the image name repository:tag.   # noqa: E501

        :param image_name: The image_name of this TypesBaseImage.  # noqa: E501
        :type image_name: str
        """

        self._image_name = image_name

    @property
    def top_layer(self):
        """Gets the top_layer of this TypesBaseImage.  # noqa: E501

        TopLayer is the SHA256 of the image's last filesystem layer.   # noqa: E501

        :return: The top_layer of this TypesBaseImage.  # noqa: E501
        :rtype: str
        """
        return self._top_layer

    @top_layer.setter
    def top_layer(self, top_layer):
        """Sets the top_layer of this TypesBaseImage.

        TopLayer is the SHA256 of the image's last filesystem layer.   # noqa: E501

        :param top_layer: The top_layer of this TypesBaseImage.  # noqa: E501
        :type top_layer: str
        """

        self._top_layer = top_layer

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
        if not isinstance(other, TypesBaseImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypesBaseImage):
            return True

        return self.to_dict() != other.to_dict()