# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class TransactionRequestEvmLegacyFee(BaseModel):
    """
    In the legacy fee model, the transaction fee is calculated by multiplying the gas price by the gas units used by the transaction. This can be expressed as: Transaction fee =  (gas price * gas units used).   You can specify the gas limit to limit the gas units used in the transaction. 
    """  # noqa: E501
    gas_price: StrictStr = Field(description="The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used.")
    fee_type: FeeType
    token_id: StrictStr = Field(description="The token ID of the transaction fee.")
    gas_limit: Optional[StrictStr] = Field(default='21000', description="The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies.")
    __properties: ClassVar[List[str]] = ["gas_price", "fee_type", "token_id", "gas_limit"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionRequestEvmLegacyFee from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionRequestEvmLegacyFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gas_price": obj.get("gas_price"),
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "gas_limit": obj.get("gas_limit") if obj.get("gas_limit") is not None else '21000'
        })
        return _obj


