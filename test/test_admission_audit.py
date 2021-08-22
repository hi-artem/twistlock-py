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
from openapi_client.models.admission_audit import AdmissionAudit  # noqa: E501
from openapi_client.rest import ApiException

class TestAdmissionAudit(unittest.TestCase):
    """AdmissionAudit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdmissionAudit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.admission_audit.AdmissionAudit()  # noqa: E501
        if include_optional :
            return AdmissionAudit(
                account_id = '', 
                attack_techniques = [
                    '[\"exploitationForPrivilegeEscalation\",\"exploitPublicFacingApplication\",\"applicationExploitRCE\",\"networkServiceScanning\",\"endpointDenialOfService\",\"exfiltrationGeneral\",\"systemNetworkConfigurationDiscovery\",\"unsecuredCredentials\",\"credentialDumping\",\"systemInformationDiscovery\",\"systemNetworkConnectionDiscovery\",\"systemUserDiscovery\",\"accountDiscovery\",\"cloudInstanceMetadataAPI\",\"accessKubeletMainAPI\",\"queryKubeletReadonlyAPI\",\"accessKubernetesAPIServer\",\"softwareDeploymentTools\",\"ingressToolTransfer\",\"lateralToolTransfer\",\"commandAndControlGeneral\",\"resourceHijacking\",\"manInTheMiddle\",\"nativeBinaryExecution\",\"foreignBinaryExecution\",\"createAccount\",\"accountManipulation\",\"abuseElevationControlMechanisms\",\"supplyChainCompromise\",\"obfuscatedFiles\",\"hijackExecutionFlow\",\"impairDefences\",\"scheduledTaskJob\",\"exploitationOfRemoteServices\",\"eventTriggeredExecution\",\"accountAccessRemoval\",\"privilegedContainer\",\"writableVolumes\",\"execIntoContainer\",\"softwareDiscovery\",\"createContainer\",\"kubernetesSecrets\",\"fileAndDirectoryDiscovery\",\"masquerading\",\"webShell\",\"compileAfterDelivery\"]'
                    ], 
                cluster = '', 
                collections = [
                    ''
                    ], 
                effect = '', 
                kind = '', 
                message = '', 
                namespace = '', 
                operation = '', 
                raw_request = '', 
                resource = '', 
                rule_name = '', 
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user_groups = '', 
                user_uid = '', 
                username = ''
            )
        else :
            return AdmissionAudit(
        )

    def testAdmissionAudit(self):
        """Test AdmissionAudit"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
