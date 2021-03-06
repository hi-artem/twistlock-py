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
from openapi_client.models.runtime_profile_process import RuntimeProfileProcess  # noqa: E501
from openapi_client.rest import ApiException

class TestRuntimeProfileProcess(unittest.TestCase):
    """RuntimeProfileProcess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeProfileProcess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.runtime_profile_process.RuntimeProfileProcess()  # noqa: E501
        if include_optional :
            return RuntimeProfileProcess(
                command = '', 
                md5 = '', 
                modified = True, 
                path = '', 
                ppath = '', 
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = ''
            )
        else :
            return RuntimeProfileProcess(
        )

    def testRuntimeProfileProcess(self):
        """Test RuntimeProfileProcess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
