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


class AdmissionAudit(object):
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
        'account_id': 'str',
        'attack_techniques': 'list[MitreTechnique]',
        'cluster': 'str',
        'collections': 'list[str]',
        'effect': 'str',
        'kind': 'str',
        'message': 'str',
        'namespace': 'str',
        'operation': 'str',
        'raw_request': 'str',
        'resource': 'str',
        'rule_name': 'str',
        'time': 'datetime',
        'user_groups': 'str',
        'user_uid': 'str',
        'username': 'str'
    }

    attribute_map = {
        'account_id': 'accountID',
        'attack_techniques': 'attackTechniques',
        'cluster': 'cluster',
        'collections': 'collections',
        'effect': 'effect',
        'kind': 'kind',
        'message': 'message',
        'namespace': 'namespace',
        'operation': 'operation',
        'raw_request': 'rawRequest',
        'resource': 'resource',
        'rule_name': 'ruleName',
        'time': 'time',
        'user_groups': 'userGroups',
        'user_uid': 'userUid',
        'username': 'username'
    }

    def __init__(self, account_id=None, attack_techniques=None, cluster=None, collections=None, effect=None, kind=None, message=None, namespace=None, operation=None, raw_request=None, resource=None, rule_name=None, time=None, user_groups=None, user_uid=None, username=None, local_vars_configuration=None):  # noqa: E501
        """AdmissionAudit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._attack_techniques = None
        self._cluster = None
        self._collections = None
        self._effect = None
        self._kind = None
        self._message = None
        self._namespace = None
        self._operation = None
        self._raw_request = None
        self._resource = None
        self._rule_name = None
        self._time = None
        self._user_groups = None
        self._user_uid = None
        self._username = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if attack_techniques is not None:
            self.attack_techniques = attack_techniques
        if cluster is not None:
            self.cluster = cluster
        if collections is not None:
            self.collections = collections
        if effect is not None:
            self.effect = effect
        if kind is not None:
            self.kind = kind
        if message is not None:
            self.message = message
        if namespace is not None:
            self.namespace = namespace
        if operation is not None:
            self.operation = operation
        if raw_request is not None:
            self.raw_request = raw_request
        if resource is not None:
            self.resource = resource
        if rule_name is not None:
            self.rule_name = rule_name
        if time is not None:
            self.time = time
        if user_groups is not None:
            self.user_groups = user_groups
        if user_uid is not None:
            self.user_uid = user_uid
        if username is not None:
            self.username = username

    @property
    def account_id(self):
        """Gets the account_id of this AdmissionAudit.  # noqa: E501

        AccountID is the cloud account ID.   # noqa: E501

        :return: The account_id of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AdmissionAudit.

        AccountID is the cloud account ID.   # noqa: E501

        :param account_id: The account_id of this AdmissionAudit.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def attack_techniques(self):
        """Gets the attack_techniques of this AdmissionAudit.  # noqa: E501

        AttackTechniques are the MITRE attack techniques.   # noqa: E501

        :return: The attack_techniques of this AdmissionAudit.  # noqa: E501
        :rtype: list[MitreTechnique]
        """
        return self._attack_techniques

    @attack_techniques.setter
    def attack_techniques(self, attack_techniques):
        """Sets the attack_techniques of this AdmissionAudit.

        AttackTechniques are the MITRE attack techniques.   # noqa: E501

        :param attack_techniques: The attack_techniques of this AdmissionAudit.  # noqa: E501
        :type attack_techniques: list[MitreTechnique]
        """

        self._attack_techniques = attack_techniques

    @property
    def cluster(self):
        """Gets the cluster of this AdmissionAudit.  # noqa: E501

        Cluster is the cluster where the audit took place.   # noqa: E501

        :return: The cluster of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this AdmissionAudit.

        Cluster is the cluster where the audit took place.   # noqa: E501

        :param cluster: The cluster of this AdmissionAudit.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def collections(self):
        """Gets the collections of this AdmissionAudit.  # noqa: E501

        Collections are collections to which this audit applies.   # noqa: E501

        :return: The collections of this AdmissionAudit.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this AdmissionAudit.

        Collections are collections to which this audit applies.   # noqa: E501

        :param collections: The collections of this AdmissionAudit.  # noqa: E501
        :type collections: list[str]
        """

        self._collections = collections

    @property
    def effect(self):
        """Gets the effect of this AdmissionAudit.  # noqa: E501

        Effect is the rule effect which was applied to the review which led to this audit.   # noqa: E501

        :return: The effect of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this AdmissionAudit.

        Effect is the rule effect which was applied to the review which led to this audit.   # noqa: E501

        :param effect: The effect of this AdmissionAudit.  # noqa: E501
        :type effect: str
        """

        self._effect = effect

    @property
    def kind(self):
        """Gets the kind of this AdmissionAudit.  # noqa: E501

        Kind is the type of object being manipulated. For example: Pod.   # noqa: E501

        :return: The kind of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AdmissionAudit.

        Kind is the type of object being manipulated. For example: Pod.   # noqa: E501

        :param kind: The kind of this AdmissionAudit.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def message(self):
        """Gets the message of this AdmissionAudit.  # noqa: E501

        Message is the rule user defined message which appears on audit.   # noqa: E501

        :return: The message of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AdmissionAudit.

        Message is the rule user defined message which appears on audit.   # noqa: E501

        :param message: The message of this AdmissionAudit.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def namespace(self):
        """Gets the namespace of this AdmissionAudit.  # noqa: E501

        Namespace is the namespace associated with the request (if any).   # noqa: E501

        :return: The namespace of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AdmissionAudit.

        Namespace is the namespace associated with the request (if any).   # noqa: E501

        :param namespace: The namespace of this AdmissionAudit.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def operation(self):
        """Gets the operation of this AdmissionAudit.  # noqa: E501

        Operation is the operation being performed.   # noqa: E501

        :return: The operation of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AdmissionAudit.

        Operation is the operation being performed.   # noqa: E501

        :param operation: The operation of this AdmissionAudit.  # noqa: E501
        :type operation: str
        """

        self._operation = operation

    @property
    def raw_request(self):
        """Gets the raw_request of this AdmissionAudit.  # noqa: E501

        RawRequest is the original review request that caused this audit.   # noqa: E501

        :return: The raw_request of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._raw_request

    @raw_request.setter
    def raw_request(self, raw_request):
        """Sets the raw_request of this AdmissionAudit.

        RawRequest is the original review request that caused this audit.   # noqa: E501

        :param raw_request: The raw_request of this AdmissionAudit.  # noqa: E501
        :type raw_request: str
        """

        self._raw_request = raw_request

    @property
    def resource(self):
        """Gets the resource of this AdmissionAudit.  # noqa: E501

        Resource is the name of the resource being requested.  This is not the kind.  For example: pods.   # noqa: E501

        :return: The resource of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AdmissionAudit.

        Resource is the name of the resource being requested.  This is not the kind.  For example: pods.   # noqa: E501

        :param resource: The resource of this AdmissionAudit.  # noqa: E501
        :type resource: str
        """

        self._resource = resource

    @property
    def rule_name(self):
        """Gets the rule_name of this AdmissionAudit.  # noqa: E501

        RuleName is the name of the rule which issued this audit.   # noqa: E501

        :return: The rule_name of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this AdmissionAudit.

        RuleName is the name of the rule which issued this audit.   # noqa: E501

        :param rule_name: The rule_name of this AdmissionAudit.  # noqa: E501
        :type rule_name: str
        """

        self._rule_name = rule_name

    @property
    def time(self):
        """Gets the time of this AdmissionAudit.  # noqa: E501

        Time is the time at which the audit was generated.   # noqa: E501

        :return: The time of this AdmissionAudit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AdmissionAudit.

        Time is the time at which the audit was generated.   # noqa: E501

        :param time: The time of this AdmissionAudit.  # noqa: E501
        :type time: datetime
        """

        self._time = time

    @property
    def user_groups(self):
        """Gets the user_groups of this AdmissionAudit.  # noqa: E501

        UserGroups is the names of groups this user is a part of.   # noqa: E501

        :return: The user_groups of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this AdmissionAudit.

        UserGroups is the names of groups this user is a part of.   # noqa: E501

        :param user_groups: The user_groups of this AdmissionAudit.  # noqa: E501
        :type user_groups: str
        """

        self._user_groups = user_groups

    @property
    def user_uid(self):
        """Gets the user_uid of this AdmissionAudit.  # noqa: E501

        UserUID is a unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.   # noqa: E501

        :return: The user_uid of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._user_uid

    @user_uid.setter
    def user_uid(self, user_uid):
        """Sets the user_uid of this AdmissionAudit.

        UserUID is a unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.   # noqa: E501

        :param user_uid: The user_uid of this AdmissionAudit.  # noqa: E501
        :type user_uid: str
        """

        self._user_uid = user_uid

    @property
    def username(self):
        """Gets the username of this AdmissionAudit.  # noqa: E501

        Username is the name that uniquely identifies this user among all active users.   # noqa: E501

        :return: The username of this AdmissionAudit.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AdmissionAudit.

        Username is the name that uniquely identifies this user among all active users.   # noqa: E501

        :param username: The username of this AdmissionAudit.  # noqa: E501
        :type username: str
        """

        self._username = username

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
        if not isinstance(other, AdmissionAudit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdmissionAudit):
            return True

        return self.to_dict() != other.to_dict()
