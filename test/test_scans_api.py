# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.scans_api import ScansApi  # noqa: E501
from openapi_client.rest import ApiException


class TestScansApi(unittest.TestCase):
    """ScansApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.scans_api.ScansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_scans_download_get(self):
        """Test case for api_v1_scans_download_get

        """
        pass

    def test_api_v1_scans_get(self):
        """Test case for api_v1_scans_get

        """
        pass

    def test_api_v1_scans_id_get(self):
        """Test case for api_v1_scans_id_get

        """
        pass

    def test_api_v1_scans_post(self):
        """Test case for api_v1_scans_post

        """
        pass

    def test_api_v1_scans_sonatype_post(self):
        """Test case for api_v1_scans_sonatype_post

        """
        pass

    def test_api_v1_scans_vms_post(self):
        """Test case for api_v1_scans_vms_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
