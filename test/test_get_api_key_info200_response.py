# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.get_api_key_info200_response import GetApiKeyInfo200Response


class TestGetApiKeyInfo200Response(unittest.TestCase):
    """GetApiKeyInfo200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiKeyInfo200Response:
        """Test GetApiKeyInfo200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiKeyInfo200Response`
        """
        model = GetApiKeyInfo200Response()
        if include_optional:
            return GetApiKeyInfo200Response(
                name = 'my_api_key',
                curve_type = 'ED25519',
                key = '427b06814cca3359bd0e710c1187833b7f052748a3fdf59888fad4ddc4bd379f',
                callback_url = 'https://example.com/api/callback',
                valid_ips = [
                    '127.0.0.1'
                    ],
                created_timestamp = 1701396866000,
                updated_timestamp = 1701396866000,
                expired_timestamp = 1701396866000,
                role_scopes = [
                    cobo_waas2.models.role_scopes.RoleScopes(
                        role_name = 'API_Spender', 
                        scopes = cobo_waas2.models.scopes.Scopes(
                            wallet_types = [
                                'Custodial'
                                ], 
                            wallet_subtypes = [
                                'Asset'
                                ], 
                            wallet_ids = [
                                'f47ac10b-58cc-4372-a567-0e02b2c3d479'
                                ], 
                            vault_ids = [
                                'f47ac10b-58cc-4372-a567-0e02b2c3d479'
                                ], 
                            project_ids = [
                                'f47ac10b-58cc-4372-a567-0e02b2c3d479'
                                ], ), )
                    ]
            )
        else:
            return GetApiKeyInfo200Response(
                name = 'my_api_key',
                curve_type = 'ED25519',
                key = '427b06814cca3359bd0e710c1187833b7f052748a3fdf59888fad4ddc4bd379f',
                created_timestamp = 1701396866000,
                updated_timestamp = 1701396866000,
        )
        """

    def testGetApiKeyInfo200Response(self):
        """Test GetApiKeyInfo200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
