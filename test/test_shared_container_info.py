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
from openapi_client.models.shared_container_info import SharedContainerInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedContainerInfo(unittest.TestCase):
    """SharedContainerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedContainerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_container_info.SharedContainerInfo()  # noqa: E501
        if include_optional :
            return SharedContainerInfo(
                all_compliance = openapi_client.models.vuln/all_compliance.vuln.AllCompliance(
                    compliance = [
                        openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                            applicable_rules = [
                                ''
                                ], 
                            binary_pkgs = [
                                ''
                                ], 
                            block = True, 
                            cause = '', 
                            cri = True, 
                            custom = True, 
                            cve = '', 
                            cvss = 1.337, 
                            description = '', 
                            discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                            fix_date = 56, 
                            fix_link = '', 
                            function_layer = '', 
                            grace_period_days = 56, 
                            id = 56, 
                            layer_time = 56, 
                            link = '', 
                            package_name = '', 
                            package_version = '', 
                            published = 56, 
                            risk_factors = {
                                'key' : ''
                                }, 
                            severity = '', 
                            status = '', 
                            templates = [
                                '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                                ], 
                            text = '', 
                            title = '', 
                            twistlock = True, 
                            type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                            vec_str = '', 
                            vuln_tag_infos = [
                                openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                    comment = '', 
                                    name = '', )
                                ], )
                        ], 
                    enabled = True, ), 
                app = '', 
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
                compliance_issues = [
                    openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                        applicable_rules = [
                            ''
                            ], 
                        binary_pkgs = [
                            ''
                            ], 
                        block = True, 
                        cause = '', 
                        cri = True, 
                        custom = True, 
                        cve = '', 
                        cvss = 1.337, 
                        description = '', 
                        discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                        fix_date = 56, 
                        fix_link = '', 
                        function_layer = '', 
                        grace_period_days = 56, 
                        id = 56, 
                        layer_time = 56, 
                        link = '', 
                        package_name = '', 
                        package_version = '', 
                        published = 56, 
                        risk_factors = {
                            'key' : ''
                            }, 
                        severity = '', 
                        status = '', 
                        templates = [
                            '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                            ], 
                        text = '', 
                        title = '', 
                        twistlock = True, 
                        type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                        vec_str = '', 
                        vuln_tag_infos = [
                            openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                comment = '', 
                                name = '', )
                            ], )
                    ], 
                compliance_issues_count = 56, 
                compliance_risk_score = 1.337, 
                external_labels = [
                    openapi_client.models.common/external_label.common.ExternalLabel(
                        key = '', 
                        source_name = '', 
                        source_type = '[\"namespace\",\"deployment\",\"aws\",\"azure\",\"gcp\"]', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = '', )
                    ], 
                id = '', 
                image = '', 
                image_id = '', 
                image_name = '', 
                infra = True, 
                installed_products = openapi_client.models.shared/installed_products.shared.InstalledProducts(
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
                    swarm_node = True, ), 
                labels = [
                    ''
                    ], 
                name = '', 
                namespace = '', 
                network = openapi_client.models.shared/container_network.shared.ContainerNetwork(
                    ports = [
                        openapi_client.models.shared/container_port.shared.ContainerPort(
                            container = 56, 
                            host = 56, 
                            host_ip = '', 
                            listening = True, 
                            nat = True, )
                        ], ), 
                network_settings = openapi_client.models.shared/docker_network_info.shared.DockerNetworkInfo(
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
                        ], ), 
                processes = [
                    openapi_client.models.shared/container_process.shared.ContainerProcess(
                        name = '', )
                    ], 
                profile_id = '', 
                size_bytes = 56
            )
        else :
            return SharedContainerInfo(
        )

    def testSharedContainerInfo(self):
        """Test SharedContainerInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
