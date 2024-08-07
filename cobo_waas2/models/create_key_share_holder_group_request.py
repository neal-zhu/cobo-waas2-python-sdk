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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from cobo_waas2.models.create_key_share_holder import CreateKeyShareHolder
from cobo_waas2.models.key_share_holder_group_type import KeyShareHolderGroupType
from typing import Optional, Set
from typing_extensions import Self


class CreateKeyShareHolderGroupRequest(BaseModel):
    """
    CreateKeyShareHolderGroupRequest
    """  # noqa: E501
    key_share_holder_group_type: KeyShareHolderGroupType
    participants: StrictInt = Field(description="The number of key share holders in this key share holder group.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \"threshold - participants\" format), so you can only set `participants` to 2 or 3.   2. `threshold` must be less than or equal to `participants`. ")
    threshold: StrictInt = Field(description="The number of key share holders required to sign an operation.  **Notes:** 1. Currently, the available [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) are 2-2, 2-3, and 3-3 schemes (in the \"threshold - participants\" format), so you can only set `threshold` to 2 or 3.   2. `threshold` must be less than or equal to `participants`. ")
    key_share_holders: List[CreateKeyShareHolder]
    __properties: ClassVar[List[str]] = ["key_share_holder_group_type", "participants", "threshold", "key_share_holders"]

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
        """Create an instance of CreateKeyShareHolderGroupRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in key_share_holders (list)
        _items = []
        if self.key_share_holders:
            for _item in self.key_share_holders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['key_share_holders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateKeyShareHolderGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key_share_holder_group_type": obj.get("key_share_holder_group_type"),
            "participants": obj.get("participants"),
            "threshold": obj.get("threshold"),
            "key_share_holders": [CreateKeyShareHolder.from_dict(_item) for _item in obj["key_share_holders"]] if obj.get("key_share_holders") is not None else None
        })
        return _obj


