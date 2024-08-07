# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_request_evm_eip1559_fee import TransactionRequestEvmEip1559Fee


class TestTransactionRequestEvmEip1559Fee(unittest.TestCase):
    """TransactionRequestEvmEip1559Fee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequestEvmEip1559Fee:
        """Test TransactionRequestEvmEip1559Fee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRequestEvmEip1559Fee`
        """
        model = TransactionRequestEvmEip1559Fee()
        if include_optional:
            return TransactionRequestEvmEip1559Fee(
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                gas_limit = '21000'
            )
        else:
            return TransactionRequestEvmEip1559Fee(
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
        )
        """

    def testTransactionRequestEvmEip1559Fee(self):
        """Test TransactionRequestEvmEip1559Fee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
