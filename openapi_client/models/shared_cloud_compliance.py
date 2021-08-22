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


class SharedCloudCompliance(object):
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
        'applicable_rules': 'list[str]',
        'binary_pkgs': 'list[str]',
        'block': 'bool',
        'cause': 'str',
        'collections': 'list[str]',
        'credential_id': 'str',
        'cri': 'bool',
        'custom': 'bool',
        'cve': 'str',
        'cvss': 'float',
        'description': 'str',
        'discovered': 'datetime',
        'err': 'str',
        'exploit': 'VulnExploitType',
        'fix_date': 'int',
        'fix_link': 'str',
        'function_layer': 'str',
        'grace_period_days': 'int',
        'id': 'int',
        'layer_time': 'int',
        'link': 'str',
        'package_name': 'str',
        'package_version': 'str',
        'passed': 'bool',
        'products': 'SharedInstalledProducts',
        'published': 'int',
        'risk_factors': 'dict(str, str)',
        'severity': 'str',
        'status': 'str',
        'templates': 'list[VulnComplianceTemplate]',
        'text': 'str',
        'title': 'str',
        'twistlock': 'bool',
        'type': 'VulnType',
        'vec_str': 'str',
        'vuln_tag_infos': 'list[VulnTagInfo]'
    }

    attribute_map = {
        'account_id': 'accountID',
        'applicable_rules': 'applicableRules',
        'binary_pkgs': 'binaryPkgs',
        'block': 'block',
        'cause': 'cause',
        'collections': 'collections',
        'credential_id': 'credentialId',
        'cri': 'cri',
        'custom': 'custom',
        'cve': 'cve',
        'cvss': 'cvss',
        'description': 'description',
        'discovered': 'discovered',
        'err': 'err',
        'exploit': 'exploit',
        'fix_date': 'fixDate',
        'fix_link': 'fixLink',
        'function_layer': 'functionLayer',
        'grace_period_days': 'gracePeriodDays',
        'id': 'id',
        'layer_time': 'layerTime',
        'link': 'link',
        'package_name': 'packageName',
        'package_version': 'packageVersion',
        'passed': 'passed',
        'products': 'products',
        'published': 'published',
        'risk_factors': 'riskFactors',
        'severity': 'severity',
        'status': 'status',
        'templates': 'templates',
        'text': 'text',
        'title': 'title',
        'twistlock': 'twistlock',
        'type': 'type',
        'vec_str': 'vecStr',
        'vuln_tag_infos': 'vulnTagInfos'
    }

    def __init__(self, account_id=None, applicable_rules=None, binary_pkgs=None, block=None, cause=None, collections=None, credential_id=None, cri=None, custom=None, cve=None, cvss=None, description=None, discovered=None, err=None, exploit=None, fix_date=None, fix_link=None, function_layer=None, grace_period_days=None, id=None, layer_time=None, link=None, package_name=None, package_version=None, passed=None, products=None, published=None, risk_factors=None, severity=None, status=None, templates=None, text=None, title=None, twistlock=None, type=None, vec_str=None, vuln_tag_infos=None, local_vars_configuration=None):  # noqa: E501
        """SharedCloudCompliance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._applicable_rules = None
        self._binary_pkgs = None
        self._block = None
        self._cause = None
        self._collections = None
        self._credential_id = None
        self._cri = None
        self._custom = None
        self._cve = None
        self._cvss = None
        self._description = None
        self._discovered = None
        self._err = None
        self._exploit = None
        self._fix_date = None
        self._fix_link = None
        self._function_layer = None
        self._grace_period_days = None
        self._id = None
        self._layer_time = None
        self._link = None
        self._package_name = None
        self._package_version = None
        self._passed = None
        self._products = None
        self._published = None
        self._risk_factors = None
        self._severity = None
        self._status = None
        self._templates = None
        self._text = None
        self._title = None
        self._twistlock = None
        self._type = None
        self._vec_str = None
        self._vuln_tag_infos = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if applicable_rules is not None:
            self.applicable_rules = applicable_rules
        if binary_pkgs is not None:
            self.binary_pkgs = binary_pkgs
        if block is not None:
            self.block = block
        if cause is not None:
            self.cause = cause
        if collections is not None:
            self.collections = collections
        if credential_id is not None:
            self.credential_id = credential_id
        if cri is not None:
            self.cri = cri
        if custom is not None:
            self.custom = custom
        if cve is not None:
            self.cve = cve
        if cvss is not None:
            self.cvss = cvss
        if description is not None:
            self.description = description
        if discovered is not None:
            self.discovered = discovered
        if err is not None:
            self.err = err
        if exploit is not None:
            self.exploit = exploit
        if fix_date is not None:
            self.fix_date = fix_date
        if fix_link is not None:
            self.fix_link = fix_link
        if function_layer is not None:
            self.function_layer = function_layer
        if grace_period_days is not None:
            self.grace_period_days = grace_period_days
        if id is not None:
            self.id = id
        if layer_time is not None:
            self.layer_time = layer_time
        if link is not None:
            self.link = link
        if package_name is not None:
            self.package_name = package_name
        if package_version is not None:
            self.package_version = package_version
        if passed is not None:
            self.passed = passed
        if products is not None:
            self.products = products
        if published is not None:
            self.published = published
        if risk_factors is not None:
            self.risk_factors = risk_factors
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if templates is not None:
            self.templates = templates
        if text is not None:
            self.text = text
        if title is not None:
            self.title = title
        if twistlock is not None:
            self.twistlock = twistlock
        if type is not None:
            self.type = type
        if vec_str is not None:
            self.vec_str = vec_str
        if vuln_tag_infos is not None:
            self.vuln_tag_infos = vuln_tag_infos

    @property
    def account_id(self):
        """Gets the account_id of this SharedCloudCompliance.  # noqa: E501

        AccountID is the cloud account ID.   # noqa: E501

        :return: The account_id of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SharedCloudCompliance.

        AccountID is the cloud account ID.   # noqa: E501

        :param account_id: The account_id of this SharedCloudCompliance.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def applicable_rules(self):
        """Gets the applicable_rules of this SharedCloudCompliance.  # noqa: E501

        Rules applied on the package.   # noqa: E501

        :return: The applicable_rules of this SharedCloudCompliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._applicable_rules

    @applicable_rules.setter
    def applicable_rules(self, applicable_rules):
        """Sets the applicable_rules of this SharedCloudCompliance.

        Rules applied on the package.   # noqa: E501

        :param applicable_rules: The applicable_rules of this SharedCloudCompliance.  # noqa: E501
        :type applicable_rules: list[str]
        """

        self._applicable_rules = applicable_rules

    @property
    def binary_pkgs(self):
        """Gets the binary_pkgs of this SharedCloudCompliance.  # noqa: E501

        Names of the distro binary package names (packages which are built from the source of the package).   # noqa: E501

        :return: The binary_pkgs of this SharedCloudCompliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_pkgs

    @binary_pkgs.setter
    def binary_pkgs(self, binary_pkgs):
        """Sets the binary_pkgs of this SharedCloudCompliance.

        Names of the distro binary package names (packages which are built from the source of the package).   # noqa: E501

        :param binary_pkgs: The binary_pkgs of this SharedCloudCompliance.  # noqa: E501
        :type binary_pkgs: list[str]
        """

        self._binary_pkgs = binary_pkgs

    @property
    def block(self):
        """Gets the block of this SharedCloudCompliance.  # noqa: E501

        Indicates if the vulnerability has a block effect (true) or not (false).   # noqa: E501

        :return: The block of this SharedCloudCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this SharedCloudCompliance.

        Indicates if the vulnerability has a block effect (true) or not (false).   # noqa: E501

        :param block: The block of this SharedCloudCompliance.  # noqa: E501
        :type block: bool
        """

        self._block = block

    @property
    def cause(self):
        """Gets the cause of this SharedCloudCompliance.  # noqa: E501

        Additional information regarding the root cause for the vulnerability.   # noqa: E501

        :return: The cause of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this SharedCloudCompliance.

        Additional information regarding the root cause for the vulnerability.   # noqa: E501

        :param cause: The cause of this SharedCloudCompliance.  # noqa: E501
        :type cause: str
        """

        self._cause = cause

    @property
    def collections(self):
        """Gets the collections of this SharedCloudCompliance.  # noqa: E501

        Collections are collections to which this compliance applies.   # noqa: E501

        :return: The collections of this SharedCloudCompliance.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this SharedCloudCompliance.

        Collections are collections to which this compliance applies.   # noqa: E501

        :param collections: The collections of this SharedCloudCompliance.  # noqa: E501
        :type collections: list[str]
        """

        self._collections = collections

    @property
    def credential_id(self):
        """Gets the credential_id of this SharedCloudCompliance.  # noqa: E501

        CredentialID is the id of the used credential.   # noqa: E501

        :return: The credential_id of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this SharedCloudCompliance.

        CredentialID is the id of the used credential.   # noqa: E501

        :param credential_id: The credential_id of this SharedCloudCompliance.  # noqa: E501
        :type credential_id: str
        """

        self._credential_id = credential_id

    @property
    def cri(self):
        """Gets the cri of this SharedCloudCompliance.  # noqa: E501

        Indicates if this is a CRI-specific vulnerability (true) or not (false).   # noqa: E501

        :return: The cri of this SharedCloudCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._cri

    @cri.setter
    def cri(self, cri):
        """Sets the cri of this SharedCloudCompliance.

        Indicates if this is a CRI-specific vulnerability (true) or not (false).   # noqa: E501

        :param cri: The cri of this SharedCloudCompliance.  # noqa: E501
        :type cri: bool
        """

        self._cri = cri

    @property
    def custom(self):
        """Gets the custom of this SharedCloudCompliance.  # noqa: E501

        Indicates if the vulnerability is a custom vulnerability (e.g., openscap, sandbox) (true) or not (false).   # noqa: E501

        :return: The custom of this SharedCloudCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this SharedCloudCompliance.

        Indicates if the vulnerability is a custom vulnerability (e.g., openscap, sandbox) (true) or not (false).   # noqa: E501

        :param custom: The custom of this SharedCloudCompliance.  # noqa: E501
        :type custom: bool
        """

        self._custom = custom

    @property
    def cve(self):
        """Gets the cve of this SharedCloudCompliance.  # noqa: E501

        CVE ID of the vulnerability (if applied).   # noqa: E501

        :return: The cve of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this SharedCloudCompliance.

        CVE ID of the vulnerability (if applied).   # noqa: E501

        :param cve: The cve of this SharedCloudCompliance.  # noqa: E501
        :type cve: str
        """

        self._cve = cve

    @property
    def cvss(self):
        """Gets the cvss of this SharedCloudCompliance.  # noqa: E501

        CVSS score of the vulnerability.   # noqa: E501

        :return: The cvss of this SharedCloudCompliance.  # noqa: E501
        :rtype: float
        """
        return self._cvss

    @cvss.setter
    def cvss(self, cvss):
        """Sets the cvss of this SharedCloudCompliance.

        CVSS score of the vulnerability.   # noqa: E501

        :param cvss: The cvss of this SharedCloudCompliance.  # noqa: E501
        :type cvss: float
        """

        self._cvss = cvss

    @property
    def description(self):
        """Gets the description of this SharedCloudCompliance.  # noqa: E501

        Description of the vulnerability.   # noqa: E501

        :return: The description of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SharedCloudCompliance.

        Description of the vulnerability.   # noqa: E501

        :param description: The description of this SharedCloudCompliance.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def discovered(self):
        """Gets the discovered of this SharedCloudCompliance.  # noqa: E501

        Date/time when the vulnerability was discovered.   # noqa: E501

        :return: The discovered of this SharedCloudCompliance.  # noqa: E501
        :rtype: datetime
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this SharedCloudCompliance.

        Date/time when the vulnerability was discovered.   # noqa: E501

        :param discovered: The discovered of this SharedCloudCompliance.  # noqa: E501
        :type discovered: datetime
        """

        self._discovered = discovered

    @property
    def err(self):
        """Gets the err of this SharedCloudCompliance.  # noqa: E501

        Err holds any error found during a scan.   # noqa: E501

        :return: The err of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this SharedCloudCompliance.

        Err holds any error found during a scan.   # noqa: E501

        :param err: The err of this SharedCloudCompliance.  # noqa: E501
        :type err: str
        """

        self._err = err

    @property
    def exploit(self):
        """Gets the exploit of this SharedCloudCompliance.  # noqa: E501


        :return: The exploit of this SharedCloudCompliance.  # noqa: E501
        :rtype: VulnExploitType
        """
        return self._exploit

    @exploit.setter
    def exploit(self, exploit):
        """Sets the exploit of this SharedCloudCompliance.


        :param exploit: The exploit of this SharedCloudCompliance.  # noqa: E501
        :type exploit: VulnExploitType
        """

        self._exploit = exploit

    @property
    def fix_date(self):
        """Gets the fix_date of this SharedCloudCompliance.  # noqa: E501

        Date/time when the vulnerability was fixed (in Unix time).   # noqa: E501

        :return: The fix_date of this SharedCloudCompliance.  # noqa: E501
        :rtype: int
        """
        return self._fix_date

    @fix_date.setter
    def fix_date(self, fix_date):
        """Sets the fix_date of this SharedCloudCompliance.

        Date/time when the vulnerability was fixed (in Unix time).   # noqa: E501

        :param fix_date: The fix_date of this SharedCloudCompliance.  # noqa: E501
        :type fix_date: int
        """

        self._fix_date = fix_date

    @property
    def fix_link(self):
        """Gets the fix_link of this SharedCloudCompliance.  # noqa: E501

        Link to the vendor's fixed-version information.   # noqa: E501

        :return: The fix_link of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._fix_link

    @fix_link.setter
    def fix_link(self, fix_link):
        """Sets the fix_link of this SharedCloudCompliance.

        Link to the vendor's fixed-version information.   # noqa: E501

        :param fix_link: The fix_link of this SharedCloudCompliance.  # noqa: E501
        :type fix_link: str
        """

        self._fix_link = fix_link

    @property
    def function_layer(self):
        """Gets the function_layer of this SharedCloudCompliance.  # noqa: E501

        Specifies the serverless layer ID in which the vulnerability was discovered.   # noqa: E501

        :return: The function_layer of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._function_layer

    @function_layer.setter
    def function_layer(self, function_layer):
        """Sets the function_layer of this SharedCloudCompliance.

        Specifies the serverless layer ID in which the vulnerability was discovered.   # noqa: E501

        :param function_layer: The function_layer of this SharedCloudCompliance.  # noqa: E501
        :type function_layer: str
        """

        self._function_layer = function_layer

    @property
    def grace_period_days(self):
        """Gets the grace_period_days of this SharedCloudCompliance.  # noqa: E501

        Number of grace days left for a vulnerability, based on the configured grace period. Nil if no block vulnerability rule applies.   # noqa: E501

        :return: The grace_period_days of this SharedCloudCompliance.  # noqa: E501
        :rtype: int
        """
        return self._grace_period_days

    @grace_period_days.setter
    def grace_period_days(self, grace_period_days):
        """Sets the grace_period_days of this SharedCloudCompliance.

        Number of grace days left for a vulnerability, based on the configured grace period. Nil if no block vulnerability rule applies.   # noqa: E501

        :param grace_period_days: The grace_period_days of this SharedCloudCompliance.  # noqa: E501
        :type grace_period_days: int
        """

        self._grace_period_days = grace_period_days

    @property
    def id(self):
        """Gets the id of this SharedCloudCompliance.  # noqa: E501

        ID of the violation.   # noqa: E501

        :return: The id of this SharedCloudCompliance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedCloudCompliance.

        ID of the violation.   # noqa: E501

        :param id: The id of this SharedCloudCompliance.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def layer_time(self):
        """Gets the layer_time of this SharedCloudCompliance.  # noqa: E501

        Date/time of the image layer to which the CVE belongs.   # noqa: E501

        :return: The layer_time of this SharedCloudCompliance.  # noqa: E501
        :rtype: int
        """
        return self._layer_time

    @layer_time.setter
    def layer_time(self, layer_time):
        """Sets the layer_time of this SharedCloudCompliance.

        Date/time of the image layer to which the CVE belongs.   # noqa: E501

        :param layer_time: The layer_time of this SharedCloudCompliance.  # noqa: E501
        :type layer_time: int
        """

        self._layer_time = layer_time

    @property
    def link(self):
        """Gets the link of this SharedCloudCompliance.  # noqa: E501

        Vendor link to the CVE.   # noqa: E501

        :return: The link of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SharedCloudCompliance.

        Vendor link to the CVE.   # noqa: E501

        :param link: The link of this SharedCloudCompliance.  # noqa: E501
        :type link: str
        """

        self._link = link

    @property
    def package_name(self):
        """Gets the package_name of this SharedCloudCompliance.  # noqa: E501

        Name of the package that caused the vulnerability.   # noqa: E501

        :return: The package_name of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this SharedCloudCompliance.

        Name of the package that caused the vulnerability.   # noqa: E501

        :param package_name: The package_name of this SharedCloudCompliance.  # noqa: E501
        :type package_name: str
        """

        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this SharedCloudCompliance.  # noqa: E501

        Version of the package that caused the vulnerability (or null).   # noqa: E501

        :return: The package_version of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this SharedCloudCompliance.

        Version of the package that caused the vulnerability (or null).   # noqa: E501

        :param package_version: The package_version of this SharedCloudCompliance.  # noqa: E501
        :type package_version: str
        """

        self._package_version = package_version

    @property
    def passed(self):
        """Gets the passed of this SharedCloudCompliance.  # noqa: E501

        Passed indicates if the compliance check pass.   # noqa: E501

        :return: The passed of this SharedCloudCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this SharedCloudCompliance.

        Passed indicates if the compliance check pass.   # noqa: E501

        :param passed: The passed of this SharedCloudCompliance.  # noqa: E501
        :type passed: bool
        """

        self._passed = passed

    @property
    def products(self):
        """Gets the products of this SharedCloudCompliance.  # noqa: E501


        :return: The products of this SharedCloudCompliance.  # noqa: E501
        :rtype: SharedInstalledProducts
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this SharedCloudCompliance.


        :param products: The products of this SharedCloudCompliance.  # noqa: E501
        :type products: SharedInstalledProducts
        """

        self._products = products

    @property
    def published(self):
        """Gets the published of this SharedCloudCompliance.  # noqa: E501

        Date/time when the vulnerability was published (in Unix time).   # noqa: E501

        :return: The published of this SharedCloudCompliance.  # noqa: E501
        :rtype: int
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this SharedCloudCompliance.

        Date/time when the vulnerability was published (in Unix time).   # noqa: E501

        :param published: The published of this SharedCloudCompliance.  # noqa: E501
        :type published: int
        """

        self._published = published

    @property
    def risk_factors(self):
        """Gets the risk_factors of this SharedCloudCompliance.  # noqa: E501

        RiskFactors maps the existence of vulnerability risk factors  # noqa: E501

        :return: The risk_factors of this SharedCloudCompliance.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._risk_factors

    @risk_factors.setter
    def risk_factors(self, risk_factors):
        """Sets the risk_factors of this SharedCloudCompliance.

        RiskFactors maps the existence of vulnerability risk factors  # noqa: E501

        :param risk_factors: The risk_factors of this SharedCloudCompliance.  # noqa: E501
        :type risk_factors: dict(str, str)
        """

        self._risk_factors = risk_factors

    @property
    def severity(self):
        """Gets the severity of this SharedCloudCompliance.  # noqa: E501

        Textual representation of the vulnerability's severity.   # noqa: E501

        :return: The severity of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SharedCloudCompliance.

        Textual representation of the vulnerability's severity.   # noqa: E501

        :param severity: The severity of this SharedCloudCompliance.  # noqa: E501
        :type severity: str
        """

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this SharedCloudCompliance.  # noqa: E501

        Vendor status for the vulnerability.   # noqa: E501

        :return: The status of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SharedCloudCompliance.

        Vendor status for the vulnerability.   # noqa: E501

        :param status: The status of this SharedCloudCompliance.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def templates(self):
        """Gets the templates of this SharedCloudCompliance.  # noqa: E501

        List of templates with which the vulnerability is associated.   # noqa: E501

        :return: The templates of this SharedCloudCompliance.  # noqa: E501
        :rtype: list[VulnComplianceTemplate]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this SharedCloudCompliance.

        List of templates with which the vulnerability is associated.   # noqa: E501

        :param templates: The templates of this SharedCloudCompliance.  # noqa: E501
        :type templates: list[VulnComplianceTemplate]
        """

        self._templates = templates

    @property
    def text(self):
        """Gets the text of this SharedCloudCompliance.  # noqa: E501

        Description of the violation.   # noqa: E501

        :return: The text of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SharedCloudCompliance.

        Description of the violation.   # noqa: E501

        :param text: The text of this SharedCloudCompliance.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def title(self):
        """Gets the title of this SharedCloudCompliance.  # noqa: E501

        Compliance title.   # noqa: E501

        :return: The title of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SharedCloudCompliance.

        Compliance title.   # noqa: E501

        :param title: The title of this SharedCloudCompliance.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def twistlock(self):
        """Gets the twistlock of this SharedCloudCompliance.  # noqa: E501

        Indicates if this is a Twistlock-specific vulnerability (true) or not (false).   # noqa: E501

        :return: The twistlock of this SharedCloudCompliance.  # noqa: E501
        :rtype: bool
        """
        return self._twistlock

    @twistlock.setter
    def twistlock(self, twistlock):
        """Sets the twistlock of this SharedCloudCompliance.

        Indicates if this is a Twistlock-specific vulnerability (true) or not (false).   # noqa: E501

        :param twistlock: The twistlock of this SharedCloudCompliance.  # noqa: E501
        :type twistlock: bool
        """

        self._twistlock = twistlock

    @property
    def type(self):
        """Gets the type of this SharedCloudCompliance.  # noqa: E501


        :return: The type of this SharedCloudCompliance.  # noqa: E501
        :rtype: VulnType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SharedCloudCompliance.


        :param type: The type of this SharedCloudCompliance.  # noqa: E501
        :type type: VulnType
        """

        self._type = type

    @property
    def vec_str(self):
        """Gets the vec_str of this SharedCloudCompliance.  # noqa: E501

        Textual representation of the metric values used to score the vulnerability.   # noqa: E501

        :return: The vec_str of this SharedCloudCompliance.  # noqa: E501
        :rtype: str
        """
        return self._vec_str

    @vec_str.setter
    def vec_str(self, vec_str):
        """Sets the vec_str of this SharedCloudCompliance.

        Textual representation of the metric values used to score the vulnerability.   # noqa: E501

        :param vec_str: The vec_str of this SharedCloudCompliance.  # noqa: E501
        :type vec_str: str
        """

        self._vec_str = vec_str

    @property
    def vuln_tag_infos(self):
        """Gets the vuln_tag_infos of this SharedCloudCompliance.  # noqa: E501

        Tag information for the vulnerability.   # noqa: E501

        :return: The vuln_tag_infos of this SharedCloudCompliance.  # noqa: E501
        :rtype: list[VulnTagInfo]
        """
        return self._vuln_tag_infos

    @vuln_tag_infos.setter
    def vuln_tag_infos(self, vuln_tag_infos):
        """Sets the vuln_tag_infos of this SharedCloudCompliance.

        Tag information for the vulnerability.   # noqa: E501

        :param vuln_tag_infos: The vuln_tag_infos of this SharedCloudCompliance.  # noqa: E501
        :type vuln_tag_infos: list[VulnTagInfo]
        """

        self._vuln_tag_infos = vuln_tag_infos

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
        if not isinstance(other, SharedCloudCompliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedCloudCompliance):
            return True

        return self.to_dict() != other.to_dict()