# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.eigen_layer_native_stake_extra import EigenLayerNativeStakeExtra


class TestEigenLayerNativeStakeExtra(unittest.TestCase):
    """EigenLayerNativeStakeExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EigenLayerNativeStakeExtra:
        """Test EigenLayerNativeStakeExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EigenLayerNativeStakeExtra`
        """
        model = EigenLayerNativeStakeExtra()
        if include_optional:
            return EigenLayerNativeStakeExtra(
                pool_type = 'Babylon',
                fee_recipient = 30
            )
        else:
            return EigenLayerNativeStakeExtra(
                pool_type = 'Babylon',
        )
        """

    def testEigenLayerNativeStakeExtra(self):
        """Test EigenLayerNativeStakeExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
