# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.mpc_transfer_source import MpcTransferSource


class TestMpcTransferSource(unittest.TestCase):
    """MpcTransferSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MpcTransferSource:
        """Test MpcTransferSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MpcTransferSource`
        """
        model = MpcTransferSource()
        if include_optional:
            return MpcTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                included_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ],
                excluded_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ]
            )
        else:
            return MpcTransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testMpcTransferSource(self):
        """Test MpcTransferSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
