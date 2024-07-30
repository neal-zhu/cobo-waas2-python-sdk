# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_addresses200_response import ListAddresses200Response


class TestListAddresses200Response(unittest.TestCase):
    """ListAddresses200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAddresses200Response:
        """Test ListAddresses200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAddresses200Response`
        """
        model = ListAddresses200Response()
        if include_optional:
            return ListAddresses200Response(
                data = [
                    cobo_waas2.models.address_info.AddressInfo(
                        address = '0x0000000000000000000000000000000000000000', 
                        chain_id = 'ETH', 
                        memo = '82840924', 
                        path = 'm/44'/60'/0'/0', 
                        encoding = 'ENCODING_P2PKH', 
                        pubkey = 'xpub661MyMwAqRbcG4vPNi58VQJrXW8D9VzmauuRq2rTY3oUVnKGuLTxQxvvoEXgLvZ7N9GQXQkWVgKn1rzEUUEm4NdvrBKUqjpNJEnn2UL4rYq', )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListAddresses200Response(
        )
        """

    def testListAddresses200Response(self):
        """Test ListAddresses200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()