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
from openapi_client.models.shared_subnet_connections import SharedSubnetConnections  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedSubnetConnections(unittest.TestCase):
    """SharedSubnetConnections unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedSubnetConnections
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_subnet_connections.SharedSubnetConnections()  # noqa: E501
        if include_optional :
            return SharedSubnetConnections(
                incoming = {
                    'key' : openapi_client.models.cnnf/radar_connection_instances.cnnf.RadarConnectionInstances(
                        instances = [
                            openapi_client.models.cnnf/radar_connection_instance.cnnf.RadarConnectionInstance(
                                dst = '', 
                                policy_rule = openapi_client.models.cnnf/radar_policy_rule.cnnf.RadarPolicyRule(
                                    effect = '[\"allow\",\"alert\",\"prevent\",\"monitor\",\"\"]', 
                                    port_ranges = [
                                        openapi_client.models.common/port_range.common.PortRange(
                                            deny = True, 
                                            end = 56, 
                                            start = 56, )
                                        ], ), 
                                port = openapi_client.models.common/port_data.common.PortData(
                                    protocol = '', ), 
                                src = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    }, 
                outgoing = {
                    'key' : openapi_client.models.cnnf/radar_connection_instances.cnnf.RadarConnectionInstances(
                        instances = [
                            openapi_client.models.cnnf/radar_connection_instance.cnnf.RadarConnectionInstance(
                                dst = '', 
                                policy_rule = openapi_client.models.cnnf/radar_policy_rule.cnnf.RadarPolicyRule(
                                    effect = '[\"allow\",\"alert\",\"prevent\",\"monitor\",\"\"]', 
                                    port_ranges = [
                                        openapi_client.models.common/port_range.common.PortRange(
                                            deny = True, 
                                            end = 56, 
                                            start = 56, )
                                        ], ), 
                                port = openapi_client.models.common/port_data.common.PortData(
                                    protocol = '', ), 
                                src = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    }
            )
        else :
            return SharedSubnetConnections(
        )

    def testSharedSubnetConnections(self):
        """Test SharedSubnetConnections"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
