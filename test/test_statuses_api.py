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
from openapi_client.api.statuses_api import StatusesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestStatusesApi(unittest.TestCase):
    """StatusesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.statuses_api.StatusesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_statuses_host_auto_deploy_get(self):
        """Test case for api_v1_statuses_host_auto_deploy_get

        """
        pass

    def test_api_v1_statuses_intelligence_get(self):
        """Test case for api_v1_statuses_intelligence_get

        """
        pass

    def test_api_v1_statuses_registry_get(self):
        """Test case for api_v1_statuses_registry_get

        """
        pass

    def test_api_v1_statuses_secrets_get(self):
        """Test case for api_v1_statuses_secrets_get

        """
        pass

    def test_api_v1_statuses_serverless_auto_deploy_get(self):
        """Test case for api_v1_statuses_serverless_auto_deploy_get

        """
        pass

    def test_api_v1_statuses_serverless_radar_get(self):
        """Test case for api_v1_statuses_serverless_radar_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
