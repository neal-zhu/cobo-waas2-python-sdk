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
from cobo_waas2.models.key_share_holder_type import KeyShareHolderType
from typing import Optional, Set
from typing_extensions import Self


class CreateKeyShareHolder(BaseModel):
    """
    When creating MainKeyGroup and SigningKeyGroup, the Cobo key share holder will be added automatically.
    """  # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Key share holder's name.")
    type: Optional[KeyShareHolderType] = None
    tss_node_id: Optional[StrictStr] = Field(default=None, description="Key share holder's TSS Node ID.")
    signer: Optional[StrictBool] = Field(default=None, description="Whether the key share holder's TSS Node is a designated transaction signer. - `true`: The TSS Node is a designated transaction signer.  - `false`: The TSS Node is not a designated transaction signer. ")
    __properties: ClassVar[List[str]] = ["name", "type", "tss_node_id", "signer"]

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
        """Create an instance of CreateKeyShareHolder from a JSON string"""
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
        """Create an instance of CreateKeyShareHolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "tss_node_id": obj.get("tss_node_id"),
            "signer": obj.get("signer")
        })
        return _obj


