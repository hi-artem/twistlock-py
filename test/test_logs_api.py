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
from openapi_client.api.logs_api import LogsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.logs_api.LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_logs_console_get(self):
        """Test case for api_v1_logs_console_get

        """
        pass

    def test_api_v1_logs_defender_download_get(self):
        """Test case for api_v1_logs_defender_download_get

        """
        pass

    def test_api_v1_logs_defender_get(self):
        """Test case for api_v1_logs_defender_get

        """
        pass

    def test_api_v1_logs_defender_upload_post(self):
        """Test case for api_v1_logs_defender_upload_post

        """
        pass

    def test_api_v1_logs_system_download_get(self):
        """Test case for api_v1_logs_system_download_get

        """
        pass

    def test_api_v1_logs_system_upload_post(self):
        """Test case for api_v1_logs_system_upload_post

        """
        pass


if __name__ == '__main__':
    unittest.main()