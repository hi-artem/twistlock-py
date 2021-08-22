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


class CodereposManifestFile(object):
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
        'dependencies': 'list[CodereposPkgDependency]',
        'distribution': 'VulnDistribution',
        'path': 'str',
        'type': 'VulnPackageType'
    }

    attribute_map = {
        'dependencies': 'dependencies',
        'distribution': 'distribution',
        'path': 'path',
        'type': 'type'
    }

    def __init__(self, dependencies=None, distribution=None, path=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CodereposManifestFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dependencies = None
        self._distribution = None
        self._path = None
        self._type = None
        self.discriminator = None

        if dependencies is not None:
            self.dependencies = dependencies
        if distribution is not None:
            self.distribution = distribution
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type

    @property
    def dependencies(self):
        """Gets the dependencies of this CodereposManifestFile.  # noqa: E501

        Packages listed in the manifest file.   # noqa: E501

        :return: The dependencies of this CodereposManifestFile.  # noqa: E501
        :rtype: list[CodereposPkgDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this CodereposManifestFile.

        Packages listed in the manifest file.   # noqa: E501

        :param dependencies: The dependencies of this CodereposManifestFile.  # noqa: E501
        :type dependencies: list[CodereposPkgDependency]
        """

        self._dependencies = dependencies

    @property
    def distribution(self):
        """Gets the distribution of this CodereposManifestFile.  # noqa: E501


        :return: The distribution of this CodereposManifestFile.  # noqa: E501
        :rtype: VulnDistribution
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this CodereposManifestFile.


        :param distribution: The distribution of this CodereposManifestFile.  # noqa: E501
        :type distribution: VulnDistribution
        """

        self._distribution = distribution

    @property
    def path(self):
        """Gets the path of this CodereposManifestFile.  # noqa: E501

        Path to the file.   # noqa: E501

        :return: The path of this CodereposManifestFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CodereposManifestFile.

        Path to the file.   # noqa: E501

        :param path: The path of this CodereposManifestFile.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this CodereposManifestFile.  # noqa: E501


        :return: The type of this CodereposManifestFile.  # noqa: E501
        :rtype: VulnPackageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodereposManifestFile.


        :param type: The type of this CodereposManifestFile.  # noqa: E501
        :type type: VulnPackageType
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
        if not isinstance(other, CodereposManifestFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CodereposManifestFile):
            return True

        return self.to_dict() != other.to_dict()