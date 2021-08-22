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
from openapi_client.models.forensic_container_event import ForensicContainerEvent  # noqa: E501
from openapi_client.rest import ApiException

class TestForensicContainerEvent(unittest.TestCase):
    """ForensicContainerEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ForensicContainerEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.forensic_container_event.ForensicContainerEvent()  # noqa: E501
        if include_optional :
            return ForensicContainerEvent(
                all_ports = True, 
                attack = '[\"\",\"cloudMetadataProbing\",\"kubeletAPIAccess\",\"kubeletReadonlyAccess\",\"kubectlSpawned\",\"kubectlDownloaded\",\"horizontalPortScanning\",\"verticalPortScanning\",\"explicitlyDeniedIP\",\"customFeedIP\",\"feedIP\",\"unexpectedOutboundPort\",\"suspiciousNetworkActivity\",\"unexpectedListeningPort\",\"explicitlyDeniedListeningPort\",\"explicitlyDeniedOutboundPort\",\"listeningPortModifiedProcess\",\"outboundPortModifiedProcess\",\"feedDNS\",\"explicitlyDeniedDNS\",\"dnsQuery\",\"unexpectedProcess\",\"portScanProcess\",\"malwareProcessCustom\",\"malwareProcessFeed\",\"explicitlyDeniedProcess\",\"modifiedProcess\",\"cryptoMinerProcess\",\"lateralMovementProcess\",\"tmpfsProcess\",\"policyHijacked\",\"reverseShell\",\"suidBinaries\",\"unknownOriginBinary\",\"webShell\",\"administrativeAccount\",\"encryptedBinary\",\"sshAccess\",\"explicitlyDeniedFile\",\"malwareFileCustom\",\"malwareFileFeed\",\"execFileAccess\",\"elfFileAccess\",\"secretFileAccess\",\"regFileAccess\",\"wildfireMalware\",\"unknownOriginBinary\",\"webShell\",\"fileIntegrity\",\"alteredBinary\",\"malwareDownloaded\",\"suspiciousELFHeader\",\"executionFlowHijackAttempt\",\"customRule\"]', 
                category = '[\"portScanning\",\"hijackedProcess\",\"dataExfiltration\",\"kubernetes\",\"backdoorAdministrativeAccount\",\"backdoorSSHAccess\",\"cryptoMiner\",\"lateralMovement\",\"bruteForce\",\"customRule\",\"alteredBinary\",\"suspiciousBinary\",\"executionFlowHijackAttempt\",\"reverseShell\",\"malware\"]', 
                command = '', 
                container_id = '', 
                dst_ip = '', 
                dst_port = 56, 
                dst_profile_id = '', 
                effect = '', 
                listening_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '', 
                network_collection_type = '', 
                outbound = True, 
                path = '', 
                pid = 56, 
                port = 56, 
                ppid = 56, 
                process = '', 
                src_ip = '', 
                src_profile_id = '', 
                static = True, 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                type = '[\"Process spawned\",\"Binary created\",\"Container started\",\"Listening port\",\"Connection established\",\"Runtime audit\",\"Runtime profile process\",\"Runtime profile filesystem\",\"Runtime profile networking\",\"Incident\"]', 
                user = ''
            )
        else :
            return ForensicContainerEvent(
        )

    def testForensicContainerEvent(self):
        """Test ForensicContainerEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
