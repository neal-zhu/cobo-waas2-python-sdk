# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.cobo_safe_delegate import CoboSafeDelegate


class TestCoboSafeDelegate(unittest.TestCase):
    """CoboSafeDelegate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoboSafeDelegate:
        """Test CoboSafeDelegate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoboSafeDelegate`
        """
        model = CoboSafeDelegate()
        if include_optional:
            return CoboSafeDelegate(
                delegate_type = 'Org-Controlled',
                wallet_id = '123e4567-e89b-12d3-a456-426614174000',
                address = '0x1234567890123456789012345678901234567890'
            )
        else:
            return CoboSafeDelegate(
                delegate_type = 'Org-Controlled',
                wallet_id = '123e4567-e89b-12d3-a456-426614174000',
                address = '0x1234567890123456789012345678901234567890',
        )
        """

    def testCoboSafeDelegate(self):
        """Test CoboSafeDelegate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
