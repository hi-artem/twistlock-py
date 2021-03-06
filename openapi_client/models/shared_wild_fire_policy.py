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


class SharedWildFirePolicy(object):
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
        'compliance_enabled': 'bool',
        'grayware_as_malware': 'bool',
        'region': 'str',
        'runtime_enabled': 'bool',
        'upload_enabled': 'bool'
    }

    attribute_map = {
        'compliance_enabled': 'complianceEnabled',
        'grayware_as_malware': 'graywareAsMalware',
        'region': 'region',
        'runtime_enabled': 'runtimeEnabled',
        'upload_enabled': 'uploadEnabled'
    }

    def __init__(self, compliance_enabled=None, grayware_as_malware=None, region=None, runtime_enabled=None, upload_enabled=None, local_vars_configuration=None):  # noqa: E501
        """SharedWildFirePolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._compliance_enabled = None
        self._grayware_as_malware = None
        self._region = None
        self._runtime_enabled = None
        self._upload_enabled = None
        self.discriminator = None

        if compliance_enabled is not None:
            self.compliance_enabled = compliance_enabled
        if grayware_as_malware is not None:
            self.grayware_as_malware = grayware_as_malware
        if region is not None:
            self.region = region
        if runtime_enabled is not None:
            self.runtime_enabled = runtime_enabled
        if upload_enabled is not None:
            self.upload_enabled = upload_enabled

    @property
    def compliance_enabled(self):
        """Gets the compliance_enabled of this SharedWildFirePolicy.  # noqa: E501

        ComplianceEnabled indicates whether compliance malware scan will consult WF.   # noqa: E501

        :return: The compliance_enabled of this SharedWildFirePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._compliance_enabled

    @compliance_enabled.setter
    def compliance_enabled(self, compliance_enabled):
        """Sets the compliance_enabled of this SharedWildFirePolicy.

        ComplianceEnabled indicates whether compliance malware scan will consult WF.   # noqa: E501

        :param compliance_enabled: The compliance_enabled of this SharedWildFirePolicy.  # noqa: E501
        :type compliance_enabled: bool
        """

        self._compliance_enabled = compliance_enabled

    @property
    def grayware_as_malware(self):
        """Gets the grayware_as_malware of this SharedWildFirePolicy.  # noqa: E501

        GraywareAsMalware indicates whether files with WF verdict of Grayware will be treated as malware.   # noqa: E501

        :return: The grayware_as_malware of this SharedWildFirePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._grayware_as_malware

    @grayware_as_malware.setter
    def grayware_as_malware(self, grayware_as_malware):
        """Sets the grayware_as_malware of this SharedWildFirePolicy.

        GraywareAsMalware indicates whether files with WF verdict of Grayware will be treated as malware.   # noqa: E501

        :param grayware_as_malware: The grayware_as_malware of this SharedWildFirePolicy.  # noqa: E501
        :type grayware_as_malware: bool
        """

        self._grayware_as_malware = grayware_as_malware

    @property
    def region(self):
        """Gets the region of this SharedWildFirePolicy.  # noqa: E501

        Region is the WF server region to query.   # noqa: E501

        :return: The region of this SharedWildFirePolicy.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SharedWildFirePolicy.

        Region is the WF server region to query.   # noqa: E501

        :param region: The region of this SharedWildFirePolicy.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def runtime_enabled(self):
        """Gets the runtime_enabled of this SharedWildFirePolicy.  # noqa: E501

        RuntimeEnabled indicates whether runtime malware scan will consult WF.   # noqa: E501

        :return: The runtime_enabled of this SharedWildFirePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._runtime_enabled

    @runtime_enabled.setter
    def runtime_enabled(self, runtime_enabled):
        """Sets the runtime_enabled of this SharedWildFirePolicy.

        RuntimeEnabled indicates whether runtime malware scan will consult WF.   # noqa: E501

        :param runtime_enabled: The runtime_enabled of this SharedWildFirePolicy.  # noqa: E501
        :type runtime_enabled: bool
        """

        self._runtime_enabled = runtime_enabled

    @property
    def upload_enabled(self):
        """Gets the upload_enabled of this SharedWildFirePolicy.  # noqa: E501

        UploadEnabled indicates whether files will be uploaded to WF.   # noqa: E501

        :return: The upload_enabled of this SharedWildFirePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._upload_enabled

    @upload_enabled.setter
    def upload_enabled(self, upload_enabled):
        """Sets the upload_enabled of this SharedWildFirePolicy.

        UploadEnabled indicates whether files will be uploaded to WF.   # noqa: E501

        :param upload_enabled: The upload_enabled of this SharedWildFirePolicy.  # noqa: E501
        :type upload_enabled: bool
        """

        self._upload_enabled = upload_enabled

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
        if not isinstance(other, SharedWildFirePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedWildFirePolicy):
            return True

        return self.to_dict() != other.to_dict()
