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
from openapi_client.api.vms_api import VmsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestVmsApi(unittest.TestCase):
    """VmsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.vms_api.VmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_vms_download_get(self):
        """Test case for api_v1_vms_download_get

        """
        pass

    def test_api_v1_vms_get(self):
        """Test case for api_v1_vms_get

        """
        pass

    def test_api_v1_vms_labels_get(self):
        """Test case for api_v1_vms_labels_get

        """
        pass

    def test_api_v1_vms_names_get(self):
        """Test case for api_v1_vms_names_get

        """
        pass

    def test_api_v1_vms_progress_get(self):
        """Test case for api_v1_vms_progress_get

        """
        pass

    def test_api_v1_vms_scan_post(self):
        """Test case for api_v1_vms_scan_post

        """
        pass

    def test_api_v1_vms_stop_post(self):
        """Test case for api_v1_vms_stop_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
