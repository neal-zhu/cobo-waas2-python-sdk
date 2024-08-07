# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_timeline import TransactionTimeline


class TestTransactionTimeline(unittest.TestCase):
    """TransactionTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionTimeline:
        """Test TransactionTimeline
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionTimeline`
        """
        model = TransactionTimeline()
        if include_optional:
            return TransactionTimeline(
                status = 'Submitted',
                finished = True,
                finished_timestamp = 1610445878970
            )
        else:
            return TransactionTimeline(
        )
        """

    def testTransactionTimeline(self):
        """Test TransactionTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
