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
from openapi_client.models.serverless_radar_data import ServerlessRadarData  # noqa: E501
from openapi_client.rest import ApiException

class TestServerlessRadarData(unittest.TestCase):
    """ServerlessRadarData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ServerlessRadarData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.serverless_radar_data.ServerlessRadarData()  # noqa: E501
        if include_optional :
            return ServerlessRadarData(
                serverless_radar = [
                    openapi_client.models.serverless/radar_entity.serverless.RadarEntity(
                        _id = '', 
                        account_id = '', 
                        alias = True, 
                        application_name = '', 
                        associated_versions = [
                            openapi_client.models.serverless/associated_version.serverless.AssociatedVersion(
                                version = '', 
                                weight = '', )
                            ], 
                        collections = [
                            ''
                            ], 
                        compliance_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), 
                        credential_id = '', 
                        defended = True, 
                        description = '', 
                        incident_count = 56, 
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        network_count = 56, 
                        permissions = [
                            openapi_client.models.serverless/permissions.serverless.Permissions(
                                actions = [
                                    openapi_client.models.serverless/action_resources.serverless.ActionResources(
                                        resources = [
                                            openapi_client.models.serverless/resource.serverless.Resource(
                                                allow = True, 
                                                condition = [
                                                    openapi_client.models.serverless/condition.serverless.Condition(
                                                        conditions = [
                                                            openapi_client.models.shared/key_values.shared.KeyValues(
                                                                key = '', 
                                                                values = [
                                                                    ''
                                                                    ], )
                                                            ], 
                                                        name = '', )
                                                    ], 
                                                name = '', 
                                                negate = True, )
                                            ], 
                                        service_api = openapi_client.models.serverless/service_api.serverless.ServiceAPI(
                                            api = '', 
                                            negate = True, 
                                            service = '', ), )
                                    ], 
                                service = '', )
                            ], 
                        permissions_boundary = [
                            openapi_client.models.serverless/permissions.serverless.Permissions(
                                service = '', )
                            ], 
                        processes_count = 56, 
                        provider = '[\"aws\",\"azure\",\"gcp\",\"alibaba\",\"others\"]', 
                        region = '', 
                        runtime = '', 
                        scanned = True, 
                        tags = [
                            openapi_client.models.common/external_label.common.ExternalLabel(
                                key = '', 
                                source_name = '', 
                                source_type = '[\"namespace\",\"deployment\",\"aws\",\"azure\",\"gcp\"]', 
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                value = '', )
                            ], 
                        triggers = [
                            openapi_client.models.serverless/triggers.serverless.Triggers(
                                service = '', )
                            ], 
                        version = '', 
                        vulnerability_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), )
                    ]
            )
        else :
            return ServerlessRadarData(
        )

    def testServerlessRadarData(self):
        """Test ServerlessRadarData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
