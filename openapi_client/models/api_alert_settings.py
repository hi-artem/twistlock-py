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


class ApiAlertSettings(object):
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
        'aggregation_period_ms': 'int',
        'security_advisor_webhook': 'str'
    }

    attribute_map = {
        'aggregation_period_ms': 'aggregationPeriodMs',
        'security_advisor_webhook': 'securityAdvisorWebhook'
    }

    def __init__(self, aggregation_period_ms=None, security_advisor_webhook=None, local_vars_configuration=None):  # noqa: E501
        """ApiAlertSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aggregation_period_ms = None
        self._security_advisor_webhook = None
        self.discriminator = None

        if aggregation_period_ms is not None:
            self.aggregation_period_ms = aggregation_period_ms
        if security_advisor_webhook is not None:
            self.security_advisor_webhook = security_advisor_webhook

    @property
    def aggregation_period_ms(self):
        """Gets the aggregation_period_ms of this ApiAlertSettings.  # noqa: E501

        AggregationPeriodMs is the alert aggregation period in milliseconds.   # noqa: E501

        :return: The aggregation_period_ms of this ApiAlertSettings.  # noqa: E501
        :rtype: int
        """
        return self._aggregation_period_ms

    @aggregation_period_ms.setter
    def aggregation_period_ms(self, aggregation_period_ms):
        """Sets the aggregation_period_ms of this ApiAlertSettings.

        AggregationPeriodMs is the alert aggregation period in milliseconds.   # noqa: E501

        :param aggregation_period_ms: The aggregation_period_ms of this ApiAlertSettings.  # noqa: E501
        :type aggregation_period_ms: int
        """

        self._aggregation_period_ms = aggregation_period_ms

    @property
    def security_advisor_webhook(self):
        """Gets the security_advisor_webhook of this ApiAlertSettings.  # noqa: E501

        SecurityAdvisorWebhook is a webhook for IBM security advisor alert wizard, used to authenticate the wizard with the console and to pull data.   # noqa: E501

        :return: The security_advisor_webhook of this ApiAlertSettings.  # noqa: E501
        :rtype: str
        """
        return self._security_advisor_webhook

    @security_advisor_webhook.setter
    def security_advisor_webhook(self, security_advisor_webhook):
        """Sets the security_advisor_webhook of this ApiAlertSettings.

        SecurityAdvisorWebhook is a webhook for IBM security advisor alert wizard, used to authenticate the wizard with the console and to pull data.   # noqa: E501

        :param security_advisor_webhook: The security_advisor_webhook of this ApiAlertSettings.  # noqa: E501
        :type security_advisor_webhook: str
        """

        self._security_advisor_webhook = security_advisor_webhook

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
        if not isinstance(other, ApiAlertSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiAlertSettings):
            return True

        return self.to_dict() != other.to_dict()
