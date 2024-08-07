# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.delete_wallet_by_id201_response import DeleteWalletById201Response


class TestDeleteWalletById201Response(unittest.TestCase):
    """DeleteWalletById201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteWalletById201Response:
        """Test DeleteWalletById201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteWalletById201Response`
        """
        model = DeleteWalletById201Response()
        if include_optional:
            return DeleteWalletById201Response(
                submitted = True
            )
        else:
            return DeleteWalletById201Response(
                submitted = True,
        )
        """

    def testDeleteWalletById201Response(self):
        """Test DeleteWalletById201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
