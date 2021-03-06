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
from openapi_client.api.deployment_api import DeploymentApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDeploymentApi(unittest.TestCase):
    """DeploymentApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.deployment_api.DeploymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_deployment_daemonsets_deploy_post(self):
        """Test case for api_v1_deployment_daemonsets_deploy_post

        """
        pass

    def test_api_v1_deployment_daemonsets_get(self):
        """Test case for api_v1_deployment_daemonsets_get

        """
        pass

    def test_api_v1_deployment_host_progress_get(self):
        """Test case for api_v1_deployment_host_progress_get

        """
        pass

    def test_api_v1_deployment_host_scan_post(self):
        """Test case for api_v1_deployment_host_scan_post

        """
        pass

    def test_api_v1_deployment_host_stop_post(self):
        """Test case for api_v1_deployment_host_stop_post

        """
        pass

    def test_api_v1_deployment_serverless_progress_get(self):
        """Test case for api_v1_deployment_serverless_progress_get

        """
        pass

    def test_api_v1_deployment_serverless_scan_post(self):
        """Test case for api_v1_deployment_serverless_scan_post

        """
        pass

    def test_api_v1_deployment_serverless_stop_post(self):
        """Test case for api_v1_deployment_serverless_stop_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
