# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
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
from typing import Optional, Set
from typing_extensions import Self


class SourceGroup(BaseModel):
    """
    The source key share holder group.  **Note:** `source_key_share_holder_group` is used only when `type` is set to either `KeyGenfromKeyGroup` or `Recovery`. This is to specify the key share holder group to be used as the source key share holder group to create key shares for the `target_key_share_holder_group`. 
    """  # noqa: E501
    key_share_holder_group_id: StrictStr = Field(description="The ID of the Source Group.")
    tss_node_ids: Optional[List[StrictStr]] = Field(default=None, description="The TSS Node IDs participating in creating a new key share holder group when `type` is set to either `KeyGenFromKeyGroup` or `Recovery`.   **Note:** In any [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) such as the 2-2, 2-3, and 3-3 schemes (in the \"threshold - node count\" format), for `tss_node_ids`, you only need to fill in 1 Cobo TSS Node ID and enough non-Cobo TSS Node IDs to satisfy the number of approvers specified in `threshold`. To obtain the Cobo TSS Node ID, run [List all Cobo key share holders](/v2/api-references/wallets--mpc-wallets/list-all-cobo-key-share-holders). ")
    __properties: ClassVar[List[str]] = ["key_share_holder_group_id", "tss_node_ids"]

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
        """Create an instance of SourceGroup from a JSON string"""
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
        """Create an instance of SourceGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key_share_holder_group_id": obj.get("key_share_holder_group_id"),
            "tss_node_ids": obj.get("tss_node_ids")
        })
        return _obj

