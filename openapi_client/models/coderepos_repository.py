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


class CodereposRepository(object):
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
        'build': 'str',
        'default_branch': 'str',
        'digest': 'str',
        'full_name': 'str',
        'job_name': 'str',
        'name': 'str',
        'owner': 'str',
        'private': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'build': 'build',
        'default_branch': 'defaultBranch',
        'digest': 'digest',
        'full_name': 'fullName',
        'job_name': 'jobName',
        'name': 'name',
        'owner': 'owner',
        'private': 'private',
        'size': 'size'
    }

    def __init__(self, build=None, default_branch=None, digest=None, full_name=None, job_name=None, name=None, owner=None, private=None, size=None, local_vars_configuration=None):  # noqa: E501
        """CodereposRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._build = None
        self._default_branch = None
        self._digest = None
        self._full_name = None
        self._job_name = None
        self._name = None
        self._owner = None
        self._private = None
        self._size = None
        self.discriminator = None

        if build is not None:
            self.build = build
        if default_branch is not None:
            self.default_branch = default_branch
        if digest is not None:
            self.digest = digest
        if full_name is not None:
            self.full_name = full_name
        if job_name is not None:
            self.job_name = job_name
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if private is not None:
            self.private = private
        if size is not None:
            self.size = size

    @property
    def build(self):
        """Gets the build of this CodereposRepository.  # noqa: E501

        CI build.   # noqa: E501

        :return: The build of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this CodereposRepository.

        CI build.   # noqa: E501

        :param build: The build of this CodereposRepository.  # noqa: E501
        :type build: str
        """

        self._build = build

    @property
    def default_branch(self):
        """Gets the default_branch of this CodereposRepository.  # noqa: E501

        Default branch in the repository, usually master.   # noqa: E501

        :return: The default_branch of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this CodereposRepository.

        Default branch in the repository, usually master.   # noqa: E501

        :param default_branch: The default_branch of this CodereposRepository.  # noqa: E501
        :type default_branch: str
        """

        self._default_branch = default_branch

    @property
    def digest(self):
        """Gets the digest of this CodereposRepository.  # noqa: E501

        Repository content digest. Used to indicate if the content of the repository has changed.   # noqa: E501

        :return: The digest of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this CodereposRepository.

        Repository content digest. Used to indicate if the content of the repository has changed.   # noqa: E501

        :param digest: The digest of this CodereposRepository.  # noqa: E501
        :type digest: str
        """

        self._digest = digest

    @property
    def full_name(self):
        """Gets the full_name of this CodereposRepository.  # noqa: E501

        Full name that represents the repository (<owner>/<name>).   # noqa: E501

        :return: The full_name of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this CodereposRepository.

        Full name that represents the repository (<owner>/<name>).   # noqa: E501

        :param full_name: The full_name of this CodereposRepository.  # noqa: E501
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def job_name(self):
        """Gets the job_name of this CodereposRepository.  # noqa: E501

        CI job name.   # noqa: E501

        :return: The job_name of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CodereposRepository.

        CI job name.   # noqa: E501

        :param job_name: The job_name of this CodereposRepository.  # noqa: E501
        :type job_name: str
        """

        self._job_name = job_name

    @property
    def name(self):
        """Gets the name of this CodereposRepository.  # noqa: E501

        Repository name.   # noqa: E501

        :return: The name of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodereposRepository.

        Repository name.   # noqa: E501

        :param name: The name of this CodereposRepository.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this CodereposRepository.  # noqa: E501

        GitHub username or organization name of the repository's owner.   # noqa: E501

        :return: The owner of this CodereposRepository.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CodereposRepository.

        GitHub username or organization name of the repository's owner.   # noqa: E501

        :param owner: The owner of this CodereposRepository.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def private(self):
        """Gets the private of this CodereposRepository.  # noqa: E501

        Indicates if the repository is private (true) or not (false).   # noqa: E501

        :return: The private of this CodereposRepository.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this CodereposRepository.

        Indicates if the repository is private (true) or not (false).   # noqa: E501

        :param private: The private of this CodereposRepository.  # noqa: E501
        :type private: bool
        """

        self._private = private

    @property
    def size(self):
        """Gets the size of this CodereposRepository.  # noqa: E501

        Size of the repository (in KB).   # noqa: E501

        :return: The size of this CodereposRepository.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CodereposRepository.

        Size of the repository (in KB).   # noqa: E501

        :param size: The size of this CodereposRepository.  # noqa: E501
        :type size: int
        """

        self._size = size

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
        if not isinstance(other, CodereposRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CodereposRepository):
            return True

        return self.to_dict() != other.to_dict()
