# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.activity_timeline import ActivityTimeline


class TestActivityTimeline(unittest.TestCase):
    """ActivityTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityTimeline:
        """Test ActivityTimeline
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityTimeline`
        """
        model = ActivityTimeline()
        if include_optional:
            return ActivityTimeline(
                action = 'Submitted',
                status = 'success',
                timestamp = 1640995200000,
                transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f'
            )
        else:
            return ActivityTimeline(
                action = 'Submitted',
        )
        """

    def testActivityTimeline(self):
        """Test ActivityTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
