# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.exchange_wallet_info import ExchangeWalletInfo


class TestExchangeWalletInfo(unittest.TestCase):
    """ExchangeWalletInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeWalletInfo:
        """Test ExchangeWalletInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeWalletInfo`
        """
        model = ExchangeWalletInfo()
        if include_optional:
            return ExchangeWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                exchange_id = 'binance',
                parent_wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                sub_accounts = [
                    cobo_waas2.models.exchange_wallet_info_all_of_sub_accounts.ExchangeWalletInfo_allOf_sub_accounts(
                        wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                        account_id = 'sub01@xx.com', )
                    ]
            )
        else:
            return ExchangeWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                exchange_id = 'binance',
        )
        """

    def testExchangeWalletInfo(self):
        """Test ExchangeWalletInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()