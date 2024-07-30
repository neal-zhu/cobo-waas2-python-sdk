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

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from cobo_waas2.models.contract_call_destination_type import ContractCallDestinationType
from typing import Optional, Set
from typing_extensions import Self


class EvmContractCallDestination(BaseModel):
    """
    The information about the transaction destination.
    """  # noqa: E501
    destination_type: ContractCallDestinationType
    address: StrictStr = Field(description="The destination address.")
    value: Optional[StrictStr] = Field(default=None, description="The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is `1.5`. ")
    calldata: Union[StrictBytes, StrictStr] = Field(description="The data that is used to invoke a specific function or method within the specified contract at the destination address. ")
    __properties: ClassVar[List[str]] = ["destination_type", "address", "value", "calldata"]

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
        """Create an instance of EvmContractCallDestination from a JSON string"""
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
        """Create an instance of EvmContractCallDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "address": obj.get("address"),
            "value": obj.get("value"),
            "calldata": obj.get("calldata")
        })
        return _obj

