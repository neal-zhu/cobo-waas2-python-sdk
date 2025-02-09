# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_transfer_to_address_destination_utxo_outputs_inner import TransactionTransferToAddressDestinationUtxoOutputsInner


class TestTransactionTransferToAddressDestinationUtxoOutputsInner(unittest.TestCase):
    """TransactionTransferToAddressDestinationUtxoOutputsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionTransferToAddressDestinationUtxoOutputsInner:
        """Test TransactionTransferToAddressDestinationUtxoOutputsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionTransferToAddressDestinationUtxoOutputsInner`
        """
        model = TransactionTransferToAddressDestinationUtxoOutputsInner()
        if include_optional:
            return TransactionTransferToAddressDestinationUtxoOutputsInner(
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sDEMO',
                amount = '1.5'
            )
        else:
            return TransactionTransferToAddressDestinationUtxoOutputsInner(
        )
        """

    def testTransactionTransferToAddressDestinationUtxoOutputsInner(self):
        """Test TransactionTransferToAddressDestinationUtxoOutputsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
