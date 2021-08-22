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


class SharedContainerInfo(object):
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
        'all_compliance': 'VulnAllCompliance',
        'app': 'str',
        'cloud_metadata': 'CommonCloudMetadata',
        'cluster': 'str',
        'compliance_distribution': 'VulnDistribution',
        'compliance_issues': 'list[VulnVulnerability]',
        'compliance_issues_count': 'int',
        'compliance_risk_score': 'float',
        'external_labels': 'list[CommonExternalLabel]',
        'id': 'str',
        'image': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'infra': 'bool',
        'installed_products': 'SharedInstalledProducts',
        'labels': 'list[str]',
        'name': 'str',
        'namespace': 'str',
        'network': 'SharedContainerNetwork',
        'network_settings': 'SharedDockerNetworkInfo',
        'processes': 'list[SharedContainerProcess]',
        'profile_id': 'str',
        'size_bytes': 'int'
    }

    attribute_map = {
        'all_compliance': 'allCompliance',
        'app': 'app',
        'cloud_metadata': 'cloudMetadata',
        'cluster': 'cluster',
        'compliance_distribution': 'complianceDistribution',
        'compliance_issues': 'complianceIssues',
        'compliance_issues_count': 'complianceIssuesCount',
        'compliance_risk_score': 'complianceRiskScore',
        'external_labels': 'externalLabels',
        'id': 'id',
        'image': 'image',
        'image_id': 'imageID',
        'image_name': 'imageName',
        'infra': 'infra',
        'installed_products': 'installedProducts',
        'labels': 'labels',
        'name': 'name',
        'namespace': 'namespace',
        'network': 'network',
        'network_settings': 'networkSettings',
        'processes': 'processes',
        'profile_id': 'profileID',
        'size_bytes': 'sizeBytes'
    }

    def __init__(self, all_compliance=None, app=None, cloud_metadata=None, cluster=None, compliance_distribution=None, compliance_issues=None, compliance_issues_count=None, compliance_risk_score=None, external_labels=None, id=None, image=None, image_id=None, image_name=None, infra=None, installed_products=None, labels=None, name=None, namespace=None, network=None, network_settings=None, processes=None, profile_id=None, size_bytes=None, local_vars_configuration=None):  # noqa: E501
        """SharedContainerInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._all_compliance = None
        self._app = None
        self._cloud_metadata = None
        self._cluster = None
        self._compliance_distribution = None
        self._compliance_issues = None
        self._compliance_issues_count = None
        self._compliance_risk_score = None
        self._external_labels = None
        self._id = None
        self._image = None
        self._image_id = None
        self._image_name = None
        self._infra = None
        self._installed_products = None
        self._labels = None
        self._name = None
        self._namespace = None
        self._network = None
        self._network_settings = None
        self._processes = None
        self._profile_id = None
        self._size_bytes = None
        self.discriminator = None

        if all_compliance is not None:
            self.all_compliance = all_compliance
        if app is not None:
            self.app = app
        if cloud_metadata is not None:
            self.cloud_metadata = cloud_metadata
        if cluster is not None:
            self.cluster = cluster
        if compliance_distribution is not None:
            self.compliance_distribution = compliance_distribution
        if compliance_issues is not None:
            self.compliance_issues = compliance_issues
        if compliance_issues_count is not None:
            self.compliance_issues_count = compliance_issues_count
        if compliance_risk_score is not None:
            self.compliance_risk_score = compliance_risk_score
        if external_labels is not None:
            self.external_labels = external_labels
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if infra is not None:
            self.infra = infra
        if installed_products is not None:
            self.installed_products = installed_products
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if network is not None:
            self.network = network
        if network_settings is not None:
            self.network_settings = network_settings
        if processes is not None:
            self.processes = processes
        if profile_id is not None:
            self.profile_id = profile_id
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def all_compliance(self):
        """Gets the all_compliance of this SharedContainerInfo.  # noqa: E501


        :return: The all_compliance of this SharedContainerInfo.  # noqa: E501
        :rtype: VulnAllCompliance
        """
        return self._all_compliance

    @all_compliance.setter
    def all_compliance(self, all_compliance):
        """Sets the all_compliance of this SharedContainerInfo.


        :param all_compliance: The all_compliance of this SharedContainerInfo.  # noqa: E501
        :type all_compliance: VulnAllCompliance
        """

        self._all_compliance = all_compliance

    @property
    def app(self):
        """Gets the app of this SharedContainerInfo.  # noqa: E501

        App is the app that is hosted in the container.   # noqa: E501

        :return: The app of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this SharedContainerInfo.

        App is the app that is hosted in the container.   # noqa: E501

        :param app: The app of this SharedContainerInfo.  # noqa: E501
        :type app: str
        """

        self._app = app

    @property
    def cloud_metadata(self):
        """Gets the cloud_metadata of this SharedContainerInfo.  # noqa: E501


        :return: The cloud_metadata of this SharedContainerInfo.  # noqa: E501
        :rtype: CommonCloudMetadata
        """
        return self._cloud_metadata

    @cloud_metadata.setter
    def cloud_metadata(self, cloud_metadata):
        """Sets the cloud_metadata of this SharedContainerInfo.


        :param cloud_metadata: The cloud_metadata of this SharedContainerInfo.  # noqa: E501
        :type cloud_metadata: CommonCloudMetadata
        """

        self._cloud_metadata = cloud_metadata

    @property
    def cluster(self):
        """Gets the cluster of this SharedContainerInfo.  # noqa: E501

        Cluster is the provided cluster name.   # noqa: E501

        :return: The cluster of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SharedContainerInfo.

        Cluster is the provided cluster name.   # noqa: E501

        :param cluster: The cluster of this SharedContainerInfo.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def compliance_distribution(self):
        """Gets the compliance_distribution of this SharedContainerInfo.  # noqa: E501


        :return: The compliance_distribution of this SharedContainerInfo.  # noqa: E501
        :rtype: VulnDistribution
        """
        return self._compliance_distribution

    @compliance_distribution.setter
    def compliance_distribution(self, compliance_distribution):
        """Sets the compliance_distribution of this SharedContainerInfo.


        :param compliance_distribution: The compliance_distribution of this SharedContainerInfo.  # noqa: E501
        :type compliance_distribution: VulnDistribution
        """

        self._compliance_distribution = compliance_distribution

    @property
    def compliance_issues(self):
        """Gets the compliance_issues of this SharedContainerInfo.  # noqa: E501

        ComplianceIssues are all the container compliance issues.   # noqa: E501

        :return: The compliance_issues of this SharedContainerInfo.  # noqa: E501
        :rtype: list[VulnVulnerability]
        """
        return self._compliance_issues

    @compliance_issues.setter
    def compliance_issues(self, compliance_issues):
        """Sets the compliance_issues of this SharedContainerInfo.

        ComplianceIssues are all the container compliance issues.   # noqa: E501

        :param compliance_issues: The compliance_issues of this SharedContainerInfo.  # noqa: E501
        :type compliance_issues: list[VulnVulnerability]
        """

        self._compliance_issues = compliance_issues

    @property
    def compliance_issues_count(self):
        """Gets the compliance_issues_count of this SharedContainerInfo.  # noqa: E501

        .   # noqa: E501

        :return: The compliance_issues_count of this SharedContainerInfo.  # noqa: E501
        :rtype: int
        """
        return self._compliance_issues_count

    @compliance_issues_count.setter
    def compliance_issues_count(self, compliance_issues_count):
        """Sets the compliance_issues_count of this SharedContainerInfo.

        .   # noqa: E501

        :param compliance_issues_count: The compliance_issues_count of this SharedContainerInfo.  # noqa: E501
        :type compliance_issues_count: int
        """

        self._compliance_issues_count = compliance_issues_count

    @property
    def compliance_risk_score(self):
        """Gets the compliance_risk_score of this SharedContainerInfo.  # noqa: E501

        ComplianceRiskScore is the container's compliance risk score.   # noqa: E501

        :return: The compliance_risk_score of this SharedContainerInfo.  # noqa: E501
        :rtype: float
        """
        return self._compliance_risk_score

    @compliance_risk_score.setter
    def compliance_risk_score(self, compliance_risk_score):
        """Sets the compliance_risk_score of this SharedContainerInfo.

        ComplianceRiskScore is the container's compliance risk score.   # noqa: E501

        :param compliance_risk_score: The compliance_risk_score of this SharedContainerInfo.  # noqa: E501
        :type compliance_risk_score: float
        """

        self._compliance_risk_score = compliance_risk_score

    @property
    def external_labels(self):
        """Gets the external_labels of this SharedContainerInfo.  # noqa: E501

        ExternalLabels is the external labels e.g., kubernetes namespace labels.   # noqa: E501

        :return: The external_labels of this SharedContainerInfo.  # noqa: E501
        :rtype: list[CommonExternalLabel]
        """
        return self._external_labels

    @external_labels.setter
    def external_labels(self, external_labels):
        """Sets the external_labels of this SharedContainerInfo.

        ExternalLabels is the external labels e.g., kubernetes namespace labels.   # noqa: E501

        :param external_labels: The external_labels of this SharedContainerInfo.  # noqa: E501
        :type external_labels: list[CommonExternalLabel]
        """

        self._external_labels = external_labels

    @property
    def id(self):
        """Gets the id of this SharedContainerInfo.  # noqa: E501

        Id is the container id.   # noqa: E501

        :return: The id of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedContainerInfo.

        Id is the container id.   # noqa: E501

        :param id: The id of this SharedContainerInfo.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this SharedContainerInfo.  # noqa: E501

        Image is the canonical image name.   # noqa: E501

        :return: The image of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this SharedContainerInfo.

        Image is the canonical image name.   # noqa: E501

        :param image: The image of this SharedContainerInfo.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def image_id(self):
        """Gets the image_id of this SharedContainerInfo.  # noqa: E501

        ImageId is the image id.   # noqa: E501

        :return: The image_id of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this SharedContainerInfo.

        ImageId is the image id.   # noqa: E501

        :param image_id: The image_id of this SharedContainerInfo.  # noqa: E501
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this SharedContainerInfo.  # noqa: E501

        Deprecated: The image name as stated in the docker run command.   # noqa: E501

        :return: The image_name of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this SharedContainerInfo.

        Deprecated: The image name as stated in the docker run command.   # noqa: E501

        :param image_name: The image_name of this SharedContainerInfo.  # noqa: E501
        :type image_name: str
        """

        self._image_name = image_name

    @property
    def infra(self):
        """Gets the infra of this SharedContainerInfo.  # noqa: E501

        Infra represents any container that belongs to the infrastructure.   # noqa: E501

        :return: The infra of this SharedContainerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._infra

    @infra.setter
    def infra(self, infra):
        """Sets the infra of this SharedContainerInfo.

        Infra represents any container that belongs to the infrastructure.   # noqa: E501

        :param infra: The infra of this SharedContainerInfo.  # noqa: E501
        :type infra: bool
        """

        self._infra = infra

    @property
    def installed_products(self):
        """Gets the installed_products of this SharedContainerInfo.  # noqa: E501


        :return: The installed_products of this SharedContainerInfo.  # noqa: E501
        :rtype: SharedInstalledProducts
        """
        return self._installed_products

    @installed_products.setter
    def installed_products(self, installed_products):
        """Sets the installed_products of this SharedContainerInfo.


        :param installed_products: The installed_products of this SharedContainerInfo.  # noqa: E501
        :type installed_products: SharedInstalledProducts
        """

        self._installed_products = installed_products

    @property
    def labels(self):
        """Gets the labels of this SharedContainerInfo.  # noqa: E501

        Labels are the container labels (https://docs.docker.com/engine/userguide/labels-custom-metadata/).   # noqa: E501

        :return: The labels of this SharedContainerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SharedContainerInfo.

        Labels are the container labels (https://docs.docker.com/engine/userguide/labels-custom-metadata/).   # noqa: E501

        :param labels: The labels of this SharedContainerInfo.  # noqa: E501
        :type labels: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this SharedContainerInfo.  # noqa: E501

        Name is the container name.   # noqa: E501

        :return: The name of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedContainerInfo.

        Name is the container name.   # noqa: E501

        :param name: The name of this SharedContainerInfo.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this SharedContainerInfo.  # noqa: E501

        Namespace is the k8s deployment namespace.   # noqa: E501

        :return: The namespace of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SharedContainerInfo.

        Namespace is the k8s deployment namespace.   # noqa: E501

        :param namespace: The namespace of this SharedContainerInfo.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def network(self):
        """Gets the network of this SharedContainerInfo.  # noqa: E501


        :return: The network of this SharedContainerInfo.  # noqa: E501
        :rtype: SharedContainerNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this SharedContainerInfo.


        :param network: The network of this SharedContainerInfo.  # noqa: E501
        :type network: SharedContainerNetwork
        """

        self._network = network

    @property
    def network_settings(self):
        """Gets the network_settings of this SharedContainerInfo.  # noqa: E501


        :return: The network_settings of this SharedContainerInfo.  # noqa: E501
        :rtype: SharedDockerNetworkInfo
        """
        return self._network_settings

    @network_settings.setter
    def network_settings(self, network_settings):
        """Sets the network_settings of this SharedContainerInfo.


        :param network_settings: The network_settings of this SharedContainerInfo.  # noqa: E501
        :type network_settings: SharedDockerNetworkInfo
        """

        self._network_settings = network_settings

    @property
    def processes(self):
        """Gets the processes of this SharedContainerInfo.  # noqa: E501

        Processes are the processes that are running inside the container.   # noqa: E501

        :return: The processes of this SharedContainerInfo.  # noqa: E501
        :rtype: list[SharedContainerProcess]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this SharedContainerInfo.

        Processes are the processes that are running inside the container.   # noqa: E501

        :param processes: The processes of this SharedContainerInfo.  # noqa: E501
        :type processes: list[SharedContainerProcess]
        """

        self._processes = processes

    @property
    def profile_id(self):
        """Gets the profile_id of this SharedContainerInfo.  # noqa: E501

        ProfileID is the container profile id.   # noqa: E501

        :return: The profile_id of this SharedContainerInfo.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this SharedContainerInfo.

        ProfileID is the container profile id.   # noqa: E501

        :param profile_id: The profile_id of this SharedContainerInfo.  # noqa: E501
        :type profile_id: str
        """

        self._profile_id = profile_id

    @property
    def size_bytes(self):
        """Gets the size_bytes of this SharedContainerInfo.  # noqa: E501

        .   # noqa: E501

        :return: The size_bytes of this SharedContainerInfo.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this SharedContainerInfo.

        .   # noqa: E501

        :param size_bytes: The size_bytes of this SharedContainerInfo.  # noqa: E501
        :type size_bytes: int
        """

        self._size_bytes = size_bytes

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
        if not isinstance(other, SharedContainerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedContainerInfo):
            return True

        return self.to_dict() != other.to_dict()
