# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.pool_details_all_of_validators_info import PoolDetailsAllOfValidatorsInfo


class TestPoolDetailsAllOfValidatorsInfo(unittest.TestCase):
    """PoolDetailsAllOfValidatorsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PoolDetailsAllOfValidatorsInfo:
        """Test PoolDetailsAllOfValidatorsInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PoolDetailsAllOfValidatorsInfo`
        """
        model = PoolDetailsAllOfValidatorsInfo()
        if include_optional:
            return PoolDetailsAllOfValidatorsInfo(
                pool_type = 'Babylon',
                icon_url = 'https://example.com/icon.png',
                name = 'Cobo',
                priority = 0,
                public_key = 'eca1b104dce16c30705f4147a9c4a373ac88646c5d1bcda6a89c018940cb96a0',
                commission_rate = 0.1,
                supported_pos_chains = ["Babylon","Cosmos","Ethereum"]
            )
        else:
            return PoolDetailsAllOfValidatorsInfo(
                pool_type = 'Babylon',
                icon_url = 'https://example.com/icon.png',
                name = 'Cobo',
                public_key = 'eca1b104dce16c30705f4147a9c4a373ac88646c5d1bcda6a89c018940cb96a0',
                commission_rate = 0.1,
                supported_pos_chains = ["Babylon","Cosmos","Ethereum"],
        )
        """

    def testPoolDetailsAllOfValidatorsInfo(self):
        """Test PoolDetailsAllOfValidatorsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
