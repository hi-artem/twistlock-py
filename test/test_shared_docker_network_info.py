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
from openapi_client.models.shared_docker_network_info import SharedDockerNetworkInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedDockerNetworkInfo(unittest.TestCase):
    """SharedDockerNetworkInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedDockerNetworkInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_docker_network_info.SharedDockerNetworkInfo()  # noqa: E501
        if include_optional :
            return SharedDockerNetworkInfo(
                ip_address = '', 
                mac_address = '', 
                networks = [
                    openapi_client.models.shared/network_info.shared.NetworkInfo(
                        ip_address = '', 
                        mac_address = '', 
                        name = '', )
                    ], 
                ports = [
                    openapi_client.models.shared/port.shared.Port(
                        container_port = '', 
                        host_ip = '', 
                        host_port = 56, )
                    ]
            )
        else :
            return SharedDockerNetworkInfo(
        )

    def testSharedDockerNetworkInfo(self):
        """Test SharedDockerNetworkInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()