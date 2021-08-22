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
from openapi_client.models.types_available_vulnerabilities import TypesAvailableVulnerabilities  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesAvailableVulnerabilities(unittest.TestCase):
    """TypesAvailableVulnerabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesAvailableVulnerabilities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_available_vulnerabilities.TypesAvailableVulnerabilities()  # noqa: E501
        if include_optional :
            return TypesAvailableVulnerabilities(
                compliance_vulnerabilities = [
                    openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                        applicable_rules = [
                            ''
                            ], 
                        binary_pkgs = [
                            ''
                            ], 
                        block = True, 
                        cause = '', 
                        cri = True, 
                        custom = True, 
                        cve = '', 
                        cvss = 1.337, 
                        description = '', 
                        discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                        fix_date = 56, 
                        fix_link = '', 
                        function_layer = '', 
                        grace_period_days = 56, 
                        id = 56, 
                        layer_time = 56, 
                        link = '', 
                        package_name = '', 
                        package_version = '', 
                        published = 56, 
                        risk_factors = {
                            'key' : ''
                            }, 
                        severity = '', 
                        status = '', 
                        templates = [
                            '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                            ], 
                        text = '', 
                        title = '', 
                        twistlock = True, 
                        type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                        vec_str = '', 
                        vuln_tag_infos = [
                            openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                comment = '', 
                                name = '', )
                            ], )
                    ], 
                cve_vulnerabilities = [
                    openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                        applicable_rules = [
                            ''
                            ], 
                        binary_pkgs = [
                            ''
                            ], 
                        block = True, 
                        cause = '', 
                        cri = True, 
                        custom = True, 
                        cve = '', 
                        cvss = 1.337, 
                        description = '', 
                        discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                        fix_date = 56, 
                        fix_link = '', 
                        function_layer = '', 
                        grace_period_days = 56, 
                        id = 56, 
                        layer_time = 56, 
                        link = '', 
                        package_name = '', 
                        package_version = '', 
                        published = 56, 
                        risk_factors = {
                            'key' : ''
                            }, 
                        severity = '', 
                        status = '', 
                        templates = [
                            '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                            ], 
                        text = '', 
                        title = '', 
                        twistlock = True, 
                        type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                        vec_str = '', 
                        vuln_tag_infos = [
                            openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                comment = '', 
                                name = '', )
                            ], )
                    ]
            )
        else :
            return TypesAvailableVulnerabilities(
        )

    def testTypesAvailableVulnerabilities(self):
        """Test TypesAvailableVulnerabilities"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
