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


class SharedCloudDiscoveryEntity(object):
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
        'active_services_count': 'int',
        'arn': 'str',
        'container_group': 'str',
        'created_at': 'datetime',
        'defended': 'bool',
        'image': 'str',
        'last_modified': 'datetime',
        'name': 'str',
        'nodes_count': 'int',
        'resource_group': 'str',
        'running_tasks_count': 'int',
        'runtime': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'active_services_count': 'activeServicesCount',
        'arn': 'arn',
        'container_group': 'containerGroup',
        'created_at': 'createdAt',
        'defended': 'defended',
        'image': 'image',
        'last_modified': 'lastModified',
        'name': 'name',
        'nodes_count': 'nodesCount',
        'resource_group': 'resourceGroup',
        'running_tasks_count': 'runningTasksCount',
        'runtime': 'runtime',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, active_services_count=None, arn=None, container_group=None, created_at=None, defended=None, image=None, last_modified=None, name=None, nodes_count=None, resource_group=None, running_tasks_count=None, runtime=None, status=None, version=None, local_vars_configuration=None):  # noqa: E501
        """SharedCloudDiscoveryEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active_services_count = None
        self._arn = None
        self._container_group = None
        self._created_at = None
        self._defended = None
        self._image = None
        self._last_modified = None
        self._name = None
        self._nodes_count = None
        self._resource_group = None
        self._running_tasks_count = None
        self._runtime = None
        self._status = None
        self._version = None
        self.discriminator = None

        if active_services_count is not None:
            self.active_services_count = active_services_count
        if arn is not None:
            self.arn = arn
        if container_group is not None:
            self.container_group = container_group
        if created_at is not None:
            self.created_at = created_at
        if defended is not None:
            self.defended = defended
        if image is not None:
            self.image = image
        if last_modified is not None:
            self.last_modified = last_modified
        if name is not None:
            self.name = name
        if nodes_count is not None:
            self.nodes_count = nodes_count
        if resource_group is not None:
            self.resource_group = resource_group
        if running_tasks_count is not None:
            self.running_tasks_count = running_tasks_count
        if runtime is not None:
            self.runtime = runtime
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def active_services_count(self):
        """Gets the active_services_count of this SharedCloudDiscoveryEntity.  # noqa: E501

        ActiveServicesCount is the number of active services in ecs cluster.   # noqa: E501

        :return: The active_services_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: int
        """
        return self._active_services_count

    @active_services_count.setter
    def active_services_count(self, active_services_count):
        """Sets the active_services_count of this SharedCloudDiscoveryEntity.

        ActiveServicesCount is the number of active services in ecs cluster.   # noqa: E501

        :param active_services_count: The active_services_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type active_services_count: int
        """

        self._active_services_count = active_services_count

    @property
    def arn(self):
        """Gets the arn of this SharedCloudDiscoveryEntity.  # noqa: E501

        The Amazon Resource Name (ARN) assigned to the entity.   # noqa: E501

        :return: The arn of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """Sets the arn of this SharedCloudDiscoveryEntity.

        The Amazon Resource Name (ARN) assigned to the entity.   # noqa: E501

        :param arn: The arn of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type arn: str
        """

        self._arn = arn

    @property
    def container_group(self):
        """Gets the container_group of this SharedCloudDiscoveryEntity.  # noqa: E501

        ContainerGroup is the azure aci container group the container belongs to.   # noqa: E501

        :return: The container_group of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._container_group

    @container_group.setter
    def container_group(self, container_group):
        """Sets the container_group of this SharedCloudDiscoveryEntity.

        ContainerGroup is the azure aci container group the container belongs to.   # noqa: E501

        :param container_group: The container_group of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type container_group: str
        """

        self._container_group = container_group

    @property
    def created_at(self):
        """Gets the created_at of this SharedCloudDiscoveryEntity.  # noqa: E501

        CreatedAt is the time when the entity was created.   # noqa: E501

        :return: The created_at of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SharedCloudDiscoveryEntity.

        CreatedAt is the time when the entity was created.   # noqa: E501

        :param created_at: The created_at of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def defended(self):
        """Gets the defended of this SharedCloudDiscoveryEntity.  # noqa: E501

        Defended indicates if the entity is defended.   # noqa: E501

        :return: The defended of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: bool
        """
        return self._defended

    @defended.setter
    def defended(self, defended):
        """Sets the defended of this SharedCloudDiscoveryEntity.

        Defended indicates if the entity is defended.   # noqa: E501

        :param defended: The defended of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type defended: bool
        """

        self._defended = defended

    @property
    def image(self):
        """Gets the image of this SharedCloudDiscoveryEntity.  # noqa: E501

        Image is the image of an aci container.   # noqa: E501

        :return: The image of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SharedCloudDiscoveryEntity.

        Image is the image of an aci container.   # noqa: E501

        :param image: The image of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def last_modified(self):
        """Gets the last_modified of this SharedCloudDiscoveryEntity.  # noqa: E501

        LastModified is the modification time of the function.   # noqa: E501

        :return: The last_modified of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this SharedCloudDiscoveryEntity.

        LastModified is the modification time of the function.   # noqa: E501

        :param last_modified: The last_modified of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type last_modified: datetime
        """

        self._last_modified = last_modified

    @property
    def name(self):
        """Gets the name of this SharedCloudDiscoveryEntity.  # noqa: E501

        Name is the name of the entity.   # noqa: E501

        :return: The name of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedCloudDiscoveryEntity.

        Name is the name of the entity.   # noqa: E501

        :param name: The name of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def nodes_count(self):
        """Gets the nodes_count of this SharedCloudDiscoveryEntity.  # noqa: E501

        NodesCount is the number of nodes in the cluster (aks, gke).   # noqa: E501

        :return: The nodes_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: int
        """
        return self._nodes_count

    @nodes_count.setter
    def nodes_count(self, nodes_count):
        """Sets the nodes_count of this SharedCloudDiscoveryEntity.

        NodesCount is the number of nodes in the cluster (aks, gke).   # noqa: E501

        :param nodes_count: The nodes_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type nodes_count: int
        """

        self._nodes_count = nodes_count

    @property
    def resource_group(self):
        """Gets the resource_group of this SharedCloudDiscoveryEntity.  # noqa: E501

        ResourceGroup is the the azure resource group containing the entity.   # noqa: E501

        :return: The resource_group of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this SharedCloudDiscoveryEntity.

        ResourceGroup is the the azure resource group containing the entity.   # noqa: E501

        :param resource_group: The resource_group of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type resource_group: str
        """

        self._resource_group = resource_group

    @property
    def running_tasks_count(self):
        """Gets the running_tasks_count of this SharedCloudDiscoveryEntity.  # noqa: E501

        RunningTasksCount is the number of running tasks in ecs cluster.   # noqa: E501

        :return: The running_tasks_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: int
        """
        return self._running_tasks_count

    @running_tasks_count.setter
    def running_tasks_count(self, running_tasks_count):
        """Sets the running_tasks_count of this SharedCloudDiscoveryEntity.

        RunningTasksCount is the number of running tasks in ecs cluster.   # noqa: E501

        :param running_tasks_count: The running_tasks_count of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type running_tasks_count: int
        """

        self._running_tasks_count = running_tasks_count

    @property
    def runtime(self):
        """Gets the runtime of this SharedCloudDiscoveryEntity.  # noqa: E501

        Runtime is runtime environment for the function, i.e. nodejs.   # noqa: E501

        :return: The runtime of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this SharedCloudDiscoveryEntity.

        Runtime is runtime environment for the function, i.e. nodejs.   # noqa: E501

        :param runtime: The runtime of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type runtime: str
        """

        self._runtime = runtime

    @property
    def status(self):
        """Gets the status of this SharedCloudDiscoveryEntity.  # noqa: E501

        Status is the current status of entity.   # noqa: E501

        :return: The status of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SharedCloudDiscoveryEntity.

        Status is the current status of entity.   # noqa: E501

        :param status: The status of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this SharedCloudDiscoveryEntity.  # noqa: E501

        Version is the version of the entity.   # noqa: E501

        :return: The version of this SharedCloudDiscoveryEntity.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SharedCloudDiscoveryEntity.

        Version is the version of the entity.   # noqa: E501

        :param version: The version of this SharedCloudDiscoveryEntity.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, SharedCloudDiscoveryEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedCloudDiscoveryEntity):
            return True

        return self.to_dict() != other.to_dict()
