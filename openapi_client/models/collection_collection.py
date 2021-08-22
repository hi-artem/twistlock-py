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


class CollectionCollection(object):
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
        'account_ids': 'list[str]',
        'app_ids': 'list[str]',
        'clusters': 'list[str]',
        'code_repos': 'list[str]',
        'color': 'str',
        'containers': 'list[str]',
        'description': 'str',
        'functions': 'list[str]',
        'hosts': 'list[str]',
        'images': 'list[str]',
        'labels': 'list[str]',
        'modified': 'datetime',
        'name': 'str',
        'namespaces': 'list[str]',
        'owner': 'str',
        'prisma': 'bool',
        'system': 'bool'
    }

    attribute_map = {
        'account_ids': 'accountIDs',
        'app_ids': 'appIDs',
        'clusters': 'clusters',
        'code_repos': 'codeRepos',
        'color': 'color',
        'containers': 'containers',
        'description': 'description',
        'functions': 'functions',
        'hosts': 'hosts',
        'images': 'images',
        'labels': 'labels',
        'modified': 'modified',
        'name': 'name',
        'namespaces': 'namespaces',
        'owner': 'owner',
        'prisma': 'prisma',
        'system': 'system'
    }

    def __init__(self, account_ids=None, app_ids=None, clusters=None, code_repos=None, color=None, containers=None, description=None, functions=None, hosts=None, images=None, labels=None, modified=None, name=None, namespaces=None, owner=None, prisma=None, system=None, local_vars_configuration=None):  # noqa: E501
        """CollectionCollection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_ids = None
        self._app_ids = None
        self._clusters = None
        self._code_repos = None
        self._color = None
        self._containers = None
        self._description = None
        self._functions = None
        self._hosts = None
        self._images = None
        self._labels = None
        self._modified = None
        self._name = None
        self._namespaces = None
        self._owner = None
        self._prisma = None
        self._system = None
        self.discriminator = None

        if account_ids is not None:
            self.account_ids = account_ids
        if app_ids is not None:
            self.app_ids = app_ids
        if clusters is not None:
            self.clusters = clusters
        if code_repos is not None:
            self.code_repos = code_repos
        if color is not None:
            self.color = color
        if containers is not None:
            self.containers = containers
        if description is not None:
            self.description = description
        if functions is not None:
            self.functions = functions
        if hosts is not None:
            self.hosts = hosts
        if images is not None:
            self.images = images
        if labels is not None:
            self.labels = labels
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if namespaces is not None:
            self.namespaces = namespaces
        if owner is not None:
            self.owner = owner
        if prisma is not None:
            self.prisma = prisma
        if system is not None:
            self.system = system

    @property
    def account_ids(self):
        """Gets the account_ids of this CollectionCollection.  # noqa: E501

        List of account IDs.   # noqa: E501

        :return: The account_ids of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this CollectionCollection.

        List of account IDs.   # noqa: E501

        :param account_ids: The account_ids of this CollectionCollection.  # noqa: E501
        :type account_ids: list[str]
        """

        self._account_ids = account_ids

    @property
    def app_ids(self):
        """Gets the app_ids of this CollectionCollection.  # noqa: E501

        List of application IDs.   # noqa: E501

        :return: The app_ids of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this CollectionCollection.

        List of application IDs.   # noqa: E501

        :param app_ids: The app_ids of this CollectionCollection.  # noqa: E501
        :type app_ids: list[str]
        """

        self._app_ids = app_ids

    @property
    def clusters(self):
        """Gets the clusters of this CollectionCollection.  # noqa: E501

        List of Kubernetes cluster names.   # noqa: E501

        :return: The clusters of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this CollectionCollection.

        List of Kubernetes cluster names.   # noqa: E501

        :param clusters: The clusters of this CollectionCollection.  # noqa: E501
        :type clusters: list[str]
        """

        self._clusters = clusters

    @property
    def code_repos(self):
        """Gets the code_repos of this CollectionCollection.  # noqa: E501

        List of code repositories.   # noqa: E501

        :return: The code_repos of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._code_repos

    @code_repos.setter
    def code_repos(self, code_repos):
        """Sets the code_repos of this CollectionCollection.

        List of code repositories.   # noqa: E501

        :param code_repos: The code_repos of this CollectionCollection.  # noqa: E501
        :type code_repos: list[str]
        """

        self._code_repos = code_repos

    @property
    def color(self):
        """Gets the color of this CollectionCollection.  # noqa: E501

        Color is a color code for a collection  # noqa: E501

        :return: The color of this CollectionCollection.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CollectionCollection.

        Color is a color code for a collection  # noqa: E501

        :param color: The color of this CollectionCollection.  # noqa: E501
        :type color: str
        """

        self._color = color

    @property
    def containers(self):
        """Gets the containers of this CollectionCollection.  # noqa: E501

        List of containers.   # noqa: E501

        :return: The containers of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this CollectionCollection.

        List of containers.   # noqa: E501

        :param containers: The containers of this CollectionCollection.  # noqa: E501
        :type containers: list[str]
        """

        self._containers = containers

    @property
    def description(self):
        """Gets the description of this CollectionCollection.  # noqa: E501

        Free-form text.   # noqa: E501

        :return: The description of this CollectionCollection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CollectionCollection.

        Free-form text.   # noqa: E501

        :param description: The description of this CollectionCollection.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def functions(self):
        """Gets the functions of this CollectionCollection.  # noqa: E501

        List of functions.   # noqa: E501

        :return: The functions of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this CollectionCollection.

        List of functions.   # noqa: E501

        :param functions: The functions of this CollectionCollection.  # noqa: E501
        :type functions: list[str]
        """

        self._functions = functions

    @property
    def hosts(self):
        """Gets the hosts of this CollectionCollection.  # noqa: E501

        List of  hosts.   # noqa: E501

        :return: The hosts of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this CollectionCollection.

        List of  hosts.   # noqa: E501

        :param hosts: The hosts of this CollectionCollection.  # noqa: E501
        :type hosts: list[str]
        """

        self._hosts = hosts

    @property
    def images(self):
        """Gets the images of this CollectionCollection.  # noqa: E501

        List of images.   # noqa: E501

        :return: The images of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this CollectionCollection.

        List of images.   # noqa: E501

        :param images: The images of this CollectionCollection.  # noqa: E501
        :type images: list[str]
        """

        self._images = images

    @property
    def labels(self):
        """Gets the labels of this CollectionCollection.  # noqa: E501

        List of labels.   # noqa: E501

        :return: The labels of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CollectionCollection.

        List of labels.   # noqa: E501

        :param labels: The labels of this CollectionCollection.  # noqa: E501
        :type labels: list[str]
        """

        self._labels = labels

    @property
    def modified(self):
        """Gets the modified of this CollectionCollection.  # noqa: E501

        Datetime when the collection was last modified.   # noqa: E501

        :return: The modified of this CollectionCollection.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this CollectionCollection.

        Datetime when the collection was last modified.   # noqa: E501

        :param modified: The modified of this CollectionCollection.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this CollectionCollection.  # noqa: E501

        Collection name. Must be unique.   # noqa: E501

        :return: The name of this CollectionCollection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectionCollection.

        Collection name. Must be unique.   # noqa: E501

        :param name: The name of this CollectionCollection.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def namespaces(self):
        """Gets the namespaces of this CollectionCollection.  # noqa: E501

        List of Kubernetes namespaces.   # noqa: E501

        :return: The namespaces of this CollectionCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this CollectionCollection.

        List of Kubernetes namespaces.   # noqa: E501

        :param namespaces: The namespaces of this CollectionCollection.  # noqa: E501
        :type namespaces: list[str]
        """

        self._namespaces = namespaces

    @property
    def owner(self):
        """Gets the owner of this CollectionCollection.  # noqa: E501

        User who created or last modified the collection.   # noqa: E501

        :return: The owner of this CollectionCollection.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CollectionCollection.

        User who created or last modified the collection.   # noqa: E501

        :param owner: The owner of this CollectionCollection.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def prisma(self):
        """Gets the prisma of this CollectionCollection.  # noqa: E501

        Indicates whether this collection originates from Prisma Cloud.   # noqa: E501

        :return: The prisma of this CollectionCollection.  # noqa: E501
        :rtype: bool
        """
        return self._prisma

    @prisma.setter
    def prisma(self, prisma):
        """Sets the prisma of this CollectionCollection.

        Indicates whether this collection originates from Prisma Cloud.   # noqa: E501

        :param prisma: The prisma of this CollectionCollection.  # noqa: E501
        :type prisma: bool
        """

        self._prisma = prisma

    @property
    def system(self):
        """Gets the system of this CollectionCollection.  # noqa: E501

        Indicates whether this collection was created by the system (i.e., a non user) (true) or a real user (false).   # noqa: E501

        :return: The system of this CollectionCollection.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this CollectionCollection.

        Indicates whether this collection was created by the system (i.e., a non user) (true) or a real user (false).   # noqa: E501

        :param system: The system of this CollectionCollection.  # noqa: E501
        :type system: bool
        """

        self._system = system

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
        if not isinstance(other, CollectionCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionCollection):
            return True

        return self.to_dict() != other.to_dict()
