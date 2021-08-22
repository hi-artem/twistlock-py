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
from openapi_client.models.runtime_dns_query import RuntimeDNSQuery  # noqa: E501
from openapi_client.rest import ApiException

class TestRuntimeDNSQuery(unittest.TestCase):
    """RuntimeDNSQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeDNSQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.runtime_dns_query.RuntimeDNSQuery()  # noqa: E501
        if include_optional :
            return RuntimeDNSQuery(
                domain_name = '', 
                domain_type = ''
            )
        else :
            return RuntimeDNSQuery(
        )

    def testRuntimeDNSQuery(self):
        """Test RuntimeDNSQuery"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()