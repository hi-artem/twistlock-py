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
from openapi_client.models.types_trends import TypesTrends  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesTrends(unittest.TestCase):
    """TypesTrends unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesTrends
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_trends.TypesTrends()  # noqa: E501
        if include_optional :
            return TypesTrends(
                compliance_trend = [
                    openapi_client.models.types/compliance_daily_stats.types.ComplianceDailyStats(
                        _id = '', 
                        distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                defenders_summary = {
                    'key' : 56
                    }, 
                vulnerability_summary = openapi_client.models.types/vulnerability_summary.types.VulnerabilitySummary(
                    containers = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), 
                    functions = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), 
                    hosts = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), 
                    images = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), )
            )
        else :
            return TypesTrends(
        )

    def testTypesTrends(self):
        """Test TypesTrends"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
