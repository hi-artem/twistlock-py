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
from openapi_client.models.defender_status import DefenderStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestDefenderStatus(unittest.TestCase):
    """DefenderStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DefenderStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.defender_status.DefenderStatus()  # noqa: E501
        if include_optional :
            return DefenderStatus(
                app_firewall = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                container = openapi_client.models.defender/scan_status.defender.ScanStatus(
                    completed = True, 
                    errors = [
                        ''
                        ], 
                    hostname = '', 
                    scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    scanning = True, 
                    selective = True, ), 
                container_network_firewall = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                features = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                filesystem = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                host_custom_compliance = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                host_network_firewall = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                image = openapi_client.models.defender/scan_status.defender.ScanStatus(
                    completed = True, 
                    errors = [
                        ''
                        ], 
                    hostname = '', 
                    scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    scanning = True, 
                    selective = True, ), 
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                network = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                process = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                registry = openapi_client.models.defender/scan_status.defender.ScanStatus(
                    completed = True, 
                    errors = [
                        ''
                        ], 
                    hostname = '', 
                    scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    scanning = True, 
                    selective = True, ), 
                runc = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                runtime = openapi_client.models.defender/feature_status.defender.FeatureStatus(
                    enabled = True, 
                    err,omiztempty = '', 
                    hostname = '', ), 
                tas_droplets = openapi_client.models.defender/scan_status.defender.ScanStatus(
                    completed = True, 
                    errors = [
                        ''
                        ], 
                    hostname = '', 
                    scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    scanning = True, 
                    selective = True, ), 
                upgrade = openapi_client.models.defender/upgrade_status.defender.UpgradeStatus(
                    err = '', 
                    hostname = '', 
                    last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    progress = 56, )
            )
        else :
            return DefenderStatus(
        )

    def testDefenderStatus(self):
        """Test DefenderStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
