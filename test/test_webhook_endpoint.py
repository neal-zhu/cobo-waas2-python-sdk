# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.webhook_endpoint import WebhookEndpoint


class TestWebhookEndpoint(unittest.TestCase):
    """WebhookEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEndpoint:
        """Test WebhookEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEndpoint`
        """
        model = WebhookEndpoint()
        if include_optional:
            return WebhookEndpoint(
                url = 'https://example.com/webhook',
                subscribed_events = [
                    'wallets.transaction.created'
                    ],
                created_timestamp = 1701396866000,
                endpoint_id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f',
                status = 'STATUS_ACTIVE',
                description = 'My webhook endpoint'
            )
        else:
            return WebhookEndpoint(
                url = 'https://example.com/webhook',
                subscribed_events = [
                    'wallets.transaction.created'
                    ],
                created_timestamp = 1701396866000,
                status = 'STATUS_ACTIVE',
        )
        """

    def testWebhookEndpoint(self):
        """Test WebhookEndpoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
