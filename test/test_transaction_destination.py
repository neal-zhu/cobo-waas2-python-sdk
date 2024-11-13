# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_destination import TransactionDestination


class TestTransactionDestination(unittest.TestCase):
    """TransactionDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionDestination:
        """Test TransactionDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionDestination`
        """
        model = TransactionDestination()
        if include_optional:
            return TransactionDestination(
                destination_type = 'Address',
                account_output = cobo_waas2.models.transaction_transfer_to_address_destination_account_output.TransactionTransferToAddressDestination_account_output(
                    address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku', 
                    memo = '82840924', 
                    amount = '1.5', ),
                utxo_outputs = [
                    cobo_waas2.models.transaction_transfer_to_address_destination_utxo_outputs_inner.TransactionTransferToAddressDestination_utxo_outputs_inner(
                        address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sDEMO', 
                        amount = '1.5', )
                    ],
                change_address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sDEMO',
                force_internal = False,
                force_external = False,
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                trading_account_type = 'Asset',
                exchange_id = 'binance',
                amount = '1.5',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                value = '1.5',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
                calldata_info = cobo_waas2.models.transaction_evm_calldata_info.TransactionEvmCalldataInfo(
                    chain_id = 'ETH', 
                    address = '0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84', 
                    name = 'AppProxyUpgradeable', 
                    impl_address = '0x17144556fd3424edc8fc8a4c940b2d04936d17eb', 
                    impl_name = 'Lido', 
                    proxy = True, 
                    method = cobo_waas2.models.transaction_evm_contract_method.TransactionEvmContractMethod(
                        name = 'transfer', 
                        sig = 'transfer(address,uint256)', 
                        type = 'Function', 
                        payable = True, 
                        selector = '0xa9059cbb', ), 
                    params = '[["exactInput", "tuple", [["dstReceiver", "address", "0xbbff75515f6e924441c3d80af4714edf19911111"], ["wrappedToken", "address", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"], ["router", "uint256", "452312848583266388373324160887510303453432363010492966520592108215996663949"], ["amount", "uint256", "10000000000000000"], ["minReturnAmount", "uint256", "369987456553029"], ["fee", "uint256", "30000000000000"], ["path", "address[]", [["[0]", "address", "0x0000000000000000000000000000000000000000"], ["[1]", "address", "0x1ae21d57afc033a556ef63daa216046321b3d391"]]], ["pool", "address[]", [["[0]", "address", "0x725522665fa5e1fa2912fed453dc0044deda5cfd"]]], ["signature", "bytes", "0x"], ["channel", "string", "android"]]], ["deadline", "uint256", "1729582030"]]', ),
                message = 'YWFhYQ==',
                structured_data = {"types": {"EIP712Domain": [{"name": "name", "type": "string"}, {"name": "version", "type": "string"}, {"name": "chainId", "type": "uint256"}, {"name": "verifyingContract", "type": "address"}], "Person": [{"name": "name", "type": "string"}, {"name": "wallet", "type": "address"}], "Mail": [{"name": "from", "type": "Person"}, {"name": "to", "type": "Person"}, {"name": "contents", "type": "string"}]}, "primaryType": "Mail", "domain": {"name": "Ether Mail", "version": "1", "chainId": 1, "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"}, "message": {"from": {"name": "Cow", "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"}, "to": {"name": "Bob", "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"}, "contents": "Hello, Bob!"}}
,
                msg_hash = '',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                memo = '82840924'
            )
        else:
            return TransactionDestination(
                destination_type = 'Address',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                amount = '1.5',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
                message = 'YWFhYQ==',
                structured_data = {"types": {"EIP712Domain": [{"name": "name", "type": "string"}, {"name": "version", "type": "string"}, {"name": "chainId", "type": "uint256"}, {"name": "verifyingContract", "type": "address"}], "Person": [{"name": "name", "type": "string"}, {"name": "wallet", "type": "address"}], "Mail": [{"name": "from", "type": "Person"}, {"name": "to", "type": "Person"}, {"name": "contents", "type": "string"}]}, "primaryType": "Mail", "domain": {"name": "Ether Mail", "version": "1", "chainId": 1, "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"}, "message": {"from": {"name": "Cow", "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"}, "to": {"name": "Bob", "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"}, "contents": "Hello, Bob!"}}
,
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
        )
        """

    def testTransactionDestination(self):
        """Test TransactionDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
