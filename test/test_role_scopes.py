# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.role_scopes import RoleScopes


class TestRoleScopes(unittest.TestCase):
    """RoleScopes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleScopes:
        """Test RoleScopes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleScopes`
        """
        model = RoleScopes()
        if include_optional:
            return RoleScopes(
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
                        ], )
            )
        else:
            return RoleScopes(
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
                        ], ),
        )
        """

    def testRoleScopes(self):
        """Test RoleScopes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
