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
from openapi_client.api.hosts_api import HostsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.hosts_api.HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_hosts_download_get(self):
        """Test case for api_v1_hosts_download_get

        """
        pass

    def test_api_v1_hosts_evaluate_post(self):
        """Test case for api_v1_hosts_evaluate_post

        """
        pass

    def test_api_v1_hosts_get(self):
        """Test case for api_v1_hosts_get

        """
        pass

    def test_api_v1_hosts_info_get(self):
        """Test case for api_v1_hosts_info_get

        """
        pass

    def test_api_v1_hosts_scan_post(self):
        """Test case for api_v1_hosts_scan_post

        """
        pass


if __name__ == '__main__':
    unittest.main()