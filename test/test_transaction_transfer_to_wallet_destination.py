# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_transfer_to_wallet_destination import TransactionTransferToWalletDestination


class TestTransactionTransferToWalletDestination(unittest.TestCase):
    """TransactionTransferToWalletDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionTransferToWalletDestination:
        """Test TransactionTransferToWalletDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionTransferToWalletDestination`
        """
        model = TransactionTransferToWalletDestination()
        if include_optional:
            return TransactionTransferToWalletDestination(
                destination_type = 'Address',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                sub_wallet_id = 'Asset',
                exchange_id = 'binance',
                amount = '1.5'
            )
        else:
            return TransactionTransferToWalletDestination(
                destination_type = 'Address',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                amount = '1.5',
        )
        """

    def testTransactionTransferToWalletDestination(self):
        """Test TransactionTransferToWalletDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
