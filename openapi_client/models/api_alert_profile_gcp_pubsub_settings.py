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


class ApiAlertProfileGcpPubsubSettings(object):
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
        'credential_id': 'str',
        'enabled': 'bool',
        'topic': 'str'
    }

    attribute_map = {
        'credential_id': 'credentialId',
        'enabled': 'enabled',
        'topic': 'topic'
    }

    def __init__(self, credential_id=None, enabled=None, topic=None, local_vars_configuration=None):  # noqa: E501
        """ApiAlertProfileGcpPubsubSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._credential_id = None
        self._enabled = None
        self._topic = None
        self.discriminator = None

        if credential_id is not None:
            self.credential_id = credential_id
        if enabled is not None:
            self.enabled = enabled
        if topic is not None:
            self.topic = topic

    @property
    def credential_id(self):
        """Gets the credential_id of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501

        CredentialID is the GCP Pub/Sub authentication credentials id.   # noqa: E501

        :return: The credential_id of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this ApiAlertProfileGcpPubsubSettings.

        CredentialID is the GCP Pub/Sub authentication credentials id.   # noqa: E501

        :param credential_id: The credential_id of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :type credential_id: str
        """

        self._credential_id = credential_id

    @property
    def enabled(self):
        """Gets the enabled of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501

        Enabled indicates whether the GCP Pub/Sub settings are enabled.   # noqa: E501

        :return: The enabled of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ApiAlertProfileGcpPubsubSettings.

        Enabled indicates whether the GCP Pub/Sub settings are enabled.   # noqa: E501

        :param enabled: The enabled of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def topic(self):
        """Gets the topic of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501

        Topic is the GCP Pub/Sub topic (used by subscribers to listen for messages).   # noqa: E501

        :return: The topic of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ApiAlertProfileGcpPubsubSettings.

        Topic is the GCP Pub/Sub topic (used by subscribers to listen for messages).   # noqa: E501

        :param topic: The topic of this ApiAlertProfileGcpPubsubSettings.  # noqa: E501
        :type topic: str
        """

        self._topic = topic

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
        if not isinstance(other, ApiAlertProfileGcpPubsubSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiAlertProfileGcpPubsubSettings):
            return True

        return self.to_dict() != other.to_dict()
