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


class WaasDoSMatchCondition(object):
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
        'file_types': 'list[str]',
        'methods': 'list[str]',
        'response_code_ranges': 'list[WaasStatusCodeRange]'
    }

    attribute_map = {
        'file_types': 'fileTypes',
        'methods': 'methods',
        'response_code_ranges': 'responseCodeRanges'
    }

    def __init__(self, file_types=None, methods=None, response_code_ranges=None, local_vars_configuration=None):  # noqa: E501
        """WaasDoSMatchCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_types = None
        self._methods = None
        self._response_code_ranges = None
        self.discriminator = None

        if file_types is not None:
            self.file_types = file_types
        if methods is not None:
            self.methods = methods
        if response_code_ranges is not None:
            self.response_code_ranges = response_code_ranges

    @property
    def file_types(self):
        """Gets the file_types of this WaasDoSMatchCondition.  # noqa: E501

        File types for request matching.   # noqa: E501

        :return: The file_types of this WaasDoSMatchCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_types

    @file_types.setter
    def file_types(self, file_types):
        """Sets the file_types of this WaasDoSMatchCondition.

        File types for request matching.   # noqa: E501

        :param file_types: The file_types of this WaasDoSMatchCondition.  # noqa: E501
        :type file_types: list[str]
        """

        self._file_types = file_types

    @property
    def methods(self):
        """Gets the methods of this WaasDoSMatchCondition.  # noqa: E501

        HTTP methods for request matching.   # noqa: E501

        :return: The methods of this WaasDoSMatchCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this WaasDoSMatchCondition.

        HTTP methods for request matching.   # noqa: E501

        :param methods: The methods of this WaasDoSMatchCondition.  # noqa: E501
        :type methods: list[str]
        """

        self._methods = methods

    @property
    def response_code_ranges(self):
        """Gets the response_code_ranges of this WaasDoSMatchCondition.  # noqa: E501

        Response codes for the request's response matching.   # noqa: E501

        :return: The response_code_ranges of this WaasDoSMatchCondition.  # noqa: E501
        :rtype: list[WaasStatusCodeRange]
        """
        return self._response_code_ranges

    @response_code_ranges.setter
    def response_code_ranges(self, response_code_ranges):
        """Sets the response_code_ranges of this WaasDoSMatchCondition.

        Response codes for the request's response matching.   # noqa: E501

        :param response_code_ranges: The response_code_ranges of this WaasDoSMatchCondition.  # noqa: E501
        :type response_code_ranges: list[WaasStatusCodeRange]
        """

        self._response_code_ranges = response_code_ranges

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
        if not isinstance(other, WaasDoSMatchCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaasDoSMatchCondition):
            return True

        return self.to_dict() != other.to_dict()