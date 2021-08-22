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
from openapi_client.models.shared_file_integrity_event import SharedFileIntegrityEvent  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedFileIntegrityEvent(unittest.TestCase):
    """SharedFileIntegrityEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedFileIntegrityEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_file_integrity_event.SharedFileIntegrityEvent()  # noqa: E501
        if include_optional :
            return SharedFileIntegrityEvent(
                account_id = '', 
                cluster = '', 
                collections = [
                    ''
                    ], 
                description = '', 
                event_type = '[\"metadata\",\"read\",\"write\"]', 
                file_type = 56, 
                fqdn = '', 
                hostname = '', 
                metadata = openapi_client.models.shared/file_metadata.shared.FileMetadata(
                    gid = 56, 
                    permissions = 56, 
                    uid = 56, ), 
                path = '', 
                process_name = '', 
                rule_name = '', 
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = ''
            )
        else :
            return SharedFileIntegrityEvent(
        )

    def testSharedFileIntegrityEvent(self):
        """Test SharedFileIntegrityEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()