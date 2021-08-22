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
from openapi_client.models.types_credential_usage import TypesCredentialUsage  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesCredentialUsage(unittest.TestCase):
    """TypesCredentialUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesCredentialUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_credential_usage.TypesCredentialUsage()  # noqa: E501
        if include_optional :
            return TypesCredentialUsage(
                description = '', 
                type = '[\"Alert settings\",\"Alert profile\",\"Registry Scan\",\"Serverless Scan\",\"Cloud Scan\",\"Secret Store\",\"Serverless Auto-Deploy\",\"Host Auto-deploy\",\"VM Scan\",\"Code Repository Scan\",\"Custom Intelligence Endpoint\"]'
            )
        else :
            return TypesCredentialUsage(
        )

    def testTypesCredentialUsage(self):
        """Test TypesCredentialUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
