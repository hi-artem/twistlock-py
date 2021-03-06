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
from openapi_client.models.types_container_radar_data import TypesContainerRadarData  # noqa: E501
from openapi_client.rest import ApiException

class TestTypesContainerRadarData(unittest.TestCase):
    """TypesContainerRadarData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TypesContainerRadarData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.types_container_radar_data.TypesContainerRadarData()  # noqa: E501
        if include_optional :
            return TypesContainerRadarData(
                container_count = 56, 
                radar = [
                    openapi_client.models.types/container_radar_entity.types.ContainerRadarEntity(
                        _id = '', 
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
                        cluster = '', 
                        compliance_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), 
                        consul = True, 
                        container_count = 56, 
                        distro = '', 
                        dns = True, 
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
                        has_dns_connection = True, 
                        host_count = 56, 
                        hostname = '', 
                        image_id = '', 
                        image_name = '', 
                        image_names = [
                            ''
                            ], 
                        incident_count = 56, 
                        incoming_connections = [
                            openapi_client.models.shared/container_radar_incoming_connection.shared.ContainerRadarIncomingConnection(
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
                                profile_hash = 56, 
                                profile_id = '', )
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
                        istio = True, 
                        istio_authorization_policies = [
                            openapi_client.models.istio/authorization_policy.istio.AuthorizationPolicy(
                                name = '', 
                                namespace = '', 
                                rules = [
                                    openapi_client.models.istio/authorization_policy_rule.istio.AuthorizationPolicyRule(
                                        destinations = [
                                            openapi_client.models.istio/authorization_policy_destination.istio.AuthorizationPolicyDestination(
                                                methods = [
                                                    ''
                                                    ], 
                                                paths = [
                                                    ''
                                                    ], )
                                            ], 
                                        sources = [
                                            openapi_client.models.istio/authorization_policy_source.istio.AuthorizationPolicySource(
                                                namespaces = [
                                                    ''
                                                    ], 
                                                principals = [
                                                    ''
                                                    ], )
                                            ], )
                                    ], 
                                target_services = [
                                    openapi_client.models.istio/authorization_policy_service.istio.AuthorizationPolicyService(
                                        name = '', 
                                        namespace = '', )
                                    ], )
                            ], 
                        k8s = openapi_client.models.shared/profile_kubernetes_data.shared.ProfileKubernetesData(
                            cluster_roles = [
                                openapi_client.models.shared/kube_cluster_role.shared.KubeClusterRole(
                                    labels = [
                                        openapi_client.models.shared/kube_label.shared.KubeLabel(
                                            key = '', 
                                            value = '', )
                                        ], 
                                    name = '', 
                                    role_binding = '', )
                                ], 
                            roles = [
                                openapi_client.models.shared/kube_role.shared.KubeRole(
                                    name = '', 
                                    namespace = '', 
                                    role_binding = '', )
                                ], 
                            service_account = '', ), 
                        label = '', 
                        labels = [
                            ''
                            ], 
                        learning = True, 
                        namespace = '', 
                        network_count = 56, 
                        processes_count = 56, 
                        profile_hash = 56, 
                        region = '', 
                        resolved = True, 
                        service_ip = '', 
                        service_name = '', 
                        service_ports = [
                            56
                            ], 
                        subnet_connections = openapi_client.models.shared/subnet_connections.shared.SubnetConnections(), 
                        type = '[\"\",\"docker\",\"kubernetes\",\"tas\",\"swarm\",\"istio\",\"internet\"]', 
                        vulnerability_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), )
                    ], 
                radar_subnets = [
                    openapi_client.models.cnnf/network_entity.cnnf.NetworkEntity(
                        _id = 56, 
                        allow_all = openapi_client.models.cnnf/allow_all_connections.cnnf.AllowAllConnections(
                            inbound = [
                                '[\"container\",\"host\",\"subnet\",\"dns\"]'
                                ], 
                            outbound = [
                                '[\"container\",\"host\",\"subnet\",\"dns\"]'
                                ], ), 
                        collections = [
                            openapi_client.models.collection/collection.collection.Collection(
                                account_ids = [
                                    ''
                                    ], 
                                app_ids = [
                                    ''
                                    ], 
                                clusters = [
                                    ''
                                    ], 
                                code_repos = [
                                    ''
                                    ], 
                                color = '', 
                                containers = [
                                    ''
                                    ], 
                                description = '', 
                                functions = [
                                    ''
                                    ], 
                                hosts = [
                                    ''
                                    ], 
                                images = [
                                    ''
                                    ], 
                                labels = [
                                    ''
                                    ], 
                                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                namespaces = [
                                    ''
                                    ], 
                                owner = '', 
                                prisma = True, 
                                system = True, )
                            ], 
                        domains = [
                            ''
                            ], 
                        name = '', 
                        subnets = [
                            openapi_client.models.cnnf/subnet.cnnf.Subnet(
                                cidr = '', 
                                name = '', )
                            ], 
                        type = '[\"container\",\"host\",\"subnet\",\"dns\"]', )
                    ]
            )
        else :
            return TypesContainerRadarData(
        )

    def testTypesContainerRadarData(self):
        """Test TypesContainerRadarData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
