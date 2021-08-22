# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.vuln_custom_vulnerabilities import VulnCustomVulnerabilities  # noqa: E501
from openapi_client.rest import ApiException

class TestVulnCustomVulnerabilities(unittest.TestCase):
    """VulnCustomVulnerabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VulnCustomVulnerabilities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.vuln_custom_vulnerabilities.VulnCustomVulnerabilities()  # noqa: E501
        if include_optional :
            return VulnCustomVulnerabilities(
                id = '', 
                digest = '', 
                rules = [
                    openapi_client.models.vuln/custom_vulnerability.vuln.CustomVulnerability(
                        _id = '', 
                        max_version_inclusive = '', 
                        md5 = '', 
                        min_version_inclusive = '', 
                        name = '', 
                        package = '', 
                        type = '[\"nodejs\",\"gem\",\"python\",\"jar\",\"package\",\"windows\",\"binary\",\"nuget\",\"go\"]', )
                    ]
            )
        else :
            return VulnCustomVulnerabilities(
        )

    def testVulnCustomVulnerabilities(self):
        """Test VulnCustomVulnerabilities"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
