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
from openapi_client.models.identity_settings import IdentitySettings  # noqa: E501
from openapi_client.rest import ApiException

class TestIdentitySettings(unittest.TestCase):
    """IdentitySettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IdentitySettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.identity_settings.IdentitySettings()  # noqa: E501
        if include_optional :
            return IdentitySettings(
                ldap = openapi_client.models.identity/ldap_settings.identity.LdapSettings(
                    account_password = openapi_client.models.common/secret.common.Secret(
                        encrypted = '', 
                        plain = '', ), 
                    account_upn = '', 
                    ca_cert = '', 
                    enabled = True, 
                    group_search_base = '', 
                    search_base = '', 
                    type = '', 
                    url = '', 
                    user_search_base = '', 
                    user_search_identifier = '', ), 
                oauth = openapi_client.models.identity/provider_settings.identity.ProviderSettings(
                    auth_url = '', 
                    cert = '', 
                    client_id = '', 
                    client_secret = openapi_client.models.common/secret.common.Secret(
                        encrypted = '', 
                        plain = '', ), 
                    enabled = True, 
                    group_claim = '', 
                    group_scope = '', 
                    open_id_issues_url = '', 
                    openshift_base_url = '', 
                    provider_alias = '', 
                    provider_name = '[\"github\",\"openshift\"]', 
                    token_url = '', ), 
                openid = openapi_client.models.identity/provider_settings.identity.ProviderSettings(
                    auth_url = '', 
                    cert = '', 
                    client_id = '', 
                    client_secret = openapi_client.models.common/secret.common.Secret(
                        encrypted = '', 
                        plain = '', ), 
                    enabled = True, 
                    group_claim = '', 
                    group_scope = '', 
                    open_id_issues_url = '', 
                    openshift_base_url = '', 
                    provider_alias = '', 
                    provider_name = '[\"github\",\"openshift\"]', 
                    token_url = '', ), 
                saml = openapi_client.models.identity/saml_settings.identity.SamlSettings(
                    app_id = '', 
                    app_secret = openapi_client.models.common/secret.common.Secret(
                        encrypted = '', 
                        plain = '', ), 
                    audience = '', 
                    cert = '', 
                    console_url = '', 
                    enabled = True, 
                    issuer = '', 
                    provider_alias = '', 
                    skip_authn_context = True, 
                    tenant_id = '', 
                    type = '[\"okta\",\"gsuite\",\"ping\",\"shibboleth\",\"azure\",\"adfs\"]', 
                    url = '', )
            )
        else :
            return IdentitySettings(
        )

    def testIdentitySettings(self):
        """Test IdentitySettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
