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
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class EstimatedFixedFee(BaseModel):
    """
    In the fixed fee model, the transaction fee is a fixed amount within a certain amount of period regardless of the transaction size or network congestion, which can vary between different chains.
    """  # noqa: E501
    fee_amount: StrictStr = Field(description="The fee that you need to pay for the transaction.")
    fee_type: FeeType
    token_id: StrictStr = Field(description="The token ID of the transaction fee.")
    is_loop: Optional[StrictBool] = Field(default=None, description="Whether the transaction can be executed as a Loop transfer. For more information about Loop, see [Loop's website](https://loop.top/). - `true`: The transaction is a Loop transfer. - `false`: The transaction is not a Loop transfer. ")
    __properties: ClassVar[List[str]] = ["fee_amount", "fee_type", "token_id", "is_loop"]

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
        """Create an instance of EstimatedFixedFee from a JSON string"""
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
        """Create an instance of EstimatedFixedFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fee_amount": obj.get("fee_amount"),
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "is_loop": obj.get("is_loop")
        })
        return _obj


