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
from openapi_client.models.shared_installed_products import SharedInstalledProducts  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedInstalledProducts(unittest.TestCase):
    """SharedInstalledProducts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedInstalledProducts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_installed_products.SharedInstalledProducts()  # noqa: E501
        if include_optional :
            return SharedInstalledProducts(
                apache = '', 
                aws_cloud = True, 
                crio = True, 
                docker = '', 
                docker_enterprise = True, 
                has_package_manager = True, 
                k8s_api_server = True, 
                k8s_controller_manager = True, 
                k8s_etcd = True, 
                k8s_federation_api_server = True, 
                k8s_federation_controller_manager = True, 
                k8s_kubelet = True, 
                k8s_proxy = True, 
                k8s_scheduler = True, 
                kubernetes = '', 
                openshift = True, 
                os_distro = '', 
                serverless = True, 
                swarm_manager = True, 
                swarm_node = True
            )
        else :
            return SharedInstalledProducts(
        )

    def testSharedInstalledProducts(self):
        """Test SharedInstalledProducts"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()