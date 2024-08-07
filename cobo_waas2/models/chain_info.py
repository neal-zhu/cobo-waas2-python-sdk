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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class ChainInfo(BaseModel):
    """
    The chain information.
    """  # noqa: E501
    chain_id: StrictStr = Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains).")
    symbol: Optional[StrictStr] = Field(default=None, description="The chain symbol, which is the abbreviated name of a chain.")
    icon_url: Optional[StrictStr] = Field(default=None, description="The URL of the chain icon.")
    explorer_tx_url: Optional[StrictStr] = Field(default=None, description="The transaction URL pattern on the blockchain explorer. You can use it to concatenate the transaction URLs.")
    explorer_address_url: Optional[StrictStr] = Field(default=None, description="The address URL pattern on the blockchain explorer. You can use it to concatenate the address URLs.")
    require_memo: Optional[StrictBool] = Field(default=None, description="Whether the chain requires a memo.")
    __properties: ClassVar[List[str]] = ["chain_id", "symbol", "icon_url", "explorer_tx_url", "explorer_address_url", "require_memo"]

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
        """Create an instance of ChainInfo from a JSON string"""
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
        """Create an instance of ChainInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chain_id": obj.get("chain_id"),
            "symbol": obj.get("symbol"),
            "icon_url": obj.get("icon_url"),
            "explorer_tx_url": obj.get("explorer_tx_url"),
            "explorer_address_url": obj.get("explorer_address_url"),
            "require_memo": obj.get("require_memo")
        })
        return _obj


