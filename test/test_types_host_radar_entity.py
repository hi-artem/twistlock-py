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
from openapi_client.models.types_host_radar_entity import TypesHostRadarEntity  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesHostRadarEntity(unittest.TestCase):
    """TypesHostRadarEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesHostRadarEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_host_radar_entity.TypesHostRadarEntity()  # noqa: E501
        if include_optional :
            return TypesHostRadarEntity(
                os_distro = '', 
                id = '', 
                activities_count = 56, 
                allow_all = openapi_client.models.cnnf/allow_all_connections.cnnf.AllowAllConnections(
                    inbound = [
                        '[\"container\",\"host\",\"subnet\",\"dns\"]'
                        ], 
                    outbound = [
                        '[\"container\",\"host\",\"subnet\",\"dns\"]'
                        ], ), 
                app_firewall_attack_counts = [
                    openapi_client.models.types/app_firewall_attack_count.types.AppFirewallAttackCount(
                        count = 56, 
                        type = '[\"xss\",\"sqli\",\"cmdi\",\"lfi\",\"codeInjection\",\"deniedIP\",\"deniedCountry\",\"header\",\"violationsExceeded\",\"attackTools\",\"shellshock\",\"disallowedFile\",\"malformedRequest\",\"informationLeak\",\"unexpectedAPI\",\"dos\",\"searchEngineCrawler\",\"businessAnalyticsBot\",\"educationalBot\",\"newsBot\",\"financialBot\",\"contentFeedClient\",\"archivingBot\",\"careerSearchBot\",\"mediaSearchBot\",\"genericBot\",\"webAutomationTool\",\"webScraper\",\"apiLibrary\",\"httpLibrary\",\"sessionValidation\",\"javascriptTimeout\",\"missingCookie\",\"browserImpersonation\",\"botImpersonation\",\"requestAnomalies\",\"userDefinedBot\",\"recaptchaRequired\",\"recaptchaVerificationFailed\",\"customRule\"]', )
                    ], 
                cloud_metadata = openapi_client.models.common/cloud_metadata.common.CloudMetadata(
                    account_id = '', 
                    image = '', 
                    labels = [
                        openapi_client.models.common/external_label.common.ExternalLabel(
                            key = '', 
                            source_name = '', 
                            source_type = '[\"namespace\",\"deployment\",\"aws\",\"azure\",\"gcp\"]', 
                            timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            value = '', )
                        ], 
                    name = '', 
                    provider = '[\"aws\",\"azure\",\"gcp\",\"alibaba\",\"others\"]', 
                    region = '', 
                    resource_id = '', 
                    type = '', ), 
                cluster = '', 
                compliance_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                    critical = 56, 
                    high = 56, 
                    low = 56, 
                    medium = 56, 
                    total = 56, ), 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                file_integrity_count = 56, 
                filesystem_count = 56, 
                firewall_protection = openapi_client.models.waas/protection_status.waas.ProtectionStatus(
                    enabled = True, 
                    supported = True, ), 
                geoip = openapi_client.models.runtime/profile_network_geo_ip.runtime.ProfileNetworkGeoIP(
                    countries = [
                        openapi_client.models.runtime/geo_ip.runtime.GeoIP(
                            code = '', 
                            ip = '', 
                            modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                incident_count = 56, 
                incoming = [
                    openapi_client.models.shared/host_radar_incoming_connection.shared.HostRadarIncomingConnection(
                        dst_host = '', 
                        policy_rules = [
                            openapi_client.models.cnnf/radar_policy_rule.cnnf.RadarPolicyRule(
                                effect = '[\"allow\",\"alert\",\"prevent\",\"monitor\",\"\"]', 
                                port_ranges = [
                                    openapi_client.models.common/port_range.common.PortRange(
                                        deny = True, 
                                        end = 56, 
                                        start = 56, )
                                    ], )
                            ], 
                        ports = [
                            openapi_client.models.common/port_data.common.PortData(
                                port = 56, 
                                protocol = '', )
                            ], 
                        src_hash = 56, 
                        src_host = '', )
                    ], 
                internet = openapi_client.models.shared/internet_connections.shared.InternetConnections(
                    incoming = [
                        openapi_client.models.shared/connection.shared.Connection(
                            port = 56, 
                            protocol = '', )
                        ], 
                    outgoing = [
                        openapi_client.models.shared/connection.shared.Connection(
                            port = 56, 
                            protocol = '', )
                        ], ), 
                labels = [
                    ''
                    ], 
                listening_ports = openapi_client.models.common/profile_port_data.common.ProfilePortData(
                    all = True, 
                    ports = [
                        openapi_client.models.common/profile_port.common.ProfilePort(
                            port = 56, 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ), 
                log_inspection_count = 56, 
                network_count = 56, 
                outbound_ports = openapi_client.models.common/profile_port_data.common.ProfilePortData(
                    all = True, 
                    ports = [
                        openapi_client.models.common/profile_port.common.ProfilePort(
                            port = 56, 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ), 
                processes_count = 56, 
                profile_hash = 56, 
                subnet_connections = openapi_client.models.shared/subnet_connections.shared.SubnetConnections(
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
                        'key' : openapi_client.models.cnnf/radar_connection_instances.cnnf.RadarConnectionInstances()
                        }, ), 
                vulnerability_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                    critical = 56, 
                    high = 56, 
                    low = 56, 
                    medium = 56, 
                    total = 56, )
            )
        else :
            return TypesHostRadarEntity(
        )

    def testTypesHostRadarEntity(self):
        """Test TypesHostRadarEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()