# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_stakings200_response import ListStakings200Response


class TestListStakings200Response(unittest.TestCase):
    """ListStakings200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListStakings200Response:
        """Test ListStakings200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListStakings200Response`
        """
        model = ListStakings200Response()
        if include_optional:
            return ListStakings200Response(
                data = [
                    cobo_waas2.models.stakings.Stakings(
                        id = '0011039d-27fb-49ba-b172-6e0aa80e37ec', 
                        wallet_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec', 
                        address = '0xAbCdE123456789aBcDeF123456789aBcDeF12345', 
                        amounts = [
                            cobo_waas2.models.amount_details_inner.AmountDetails_inner(
                                status = 'Active', 
                                amount = '100.00', )
                            ], 
                        pool_id = 'babylon_btc', 
                        token_id = 'BTC', 
                        rewards_info = {}, 
                        created_timestamp = 1640995200000, 
                        updated_timestamp = 1640995200000, 
                        validator_info = cobo_waas2.models.stakings_validator_info.Stakings_validator_info(
                            icon_url = 'https://example.com/logo.png', 
                            public_key = 'eca1b104dce16c30705f4147a9c4a373ac88646c5d1bcda6a89c018940cb96a0', 
                            name = 'Cobo', 
                            address = '0xAbCdE123456789aBcDeF123456789aBcDeF12345', 
                            commission_rate = '0.1', ), 
                        extra = null, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListStakings200Response(
        )
        """

    def testListStakings200Response(self):
        """Test ListStakings200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()