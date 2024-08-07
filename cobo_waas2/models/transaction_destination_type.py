# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionDestinationType(str, Enum):
    """
    The transaction destination type. Possible values include:   - `Address`: An address transfer destination, including an address of Custodial Wallets, MPC Wallets, or Smart Contract Wallets (Safe{Wallet}) and an external address.   - `ExchangeWallet`: An Exchange Wallet transfer destination.   - `EVM_Contract`: An EVM compatible contract.   - `EVM_EIP_191_Signature`: An EVM EIP-191 signature. For more details, see [Signed Data Standard](https://eips.ethereum.org/EIPS/eip-191).   - `EVM_EIP_712_Signature`: An EVM EIP-712 signature. For more details, see [Typed structured data hashing and signing](https://eips.ethereum.org/EIPS/eip-712).   - `DepositToAddress`: An address that can be a Cobo's wallet address or an external address.   - `DepositToWallet`: An Exchange Wallet.  For the same transaction, the transaction destination varies depending on whether you are the initiator or the receiver of the transaction.     - As the initiator, you will see detailed information about the transaction destination, and the `destination` will be displayed as one of the following types: `EVM_Contract`, `EVM_EIP_191_Signature`, `EVM_EIP_712_Signature`, `DepositToAddress`, or `DepositToWallet`. `DepositToWallet` indicates the destination is an Exchange Wallet, while `DepositToAddress` indicates the destination is a wallet of other wallet types or an external address.   - As the receiver, you will see the `destination` as the type `Address` or `ExchangeWallet`. `Address` indicates the destination is a wallet of other wallet types than Exchange Wallets or an external address. 
    """

    """
    allowed enum values
    """
    ADDRESS = 'Address'
    EXCHANGEWALLET = 'ExchangeWallet'
    EVM_CONTRACT = 'EVM_Contract'
    EVM_EIP_191_SIGNATURE = 'EVM_EIP_191_Signature'
    EVM_EIP_712_SIGNATURE = 'EVM_EIP_712_Signature'
    DEPOSITTOADDRESS = 'DepositToAddress'
    DEPOSITTOWALLET = 'DepositToWallet'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionDestinationType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


