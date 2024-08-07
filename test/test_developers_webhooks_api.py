# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2 import Configuration
from cobo_waas2.api.developers_webhooks_api import DevelopersWebhooksApi


class TestDevelopersWebhooksApi(unittest.TestCase):
    """DevelopersWebhooksApi unit test stubs"""

    def setUp(self) -> None:
        Configuration.set_default(Configuration(
            api_private_key="c203fccc02a2269ec486d9c32ff74b5ba6ab0cdb461ee1fb0dfc616109115c06",
            host="https://api.sandbox.cobo.com/v2"
        ))
        self.api = DevelopersWebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_create_webhook_endpoint(self) -> None:
        """
        Test case for create_webhook_endpoint

        Register webhook endpoint
        """
        """
        create_webhook_endpoint_request = cobo_waas2.CreateWebhookEndpointRequest()

        api_response = self.api.create_webhook_endpoint(create_webhook_endpoint_request=create_webhook_endpoint_request)
        """

    def test_get_webhook_endpoint_by_id(self) -> None:
        """
        Test case for get_webhook_endpoint_by_id

        Get webhook endpoint information
        """
        """
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_webhook_endpoint_by_id(endpoint_id)
        """

    def test_get_webhook_event_by_id(self) -> None:
        """
        Test case for get_webhook_event_by_id

        Retrieve event information
        """
        """
        event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.get_webhook_event_by_id(event_id, endpoint_id)
        """

    def test_list_webhook_endpoints(self) -> None:
        """
        Test case for list_webhook_endpoints

        List webhook endpoints
        """
        """
        status = cobo_waas2.WebhookEndpointStatus()
        event_type = cobo_waas2.WebhookEventType()
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_webhook_endpoints(status=status, event_type=event_type, limit=limit, before=before, after=after)
        """

    def test_list_webhook_event_definitions(self) -> None:
        """
        Test case for list_webhook_event_definitions

        Get webhook event types
        """
        """

        api_response = self.api.list_webhook_event_definitions()
        """

    def test_list_webhook_event_logs(self) -> None:
        """
        Test case for list_webhook_event_logs

        List webhook event logs
        """
        """
        event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_webhook_event_logs(event_id, endpoint_id, limit=limit, before=before, after=after)
        """

    def test_list_webhook_events(self) -> None:
        """
        Test case for list_webhook_events

        List all webhook events
        """
        """
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        status = cobo_waas2.WebhookEventStatus()
        type = cobo_waas2.WebhookEventType()
        limit = 10
        before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
        after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

        api_response = self.api.list_webhook_events(endpoint_id, status=status, type=type, limit=limit, before=before, after=after)
        """

    def test_retry_webhook_event_by_id(self) -> None:
        """
        Test case for retry_webhook_event_by_id

        Retry event
        """
        """
        event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

        api_response = self.api.retry_webhook_event_by_id(event_id, endpoint_id)
        """

    def test_update_webhook_endpoint_by_id(self) -> None:
        """
        Test case for update_webhook_endpoint_by_id

        Update webhook endpoint
        """
        """
        endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
        update_webhook_endpoint_by_id_request = cobo_waas2.UpdateWebhookEndpointByIdRequest()

        api_response = self.api.update_webhook_endpoint_by_id(endpoint_id, update_webhook_endpoint_by_id_request=update_webhook_endpoint_by_id_request)
        """


if __name__ == '__main__':
    unittest.main()
