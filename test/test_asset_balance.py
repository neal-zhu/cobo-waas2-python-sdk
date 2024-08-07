# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.asset_balance import AssetBalance


class TestAssetBalance(unittest.TestCase):
    """AssetBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetBalance:
        """Test AssetBalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetBalance`
        """
        model = AssetBalance()
        if include_optional:
            return AssetBalance(
                asset_id = 'USDT',
                balance = cobo_waas2.models.token_balance_balance.TokenBalance_balance(
                    total = '100.0', 
                    available = '80.5', 
                    pending = '0', 
                    locked = '0', )
            )
        else:
            return AssetBalance(
                asset_id = 'USDT',
                balance = cobo_waas2.models.token_balance_balance.TokenBalance_balance(
                    total = '100.0', 
                    available = '80.5', 
                    pending = '0', 
                    locked = '0', ),
        )
        """

    def testAssetBalance(self):
        """Test AssetBalance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
