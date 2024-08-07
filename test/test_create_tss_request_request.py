# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_tss_request_request import CreateTssRequestRequest


class TestCreateTssRequestRequest(unittest.TestCase):
    """CreateTssRequestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTssRequestRequest:
        """Test CreateTssRequestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTssRequestRequest`
        """
        model = CreateTssRequestRequest()
        if include_optional:
            return CreateTssRequestRequest(
                type = 'Recovery',
                target_key_share_holder_group_id = 'a1bf161f-8b60-4f61-9c35-6434b8654437',
                source_key_share_holder_group = cobo_waas2.models.source_group.SourceGroup(
                    key_share_holder_group_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                    tss_node_ids = [
                        'cobo5yb7BNEBwwp5XXedbhnzQfvQtp132W4dH4Jz4x4eDp4KA'
                        ], )
            )
        else:
            return CreateTssRequestRequest(
                type = 'Recovery',
                target_key_share_holder_group_id = 'a1bf161f-8b60-4f61-9c35-6434b8654437',
        )
        """

    def testCreateTssRequestRequest(self):
        """Test CreateTssRequestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
