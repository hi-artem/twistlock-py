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
from openapi_client.models.types_all_defenders_usage import TypesAllDefendersUsage  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesAllDefendersUsage(unittest.TestCase):
    """TypesAllDefendersUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesAllDefendersUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_all_defenders_usage.TypesAllDefendersUsage()  # noqa: E501
        if include_optional :
            return TypesAllDefendersUsage(
                app_embedded = openapi_client.models.types/defender_usage.types.DefenderUsage(
                    credit_count = 1.337, 
                    defenders_count = 1.337, ), 
                container = openapi_client.models.types/defender_usage.types.DefenderUsage(
                    credit_count = 1.337, 
                    defenders_count = 1.337, ), 
                host = openapi_client.models.types/defender_usage.types.DefenderUsage(
                    credit_count = 1.337, 
                    defenders_count = 1.337, ), 
                period = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                remaining_credits = 56, 
                serverless = openapi_client.models.types/serverless_usage.types.ServerlessUsage(
                    credit_count = 1.337, 
                    defenders_count = 1.337, 
                    invocations = 1.337, ), 
                waas = openapi_client.models.types/defender_usage.types.DefenderUsage(
                    credit_count = 1.337, 
                    defenders_count = 1.337, )
            )
        else :
            return TypesAllDefendersUsage(
        )

    def testTypesAllDefendersUsage(self):
        """Test TypesAllDefendersUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()