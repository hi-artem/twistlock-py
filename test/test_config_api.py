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
from openapi_client.api.config_api import ConfigApi  # noqa: E501
from openapi_client.rest import ApiException


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.config_api.ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_config_auditsink_get(self):
        """Test case for api_v1_config_auditsink_get

        """
        pass

    def test_api_v1_config_validating_webhook_get(self):
        """Test case for api_v1_config_validating_webhook_get

        """
        pass


if __name__ == '__main__':
    unittest.main()