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
from openapi_client.models.runtime_profile_network import RuntimeProfileNetwork  # noqa: E501
from openapi_client.rest import ApiException

class TestRuntimeProfileNetwork(unittest.TestCase):
    """RuntimeProfileNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeProfileNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.runtime_profile_network.RuntimeProfileNetwork()  # noqa: E501
        if include_optional :
            return RuntimeProfileNetwork(
                behavioral = openapi_client.models.runtime/profile_network_behavioral.runtime.ProfileNetworkBehavioral(
                    dns_queries = [
                        openapi_client.models.runtime/dns_query.runtime.DNSQuery(
                            domain_name = '', 
                            domain_type = '', )
                        ], 
                    listening_ports = [
                        openapi_client.models.runtime/app_listening_ports.runtime.AppListeningPorts(
                            app = '', 
                            ports_data = openapi_client.models.common/profile_port_data.common.ProfilePortData(
                                all = True, 
                                ports = [
                                    openapi_client.models.common/profile_port.common.ProfilePort(
                                        port = 56, 
                                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], ), )
                        ], 
                    outbound_ports = openapi_client.models.common/profile_port_data.common.ProfilePortData(
                        all = True, ), ), 
                geoip = openapi_client.models.runtime/profile_network_geo_ip.runtime.ProfileNetworkGeoIP(
                    countries = [
                        openapi_client.models.runtime/geo_ip.runtime.GeoIP(
                            code = '', 
                            ip = '', 
                            modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                static = openapi_client.models.runtime/profile_network_static.runtime.ProfileNetworkStatic(
                    listening_ports = [
                        openapi_client.models.runtime/app_listening_ports.runtime.AppListeningPorts(
                            app = '', 
                            ports_data = openapi_client.models.common/profile_port_data.common.ProfilePortData(
                                all = True, 
                                ports = [
                                    openapi_client.models.common/profile_port.common.ProfilePort(
                                        port = 56, 
                                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], ), )
                        ], )
            )
        else :
            return RuntimeProfileNetwork(
        )

    def testRuntimeProfileNetwork(self):
        """Test RuntimeProfileNetwork"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
