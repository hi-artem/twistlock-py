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
from openapi_client.models.types_serverless_auto_deploy_status import TypesServerlessAutoDeployStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesServerlessAutoDeployStatus(unittest.TestCase):
    """TypesServerlessAutoDeployStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesServerlessAutoDeployStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_serverless_auto_deploy_status.TypesServerlessAutoDeployStatus()  # noqa: E501
        if include_optional :
            return TypesServerlessAutoDeployStatus(
                errors = [
                    ''
                    ], 
                scanning = True, 
                specs = [
                    openapi_client.models.types/serverless_auto_deploy_spec_status.types.ServerlessAutoDeploySpecStatus(
                        defended = 56, 
                        discovered = 56, 
                        name = '', )
                    ]
            )
        else :
            return TypesServerlessAutoDeployStatus(
        )

    def testTypesServerlessAutoDeployStatus(self):
        """Test TypesServerlessAutoDeployStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()