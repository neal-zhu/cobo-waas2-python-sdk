# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.evm_legacy_fee_base_price import EvmLegacyFeeBasePrice


class TestEvmLegacyFeeBasePrice(unittest.TestCase):
    """EvmLegacyFeeBasePrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvmLegacyFeeBasePrice:
        """Test EvmLegacyFeeBasePrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvmLegacyFeeBasePrice`
        """
        model = EvmLegacyFeeBasePrice()
        if include_optional:
            return EvmLegacyFeeBasePrice(
                gas_price = '100000000'
            )
        else:
            return EvmLegacyFeeBasePrice(
        )
        """

    def testEvmLegacyFeeBasePrice(self):
        """Test EvmLegacyFeeBasePrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
