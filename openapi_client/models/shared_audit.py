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


class SharedAudit(object):
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
        'allow': 'bool',
        'api': 'str',
        'cluster': 'str',
        'collections': 'list[str]',
        'container_name': 'str',
        'fqdn': 'str',
        'hostname': 'str',
        'image_name': 'str',
        'labels': 'dict(str, str)',
        'msg': 'str',
        'rule_name': 'str',
        'source_ip': 'str',
        'time': 'datetime',
        'type': 'str',
        'user': 'str'
    }

    attribute_map = {
        'account_id': 'accountID',
        'allow': 'allow',
        'api': 'api',
        'cluster': 'cluster',
        'collections': 'collections',
        'container_name': 'containerName',
        'fqdn': 'fqdn',
        'hostname': 'hostname',
        'image_name': 'imageName',
        'labels': 'labels',
        'msg': 'msg',
        'rule_name': 'ruleName',
        'source_ip': 'sourceIP',
        'time': 'time',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, account_id=None, allow=None, api=None, cluster=None, collections=None, container_name=None, fqdn=None, hostname=None, image_name=None, labels=None, msg=None, rule_name=None, source_ip=None, time=None, type=None, user=None, local_vars_configuration=None):  # noqa: E501
        """SharedAudit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._allow = None
        self._api = None
        self._cluster = None
        self._collections = None
        self._container_name = None
        self._fqdn = None
        self._hostname = None
        self._image_name = None
        self._labels = None
        self._msg = None
        self._rule_name = None
        self._source_ip = None
        self._time = None
        self._type = None
        self._user = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if allow is not None:
            self.allow = allow
        if api is not None:
            self.api = api
        if cluster is not None:
            self.cluster = cluster
        if collections is not None:
            self.collections = collections
        if container_name is not None:
            self.container_name = container_name
        if fqdn is not None:
            self.fqdn = fqdn
        if hostname is not None:
            self.hostname = hostname
        if image_name is not None:
            self.image_name = image_name
        if labels is not None:
            self.labels = labels
        if msg is not None:
            self.msg = msg
        if rule_name is not None:
            self.rule_name = rule_name
        if source_ip is not None:
            self.source_ip = source_ip
        if time is not None:
            self.time = time
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def account_id(self):
        """Gets the account_id of this SharedAudit.  # noqa: E501

        AccountID is the cloud account ID where the audit was created.   # noqa: E501

        :return: The account_id of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SharedAudit.

        AccountID is the cloud account ID where the audit was created.   # noqa: E501

        :param account_id: The account_id of this SharedAudit.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def allow(self):
        """Gets the allow of this SharedAudit.  # noqa: E501

        Allow indicates whether the command was allowe or denied.   # noqa: E501

        :return: The allow of this SharedAudit.  # noqa: E501
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this SharedAudit.

        Allow indicates whether the command was allowe or denied.   # noqa: E501

        :param allow: The allow of this SharedAudit.  # noqa: E501
        :type allow: bool
        """

        self._allow = allow

    @property
    def api(self):
        """Gets the api of this SharedAudit.  # noqa: E501

        API is the api that is being audited.   # noqa: E501

        :return: The api of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this SharedAudit.

        API is the api that is being audited.   # noqa: E501

        :param api: The api of this SharedAudit.  # noqa: E501
        :type api: str
        """

        self._api = api

    @property
    def cluster(self):
        """Gets the cluster of this SharedAudit.  # noqa: E501

        Cluster is the cluster from which the audit originated.   # noqa: E501

        :return: The cluster of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SharedAudit.

        Cluster is the cluster from which the audit originated.   # noqa: E501

        :param cluster: The cluster of this SharedAudit.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def collections(self):
        """Gets the collections of this SharedAudit.  # noqa: E501

        Collections are collections to which this audit applies.   # noqa: E501

        :return: The collections of this SharedAudit.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this SharedAudit.

        Collections are collections to which this audit applies.   # noqa: E501

        :param collections: The collections of this SharedAudit.  # noqa: E501
        :type collections: list[str]
        """

        self._collections = collections

    @property
    def container_name(self):
        """Gets the container_name of this SharedAudit.  # noqa: E501

        ContainerName is the name of the container.   # noqa: E501

        :return: The container_name of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this SharedAudit.

        ContainerName is the name of the container.   # noqa: E501

        :param container_name: The container_name of this SharedAudit.  # noqa: E501
        :type container_name: str
        """

        self._container_name = container_name

    @property
    def fqdn(self):
        """Gets the fqdn of this SharedAudit.  # noqa: E501

        FQDN is the fully qualified domain name from which the audit originated.   # noqa: E501

        :return: The fqdn of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this SharedAudit.

        FQDN is the fully qualified domain name from which the audit originated.   # noqa: E501

        :param fqdn: The fqdn of this SharedAudit.  # noqa: E501
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def hostname(self):
        """Gets the hostname of this SharedAudit.  # noqa: E501

        Hostname is the hostname from which the audit originated.   # noqa: E501

        :return: The hostname of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SharedAudit.

        Hostname is the hostname from which the audit originated.   # noqa: E501

        :param hostname: The hostname of this SharedAudit.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def image_name(self):
        """Gets the image_name of this SharedAudit.  # noqa: E501

        ImageName is the name of the image.   # noqa: E501

        :return: The image_name of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this SharedAudit.

        ImageName is the name of the image.   # noqa: E501

        :param image_name: The image_name of this SharedAudit.  # noqa: E501
        :type image_name: str
        """

        self._image_name = image_name

    @property
    def labels(self):
        """Gets the labels of this SharedAudit.  # noqa: E501

        Labels are the labels associated with the target audit (for containers/images).   # noqa: E501

        :return: The labels of this SharedAudit.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SharedAudit.

        Labels are the labels associated with the target audit (for containers/images).   # noqa: E501

        :param labels: The labels of this SharedAudit.  # noqa: E501
        :type labels: dict(str, str)
        """

        self._labels = labels

    @property
    def msg(self):
        """Gets the msg of this SharedAudit.  # noqa: E501

        Msg is the message explaining the audit.   # noqa: E501

        :return: The msg of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SharedAudit.

        Msg is the message explaining the audit.   # noqa: E501

        :param msg: The msg of this SharedAudit.  # noqa: E501
        :type msg: str
        """

        self._msg = msg

    @property
    def rule_name(self):
        """Gets the rule_name of this SharedAudit.  # noqa: E501

        RulesName is contains the name of the rule that was applied, when blocked.   # noqa: E501

        :return: The rule_name of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this SharedAudit.

        RulesName is contains the name of the rule that was applied, when blocked.   # noqa: E501

        :param rule_name: The rule_name of this SharedAudit.  # noqa: E501
        :type rule_name: str
        """

        self._rule_name = rule_name

    @property
    def source_ip(self):
        """Gets the source_ip of this SharedAudit.  # noqa: E501

        SourceIP is the remote agent's source IP.   # noqa: E501

        :return: The source_ip of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this SharedAudit.

        SourceIP is the remote agent's source IP.   # noqa: E501

        :param source_ip: The source_ip of this SharedAudit.  # noqa: E501
        :type source_ip: str
        """

        self._source_ip = source_ip

    @property
    def time(self):
        """Gets the time of this SharedAudit.  # noqa: E501

        Time is the UTC time of the audit event.   # noqa: E501

        :return: The time of this SharedAudit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SharedAudit.

        Time is the UTC time of the audit event.   # noqa: E501

        :param time: The time of this SharedAudit.  # noqa: E501
        :type time: datetime
        """

        self._time = time

    @property
    def type(self):
        """Gets the type of this SharedAudit.  # noqa: E501

        Type is the audit type.   # noqa: E501

        :return: The type of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SharedAudit.

        Type is the audit type.   # noqa: E501

        :param type: The type of this SharedAudit.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this SharedAudit.  # noqa: E501

        User is the user that run the command.   # noqa: E501

        :return: The user of this SharedAudit.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SharedAudit.

        User is the user that run the command.   # noqa: E501

        :param user: The user of this SharedAudit.  # noqa: E501
        :type user: str
        """

        self._user = user

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
        if not isinstance(other, SharedAudit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedAudit):
            return True

        return self.to_dict() != other.to_dict()
