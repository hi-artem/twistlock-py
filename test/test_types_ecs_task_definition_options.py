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
from openapi_client.models.types_ecs_task_definition_options import TypesEcsTaskDefinitionOptions  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesEcsTaskDefinitionOptions(unittest.TestCase):
    """TypesEcsTaskDefinitionOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesEcsTaskDefinitionOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_ecs_task_definition_options.TypesEcsTaskDefinitionOptions()  # noqa: E501
        if include_optional :
            return TypesEcsTaskDefinitionOptions(
                cluster = '', 
                collect_pod_labels = True, 
                console_addr = '', 
                credential_id = '', 
                cri = True, 
                docker_socket_path = '', 
                image = '', 
                istio = True, 
                namespace = '', 
                node_selector = '', 
                orchestration = '', 
                privileged = True, 
                proxy = openapi_client.models.common/defender_proxy_opt.common.DefenderProxyOpt(
                    ca = '', 
                    http_proxy = '', 
                    no_proxy = '', 
                    password = '', 
                    user = '', ), 
                region = '', 
                secretsname = '', 
                selinux = True, 
                serviceaccounts = True, 
                task_name = ''
            )
        else :
            return TypesEcsTaskDefinitionOptions(
        )

    def testTypesEcsTaskDefinitionOptions(self):
        """Test TypesEcsTaskDefinitionOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
