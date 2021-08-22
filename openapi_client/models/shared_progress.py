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


class SharedProgress(object):
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
        'discovery': 'bool',
        'error': 'str',
        'hostname': 'str',
        'id': 'str',
        'scan_time': 'datetime',
        'scanned': 'int',
        'title': 'str',
        'total': 'int',
        'type': 'SharedScanType'
    }

    attribute_map = {
        'discovery': 'discovery',
        'error': 'error',
        'hostname': 'hostname',
        'id': 'id',
        'scan_time': 'scanTime',
        'scanned': 'scanned',
        'title': 'title',
        'total': 'total',
        'type': 'type'
    }

    def __init__(self, discovery=None, error=None, hostname=None, id=None, scan_time=None, scanned=None, title=None, total=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SharedProgress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._discovery = None
        self._error = None
        self._hostname = None
        self._id = None
        self._scan_time = None
        self._scanned = None
        self._title = None
        self._total = None
        self._type = None
        self.discriminator = None

        if discovery is not None:
            self.discovery = discovery
        if error is not None:
            self.error = error
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if scan_time is not None:
            self.scan_time = scan_time
        if scanned is not None:
            self.scanned = scanned
        if title is not None:
            self.title = title
        if total is not None:
            self.total = total
        if type is not None:
            self.type = type

    @property
    def discovery(self):
        """Gets the discovery of this SharedProgress.  # noqa: E501

        Discovery indicates whether the scan is in discovery phase.   # noqa: E501

        :return: The discovery of this SharedProgress.  # noqa: E501
        :rtype: bool
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this SharedProgress.

        Discovery indicates whether the scan is in discovery phase.   # noqa: E501

        :param discovery: The discovery of this SharedProgress.  # noqa: E501
        :type discovery: bool
        """

        self._discovery = discovery

    @property
    def error(self):
        """Gets the error of this SharedProgress.  # noqa: E501

        Error is the error that happened during scan.   # noqa: E501

        :return: The error of this SharedProgress.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SharedProgress.

        Error is the error that happened during scan.   # noqa: E501

        :param error: The error of this SharedProgress.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def hostname(self):
        """Gets the hostname of this SharedProgress.  # noqa: E501

        Hostname is the hostname for which the progress apply.   # noqa: E501

        :return: The hostname of this SharedProgress.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SharedProgress.

        Hostname is the hostname for which the progress apply.   # noqa: E501

        :param hostname: The hostname of this SharedProgress.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this SharedProgress.  # noqa: E501

        ID is the ID of the entity being scanned.   # noqa: E501

        :return: The id of this SharedProgress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedProgress.

        ID is the ID of the entity being scanned.   # noqa: E501

        :param id: The id of this SharedProgress.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def scan_time(self):
        """Gets the scan_time of this SharedProgress.  # noqa: E501

        ScanTime is the time of scan.   # noqa: E501

        :return: The scan_time of this SharedProgress.  # noqa: E501
        :rtype: datetime
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this SharedProgress.

        ScanTime is the time of scan.   # noqa: E501

        :param scan_time: The scan_time of this SharedProgress.  # noqa: E501
        :type scan_time: datetime
        """

        self._scan_time = scan_time

    @property
    def scanned(self):
        """Gets the scanned of this SharedProgress.  # noqa: E501

        Scanned is the number of entities for which the scan completed.   # noqa: E501

        :return: The scanned of this SharedProgress.  # noqa: E501
        :rtype: int
        """
        return self._scanned

    @scanned.setter
    def scanned(self, scanned):
        """Sets the scanned of this SharedProgress.

        Scanned is the number of entities for which the scan completed.   # noqa: E501

        :param scanned: The scanned of this SharedProgress.  # noqa: E501
        :type scanned: int
        """

        self._scanned = scanned

    @property
    def title(self):
        """Gets the title of this SharedProgress.  # noqa: E501

        Title is the progress title (set by the scanning process).   # noqa: E501

        :return: The title of this SharedProgress.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SharedProgress.

        Title is the progress title (set by the scanning process).   # noqa: E501

        :param title: The title of this SharedProgress.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def total(self):
        """Gets the total of this SharedProgress.  # noqa: E501

        Total is the total amount of entities that should be scanned.   # noqa: E501

        :return: The total of this SharedProgress.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SharedProgress.

        Total is the total amount of entities that should be scanned.   # noqa: E501

        :param total: The total of this SharedProgress.  # noqa: E501
        :type total: int
        """

        self._total = total

    @property
    def type(self):
        """Gets the type of this SharedProgress.  # noqa: E501


        :return: The type of this SharedProgress.  # noqa: E501
        :rtype: SharedScanType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SharedProgress.


        :param type: The type of this SharedProgress.  # noqa: E501
        :type type: SharedScanType
        """

        self._type = type

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
        if not isinstance(other, SharedProgress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedProgress):
            return True

        return self.to_dict() != other.to_dict()
