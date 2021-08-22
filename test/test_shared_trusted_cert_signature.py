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
from openapi_client.models.shared_trusted_cert_signature import SharedTrustedCertSignature  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedTrustedCertSignature(unittest.TestCase):
    """SharedTrustedCertSignature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedTrustedCertSignature
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_trusted_cert_signature.SharedTrustedCertSignature()  # noqa: E501
        if include_optional :
            return SharedTrustedCertSignature(
                cn = '', 
                issuer = '', 
                not_after1 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                not_before1 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                raw = ''
            )
        else :
            return SharedTrustedCertSignature(
        )

    def testSharedTrustedCertSignature(self):
        """Test SharedTrustedCertSignature"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
