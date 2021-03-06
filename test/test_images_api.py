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
from openapi_client.api.images_api import ImagesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_images_download_get(self):
        """Test case for api_v1_images_download_get

        """
        pass

    def test_api_v1_images_evaluate_post(self):
        """Test case for api_v1_images_evaluate_post

        """
        pass

    def test_api_v1_images_get(self):
        """Test case for api_v1_images_get

        """
        pass

    def test_api_v1_images_names_get(self):
        """Test case for api_v1_images_names_get

        """
        pass

    def test_api_v1_images_progress_get(self):
        """Test case for api_v1_images_progress_get

        """
        pass

    def test_api_v1_images_scan_post(self):
        """Test case for api_v1_images_scan_post

        """
        pass

    def test_api_v1_images_twistlock_defender_app_embedded_tar_gz_get(self):
        """Test case for api_v1_images_twistlock_defender_app_embedded_tar_gz_get

        """
        pass

    def test_api_v1_images_twistlock_defender_layer_zip_post(self):
        """Test case for api_v1_images_twistlock_defender_layer_zip_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
