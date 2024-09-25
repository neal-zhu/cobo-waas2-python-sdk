# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.wallet_type import WalletType
from typing import Optional, Set
from typing_extensions import Self


class AddressBook(BaseModel):
    """
    The data for address book entry information.
    """  # noqa: E501
    org_id: StrictStr
    entry_id: StrictStr
    address: StrictStr = Field(description="address.")
    memo: Optional[StrictStr] = Field(default=None, description="memo.")
    wallet_name: Optional[StrictStr] = Field(default=None, description="wallet name.")
    wallet_type: Optional[WalletType] = None
    label: StrictStr = Field(description="The label to address.")
    email: Optional[StrictStr] = Field(default=None, description="email.")
    __properties: ClassVar[List[str]] = ["org_id", "entry_id", "address", "memo", "wallet_name", "wallet_type", "label", "email"]

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
        """Create an instance of AddressBook from a JSON string"""
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
        """Create an instance of AddressBook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "org_id": obj.get("org_id"),
            "entry_id": obj.get("entry_id"),
            "address": obj.get("address"),
            "memo": obj.get("memo"),
            "wallet_name": obj.get("wallet_name"),
            "wallet_type": obj.get("wallet_type"),
            "label": obj.get("label"),
            "email": obj.get("email")
        })
        return _obj


