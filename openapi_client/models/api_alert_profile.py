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


class ApiAlertProfile(object):
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
        'id': 'str',
        'console_identifier': 'str',
        'disabled': 'bool',
        'email': 'ApiAlertProfileEmailSettings',
        'gcp_pubsub': 'ApiAlertProfileGcpPubsubSettings',
        'jira': 'ApiAlertProfileJIRASettings',
        'last_error': 'str',
        'modified': 'datetime',
        'name': 'str',
        'notes': 'str',
        'owner': 'str',
        'pagerduty': 'ApiAlertProfilePagerDutySettings',
        'policy': 'dict(str, ApiAlertRule)',
        'previous_name': 'str',
        'security_advisor': 'ApiAlertProfileSecurityAdvisor',
        'security_center': 'ApiAlertProfileSecurityCenterSettings',
        'security_hub': 'ApiAlertProfileSecurityHubSettings',
        'service_now': 'ApiAlertProfileServiceNowSettings',
        'slack': 'ApiAlertProfileSlackSettings',
        'webhook': 'ApiAlertProfileWebhookSettings',
        'xsoar': 'ApiAlertProfileXSOARSettings'
    }

    attribute_map = {
        'id': '_id',
        'console_identifier': 'consoleIdentifier',
        'disabled': 'disabled',
        'email': 'email',
        'gcp_pubsub': 'gcpPubsub',
        'jira': 'jira',
        'last_error': 'lastError',
        'modified': 'modified',
        'name': 'name',
        'notes': 'notes',
        'owner': 'owner',
        'pagerduty': 'pagerduty',
        'policy': 'policy',
        'previous_name': 'previousName',
        'security_advisor': 'securityAdvisor',
        'security_center': 'securityCenter',
        'security_hub': 'securityHub',
        'service_now': 'serviceNow',
        'slack': 'slack',
        'webhook': 'webhook',
        'xsoar': 'xsoar'
    }

    def __init__(self, id=None, console_identifier=None, disabled=None, email=None, gcp_pubsub=None, jira=None, last_error=None, modified=None, name=None, notes=None, owner=None, pagerduty=None, policy=None, previous_name=None, security_advisor=None, security_center=None, security_hub=None, service_now=None, slack=None, webhook=None, xsoar=None, local_vars_configuration=None):  # noqa: E501
        """ApiAlertProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._console_identifier = None
        self._disabled = None
        self._email = None
        self._gcp_pubsub = None
        self._jira = None
        self._last_error = None
        self._modified = None
        self._name = None
        self._notes = None
        self._owner = None
        self._pagerduty = None
        self._policy = None
        self._previous_name = None
        self._security_advisor = None
        self._security_center = None
        self._security_hub = None
        self._service_now = None
        self._slack = None
        self._webhook = None
        self._xsoar = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if console_identifier is not None:
            self.console_identifier = console_identifier
        if disabled is not None:
            self.disabled = disabled
        if email is not None:
            self.email = email
        if gcp_pubsub is not None:
            self.gcp_pubsub = gcp_pubsub
        if jira is not None:
            self.jira = jira
        if last_error is not None:
            self.last_error = last_error
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if owner is not None:
            self.owner = owner
        if pagerduty is not None:
            self.pagerduty = pagerduty
        if policy is not None:
            self.policy = policy
        if previous_name is not None:
            self.previous_name = previous_name
        if security_advisor is not None:
            self.security_advisor = security_advisor
        if security_center is not None:
            self.security_center = security_center
        if security_hub is not None:
            self.security_hub = security_hub
        if service_now is not None:
            self.service_now = service_now
        if slack is not None:
            self.slack = slack
        if webhook is not None:
            self.webhook = webhook
        if xsoar is not None:
            self.xsoar = xsoar

    @property
    def id(self):
        """Gets the id of this ApiAlertProfile.  # noqa: E501

        ID is the alert profile ID.   # noqa: E501

        :return: The id of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiAlertProfile.

        ID is the alert profile ID.   # noqa: E501

        :param id: The id of this ApiAlertProfile.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def console_identifier(self):
        """Gets the console_identifier of this ApiAlertProfile.  # noqa: E501

        ConsoleIdentifier is the console identifier.   # noqa: E501

        :return: The console_identifier of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._console_identifier

    @console_identifier.setter
    def console_identifier(self, console_identifier):
        """Sets the console_identifier of this ApiAlertProfile.

        ConsoleIdentifier is the console identifier.   # noqa: E501

        :param console_identifier: The console_identifier of this ApiAlertProfile.  # noqa: E501
        :type console_identifier: str
        """

        self._console_identifier = console_identifier

    @property
    def disabled(self):
        """Gets the disabled of this ApiAlertProfile.  # noqa: E501

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :return: The disabled of this ApiAlertProfile.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ApiAlertProfile.

        Indicates if the rule is currently disabled (true) or not (false).   # noqa: E501

        :param disabled: The disabled of this ApiAlertProfile.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def email(self):
        """Gets the email of this ApiAlertProfile.  # noqa: E501


        :return: The email of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileEmailSettings
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApiAlertProfile.


        :param email: The email of this ApiAlertProfile.  # noqa: E501
        :type email: ApiAlertProfileEmailSettings
        """

        self._email = email

    @property
    def gcp_pubsub(self):
        """Gets the gcp_pubsub of this ApiAlertProfile.  # noqa: E501


        :return: The gcp_pubsub of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileGcpPubsubSettings
        """
        return self._gcp_pubsub

    @gcp_pubsub.setter
    def gcp_pubsub(self, gcp_pubsub):
        """Sets the gcp_pubsub of this ApiAlertProfile.


        :param gcp_pubsub: The gcp_pubsub of this ApiAlertProfile.  # noqa: E501
        :type gcp_pubsub: ApiAlertProfileGcpPubsubSettings
        """

        self._gcp_pubsub = gcp_pubsub

    @property
    def jira(self):
        """Gets the jira of this ApiAlertProfile.  # noqa: E501


        :return: The jira of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileJIRASettings
        """
        return self._jira

    @jira.setter
    def jira(self, jira):
        """Sets the jira of this ApiAlertProfile.


        :param jira: The jira of this ApiAlertProfile.  # noqa: E501
        :type jira: ApiAlertProfileJIRASettings
        """

        self._jira = jira

    @property
    def last_error(self):
        """Gets the last_error of this ApiAlertProfile.  # noqa: E501

        LastError represents the last error when sending the profile.   # noqa: E501

        :return: The last_error of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        """Sets the last_error of this ApiAlertProfile.

        LastError represents the last error when sending the profile.   # noqa: E501

        :param last_error: The last_error of this ApiAlertProfile.  # noqa: E501
        :type last_error: str
        """

        self._last_error = last_error

    @property
    def modified(self):
        """Gets the modified of this ApiAlertProfile.  # noqa: E501

        Datetime when the rule was last modified.   # noqa: E501

        :return: The modified of this ApiAlertProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ApiAlertProfile.

        Datetime when the rule was last modified.   # noqa: E501

        :param modified: The modified of this ApiAlertProfile.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this ApiAlertProfile.  # noqa: E501

        Name of the rule.   # noqa: E501

        :return: The name of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiAlertProfile.

        Name of the rule.   # noqa: E501

        :param name: The name of this ApiAlertProfile.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this ApiAlertProfile.  # noqa: E501

        Free-form text.   # noqa: E501

        :return: The notes of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ApiAlertProfile.

        Free-form text.   # noqa: E501

        :param notes: The notes of this ApiAlertProfile.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def owner(self):
        """Gets the owner of this ApiAlertProfile.  # noqa: E501

        User who created or last modified the rule.   # noqa: E501

        :return: The owner of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ApiAlertProfile.

        User who created or last modified the rule.   # noqa: E501

        :param owner: The owner of this ApiAlertProfile.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def pagerduty(self):
        """Gets the pagerduty of this ApiAlertProfile.  # noqa: E501


        :return: The pagerduty of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfilePagerDutySettings
        """
        return self._pagerduty

    @pagerduty.setter
    def pagerduty(self, pagerduty):
        """Sets the pagerduty of this ApiAlertProfile.


        :param pagerduty: The pagerduty of this ApiAlertProfile.  # noqa: E501
        :type pagerduty: ApiAlertProfilePagerDutySettings
        """

        self._pagerduty = pagerduty

    @property
    def policy(self):
        """Gets the policy of this ApiAlertProfile.  # noqa: E501

        Policy contains the mapping between alert type to the applied alert rules.   # noqa: E501

        :return: The policy of this ApiAlertProfile.  # noqa: E501
        :rtype: dict(str, ApiAlertRule)
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ApiAlertProfile.

        Policy contains the mapping between alert type to the applied alert rules.   # noqa: E501

        :param policy: The policy of this ApiAlertProfile.  # noqa: E501
        :type policy: dict(str, ApiAlertRule)
        """

        self._policy = policy

    @property
    def previous_name(self):
        """Gets the previous_name of this ApiAlertProfile.  # noqa: E501

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :return: The previous_name of this ApiAlertProfile.  # noqa: E501
        :rtype: str
        """
        return self._previous_name

    @previous_name.setter
    def previous_name(self, previous_name):
        """Sets the previous_name of this ApiAlertProfile.

        Previous name of the rule. Required for rule renaming.   # noqa: E501

        :param previous_name: The previous_name of this ApiAlertProfile.  # noqa: E501
        :type previous_name: str
        """

        self._previous_name = previous_name

    @property
    def security_advisor(self):
        """Gets the security_advisor of this ApiAlertProfile.  # noqa: E501


        :return: The security_advisor of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileSecurityAdvisor
        """
        return self._security_advisor

    @security_advisor.setter
    def security_advisor(self, security_advisor):
        """Sets the security_advisor of this ApiAlertProfile.


        :param security_advisor: The security_advisor of this ApiAlertProfile.  # noqa: E501
        :type security_advisor: ApiAlertProfileSecurityAdvisor
        """

        self._security_advisor = security_advisor

    @property
    def security_center(self):
        """Gets the security_center of this ApiAlertProfile.  # noqa: E501


        :return: The security_center of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileSecurityCenterSettings
        """
        return self._security_center

    @security_center.setter
    def security_center(self, security_center):
        """Sets the security_center of this ApiAlertProfile.


        :param security_center: The security_center of this ApiAlertProfile.  # noqa: E501
        :type security_center: ApiAlertProfileSecurityCenterSettings
        """

        self._security_center = security_center

    @property
    def security_hub(self):
        """Gets the security_hub of this ApiAlertProfile.  # noqa: E501


        :return: The security_hub of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileSecurityHubSettings
        """
        return self._security_hub

    @security_hub.setter
    def security_hub(self, security_hub):
        """Sets the security_hub of this ApiAlertProfile.


        :param security_hub: The security_hub of this ApiAlertProfile.  # noqa: E501
        :type security_hub: ApiAlertProfileSecurityHubSettings
        """

        self._security_hub = security_hub

    @property
    def service_now(self):
        """Gets the service_now of this ApiAlertProfile.  # noqa: E501


        :return: The service_now of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileServiceNowSettings
        """
        return self._service_now

    @service_now.setter
    def service_now(self, service_now):
        """Sets the service_now of this ApiAlertProfile.


        :param service_now: The service_now of this ApiAlertProfile.  # noqa: E501
        :type service_now: ApiAlertProfileServiceNowSettings
        """

        self._service_now = service_now

    @property
    def slack(self):
        """Gets the slack of this ApiAlertProfile.  # noqa: E501


        :return: The slack of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileSlackSettings
        """
        return self._slack

    @slack.setter
    def slack(self, slack):
        """Sets the slack of this ApiAlertProfile.


        :param slack: The slack of this ApiAlertProfile.  # noqa: E501
        :type slack: ApiAlertProfileSlackSettings
        """

        self._slack = slack

    @property
    def webhook(self):
        """Gets the webhook of this ApiAlertProfile.  # noqa: E501


        :return: The webhook of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileWebhookSettings
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this ApiAlertProfile.


        :param webhook: The webhook of this ApiAlertProfile.  # noqa: E501
        :type webhook: ApiAlertProfileWebhookSettings
        """

        self._webhook = webhook

    @property
    def xsoar(self):
        """Gets the xsoar of this ApiAlertProfile.  # noqa: E501


        :return: The xsoar of this ApiAlertProfile.  # noqa: E501
        :rtype: ApiAlertProfileXSOARSettings
        """
        return self._xsoar

    @xsoar.setter
    def xsoar(self, xsoar):
        """Sets the xsoar of this ApiAlertProfile.


        :param xsoar: The xsoar of this ApiAlertProfile.  # noqa: E501
        :type xsoar: ApiAlertProfileXSOARSettings
        """

        self._xsoar = xsoar

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
        if not isinstance(other, ApiAlertProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiAlertProfile):
            return True

        return self.to_dict() != other.to_dict()