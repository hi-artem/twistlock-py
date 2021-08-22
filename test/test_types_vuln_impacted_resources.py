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
from openapi_client.models.types_vuln_impacted_resources import TypesVulnImpactedResources  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesVulnImpactedResources(unittest.TestCase):
    """TypesVulnImpactedResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesVulnImpactedResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_vuln_impacted_resources.TypesVulnImpactedResources()  # noqa: E501
        if include_optional :
            return TypesVulnImpactedResources(
                id = '', 
                functions = {
                    'key' : ''
                    }, 
                hosts = [
                    ''
                    ], 
                risk_tree = {
                    'key' : [
                        openapi_client.models.types/risk_tree_resource.types.RiskTreeResource(
                            container = '', 
                            factors = openapi_client.models.types/risk_score_factors.types.RiskScoreFactors(
                                internet = True, 
                                network = True, 
                                no_security_profile = True, 
                                privileged_container = True, 
                                root_privilege = True, ), 
                            host = '', 
                            image = '', 
                            namespace = '', )
                        ]
                    }
            )
        else :
            return TypesVulnImpactedResources(
        )

    def testTypesVulnImpactedResources(self):
        """Test TypesVulnImpactedResources"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
