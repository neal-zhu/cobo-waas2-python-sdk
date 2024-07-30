# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.contract_call_params import ContractCallParams


class TestContractCallParams(unittest.TestCase):
    """ContractCallParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractCallParams:
        """Test ContractCallParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractCallParams`
        """
        model = ContractCallParams()
        if include_optional:
            return ContractCallParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                chain_id = 'ETH',
                source = None,
                destination = None,
                description = 'Transaction to call a smart contract initiated from a wallet',
                category_names = [
                    'Trading'
                    ],
                fee = None
            )
        else:
            return ContractCallParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                chain_id = 'ETH',
                source = None,
                destination = None,
        )
        """

    def testContractCallParams(self):
        """Test ContractCallParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()