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
from cobo_waas2.models.address_encoding import AddressEncoding
from typing import Optional, Set
from typing_extensions import Self


class AddressInfo(BaseModel):
    """
    The address information.
    """  # noqa: E501
    address: StrictStr = Field(description="The wallet address.")
    chain_id: StrictStr = Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains).")
    memo: Optional[StrictStr] = Field(default=None, description="The memo code.")
    path: Optional[StrictStr] = Field(default=None, description="The derivation path of the address. This property applies to MPC Wallets only.")
    encoding: Optional[AddressEncoding] = None
    pubkey: Optional[StrictStr] = Field(default=None, description="The public key of the address. This property applies to MPC Wallets only.")
    __properties: ClassVar[List[str]] = ["address", "chain_id", "memo", "path", "encoding", "pubkey"]

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
        """Create an instance of AddressInfo from a JSON string"""
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
        """Create an instance of AddressInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "chain_id": obj.get("chain_id"),
            "memo": obj.get("memo"),
            "path": obj.get("path"),
            "encoding": obj.get("encoding"),
            "pubkey": obj.get("pubkey")
        })
        return _obj


