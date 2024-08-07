# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.address_transfer_destination_account_output import AddressTransferDestinationAccountOutput


class TestAddressTransferDestinationAccountOutput(unittest.TestCase):
    """AddressTransferDestinationAccountOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressTransferDestinationAccountOutput:
        """Test AddressTransferDestinationAccountOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTransferDestinationAccountOutput`
        """
        model = AddressTransferDestinationAccountOutput()
        if include_optional:
            return AddressTransferDestinationAccountOutput(
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                memo = '82840924',
                amount = '1.5'
            )
        else:
            return AddressTransferDestinationAccountOutput(
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                amount = '1.5',
        )
        """

    def testAddressTransferDestinationAccountOutput(self):
        """Test AddressTransferDestinationAccountOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
