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
from openapi_client.models.shared_runtime_audit import SharedRuntimeAudit  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedRuntimeAudit(unittest.TestCase):
    """SharedRuntimeAudit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedRuntimeAudit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_runtime_audit.SharedRuntimeAudit()  # noqa: E501
        if include_optional :
            return SharedRuntimeAudit(
                id = '', 
                account_id = '', 
                app = '', 
                app_id = '', 
                attack_techniques = [
                    '[\"exploitationForPrivilegeEscalation\",\"exploitPublicFacingApplication\",\"applicationExploitRCE\",\"networkServiceScanning\",\"endpointDenialOfService\",\"exfiltrationGeneral\",\"systemNetworkConfigurationDiscovery\",\"unsecuredCredentials\",\"credentialDumping\",\"systemInformationDiscovery\",\"systemNetworkConnectionDiscovery\",\"systemUserDiscovery\",\"accountDiscovery\",\"cloudInstanceMetadataAPI\",\"accessKubeletMainAPI\",\"queryKubeletReadonlyAPI\",\"accessKubernetesAPIServer\",\"softwareDeploymentTools\",\"ingressToolTransfer\",\"lateralToolTransfer\",\"commandAndControlGeneral\",\"resourceHijacking\",\"manInTheMiddle\",\"nativeBinaryExecution\",\"foreignBinaryExecution\",\"createAccount\",\"accountManipulation\",\"abuseElevationControlMechanisms\",\"supplyChainCompromise\",\"obfuscatedFiles\",\"hijackExecutionFlow\",\"impairDefences\",\"scheduledTaskJob\",\"exploitationOfRemoteServices\",\"eventTriggeredExecution\",\"accountAccessRemoval\",\"privilegedContainer\",\"writableVolumes\",\"execIntoContainer\",\"softwareDiscovery\",\"createContainer\",\"kubernetesSecrets\",\"fileAndDirectoryDiscovery\",\"masquerading\",\"webShell\",\"compileAfterDelivery\"]'
                    ], 
                attack_type = '[\"\",\"cloudMetadataProbing\",\"kubeletAPIAccess\",\"kubeletReadonlyAccess\",\"kubectlSpawned\",\"kubectlDownloaded\",\"horizontalPortScanning\",\"verticalPortScanning\",\"explicitlyDeniedIP\",\"customFeedIP\",\"feedIP\",\"unexpectedOutboundPort\",\"suspiciousNetworkActivity\",\"unexpectedListeningPort\",\"explicitlyDeniedListeningPort\",\"explicitlyDeniedOutboundPort\",\"listeningPortModifiedProcess\",\"outboundPortModifiedProcess\",\"feedDNS\",\"explicitlyDeniedDNS\",\"dnsQuery\",\"unexpectedProcess\",\"portScanProcess\",\"malwareProcessCustom\",\"malwareProcessFeed\",\"explicitlyDeniedProcess\",\"modifiedProcess\",\"cryptoMinerProcess\",\"lateralMovementProcess\",\"tmpfsProcess\",\"policyHijacked\",\"reverseShell\",\"suidBinaries\",\"unknownOriginBinary\",\"webShell\",\"administrativeAccount\",\"encryptedBinary\",\"sshAccess\",\"explicitlyDeniedFile\",\"malwareFileCustom\",\"malwareFileFeed\",\"execFileAccess\",\"elfFileAccess\",\"secretFileAccess\",\"regFileAccess\",\"wildfireMalware\",\"unknownOriginBinary\",\"webShell\",\"fileIntegrity\",\"alteredBinary\",\"malwareDownloaded\",\"suspiciousELFHeader\",\"executionFlowHijackAttempt\",\"customRule\"]', 
                cluster = '', 
                collections = [
                    ''
                    ], 
                container = True, 
                container_id = '', 
                container_name = '', 
                count = 56, 
                country = '', 
                effect = '[\"block\",\"prevent\",\"alert\",\"disable\"]', 
                err = '', 
                fqdn = '', 
                function = '', 
                function_id = '', 
                hostname = '', 
                image_id = '', 
                image_name = '', 
                interactive = True, 
                label = '', 
                labels = {
                    'key' : ''
                    }, 
                msg = '', 
                namespace = '', 
                os = '', 
                pid = 56, 
                process_path = '', 
                profile_id = '', 
                raw_event = '', 
                region = '', 
                request_id = '', 
                rule_name = '', 
                runtime = '[\"python\",\"python2.7\",\"python3.6\",\"python3.7\",\"python3.8\",\"nodejs10.x\",\"dotnetcore2.1\",\"java8\"]', 
                severity = '[\"low\",\"medium\",\"high\"]', 
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                type = '[\"processes\",\"network\",\"kubernetes\",\"filesystem\"]', 
                user = '', 
                version = ''
            )
        else :
            return SharedRuntimeAudit(
        )

    def testSharedRuntimeAudit(self):
        """Test SharedRuntimeAudit"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
