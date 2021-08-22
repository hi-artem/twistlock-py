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
from openapi_client.models.waas_bot_protection_spec import WaasBotProtectionSpec  # noqa: E501
from openapi_client.rest import ApiException

class TestWaasBotProtectionSpec(unittest.TestCase):
    """WaasBotProtectionSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WaasBotProtectionSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.waas_bot_protection_spec.WaasBotProtectionSpec()  # noqa: E501
        if include_optional :
            return WaasBotProtectionSpec(
                interstitial_page = True, 
                js_injection_spec = openapi_client.models.waas/js_injection_spec.waas.JSInjectionSpec(
                    enabled = True, 
                    timeout_effect = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', ), 
                known_bot_protections_spec = openapi_client.models.waas/known_bot_protections_spec.waas.KnownBotProtectionsSpec(
                    archiving = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    business_analytics = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    career_search = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    content_feed_clients = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    educational = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    financial = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    media_search = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    news = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                    search_engine_crawlers = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', ), 
                re_captcha_spec = openapi_client.models.waas/re_captcha_spec.waas.ReCAPTCHASpec(
                    all_sessions = True, 
                    enabled = True, 
                    secret_key = openapi_client.models.common/secret.common.Secret(
                        encrypted = '', 
                        plain = '', ), 
                    site_key = '', 
                    success_expiration_hours = 56, 
                    type = '[\"checkbox\",\"invisible\"]', ), 
                session_validation = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                unknown_bot_protection_spec = ERROR_TO_EXAMPLE_VALUE, 
                user_defined_bots = [
                    openapi_client.models.waas/user_defined_bot.waas.UserDefinedBot(
                        effect = '[\"ban\",\"prevent\",\"alert\",\"allow\",\"disable\",\"reCAPTCHA\"]', 
                        header_name = '', 
                        header_values = [
                            ''
                            ], 
                        name = '', 
                        subnets = [
                            ''
                            ], )
                    ]
            )
        else :
            return WaasBotProtectionSpec(
        )

    def testWaasBotProtectionSpec(self):
        """Test WaasBotProtectionSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
