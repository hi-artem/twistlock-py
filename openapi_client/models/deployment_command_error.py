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


class DeploymentCommandError(object):
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
        'error': 'str',
        'hostname': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'region': 'str',
        'vm_image': 'str'
    }

    attribute_map = {
        'error': 'error',
        'hostname': 'hostname',
        'instance_id': 'instanceID',
        'instance_name': 'instanceName',
        'region': 'region',
        'vm_image': 'vmImage'
    }

    def __init__(self, error=None, hostname=None, instance_id=None, instance_name=None, region=None, vm_image=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentCommandError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._hostname = None
        self._instance_id = None
        self._instance_name = None
        self._region = None
        self._vm_image = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if hostname is not None:
            self.hostname = hostname
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if region is not None:
            self.region = region
        if vm_image is not None:
            self.vm_image = vm_image

    @property
    def error(self):
        """Gets the error of this DeploymentCommandError.  # noqa: E501

        Error is the error in case the command failed.   # noqa: E501

        :return: The error of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DeploymentCommandError.

        Error is the error in case the command failed.   # noqa: E501

        :param error: The error of this DeploymentCommandError.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def hostname(self):
        """Gets the hostname of this DeploymentCommandError.  # noqa: E501

        HostName is the instance hostname.   # noqa: E501

        :return: The hostname of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeploymentCommandError.

        HostName is the instance hostname.   # noqa: E501

        :param hostname: The hostname of this DeploymentCommandError.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def instance_id(self):
        """Gets the instance_id of this DeploymentCommandError.  # noqa: E501

        InstanceID is the instance id.   # noqa: E501

        :return: The instance_id of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeploymentCommandError.

        InstanceID is the instance id.   # noqa: E501

        :param instance_id: The instance_id of this DeploymentCommandError.  # noqa: E501
        :type instance_id: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DeploymentCommandError.  # noqa: E501

        instanceName is the instance name.   # noqa: E501

        :return: The instance_name of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DeploymentCommandError.

        instanceName is the instance name.   # noqa: E501

        :param instance_name: The instance_name of this DeploymentCommandError.  # noqa: E501
        :type instance_name: str
        """

        self._instance_name = instance_name

    @property
    def region(self):
        """Gets the region of this DeploymentCommandError.  # noqa: E501

        Region is the instance region.   # noqa: E501

        :return: The region of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DeploymentCommandError.

        Region is the instance region.   # noqa: E501

        :param region: The region of this DeploymentCommandError.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def vm_image(self):
        """Gets the vm_image of this DeploymentCommandError.  # noqa: E501

        VMImage is the instance image.   # noqa: E501

        :return: The vm_image of this DeploymentCommandError.  # noqa: E501
        :rtype: str
        """
        return self._vm_image

    @vm_image.setter
    def vm_image(self, vm_image):
        """Sets the vm_image of this DeploymentCommandError.

        VMImage is the instance image.   # noqa: E501

        :param vm_image: The vm_image of this DeploymentCommandError.  # noqa: E501
        :type vm_image: str
        """

        self._vm_image = vm_image

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
        if not isinstance(other, DeploymentCommandError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentCommandError):
            return True

        return self.to_dict() != other.to_dict()
