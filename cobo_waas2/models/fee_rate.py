# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.evm_eip1559_fee_rate import EvmEip1559FeeRate
from cobo_waas2.models.evm_legacy_fee_rate import EvmLegacyFeeRate
from cobo_waas2.models.fixed_fee_rate import FixedFeeRate
from cobo_waas2.models.utxo_fee_rate import UtxoFeeRate
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

FEERATE_ONE_OF_SCHEMAS = ["EvmEip1559FeeRate", "EvmLegacyFeeRate", "FixedFeeRate", "UtxoFeeRate"]

class FeeRate(BaseModel):
    """
    FeeRate
    """
    # data type: FixedFeeRate
    oneof_schema_1_validator: Optional[FixedFeeRate] = None
    # data type: EvmEip1559FeeRate
    oneof_schema_2_validator: Optional[EvmEip1559FeeRate] = None
    # data type: EvmLegacyFeeRate
    oneof_schema_3_validator: Optional[EvmLegacyFeeRate] = None
    # data type: UtxoFeeRate
    oneof_schema_4_validator: Optional[UtxoFeeRate] = None
    actual_instance: Optional[Union[EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate]] = None
    one_of_schemas: Set[str] = { "EvmEip1559FeeRate", "EvmLegacyFeeRate", "FixedFeeRate", "UtxoFeeRate" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = FeeRate.model_construct()
        error_messages = []
        match = 0
        # validate data type: FixedFeeRate
        if not isinstance(v, FixedFeeRate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FixedFeeRate`")
        else:
            match += 1
        # validate data type: EvmEip1559FeeRate
        if not isinstance(v, EvmEip1559FeeRate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EvmEip1559FeeRate`")
        else:
            match += 1
        # validate data type: EvmLegacyFeeRate
        if not isinstance(v, EvmLegacyFeeRate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EvmLegacyFeeRate`")
        else:
            match += 1
        # validate data type: UtxoFeeRate
        if not isinstance(v, UtxoFeeRate):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UtxoFeeRate`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FeeRate with oneOf schemas: EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FeeRate with oneOf schemas: EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("fee_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `fee_type` in the input.")

        # check if data type is `EvmEip1559FeeRate`
        if _data_type == "EVM_EIP_1559":
            instance.actual_instance = EvmEip1559FeeRate.from_json(json_str)
            return instance

        # check if data type is `EvmLegacyFeeRate`
        if _data_type == "EVM_Legacy":
            instance.actual_instance = EvmLegacyFeeRate.from_json(json_str)
            return instance

        # check if data type is `FixedFeeRate`
        if _data_type == "Fixed":
            instance.actual_instance = FixedFeeRate.from_json(json_str)
            return instance

        # check if data type is `UtxoFeeRate`
        if _data_type == "UTXO":
            instance.actual_instance = UtxoFeeRate.from_json(json_str)
            return instance

        # check if data type is `EvmEip1559FeeRate`
        if _data_type == "EvmEip1559FeeRate":
            instance.actual_instance = EvmEip1559FeeRate.from_json(json_str)
            return instance

        # check if data type is `EvmLegacyFeeRate`
        if _data_type == "EvmLegacyFeeRate":
            instance.actual_instance = EvmLegacyFeeRate.from_json(json_str)
            return instance

        # check if data type is `FixedFeeRate`
        if _data_type == "FixedFeeRate":
            instance.actual_instance = FixedFeeRate.from_json(json_str)
            return instance

        # check if data type is `UtxoFeeRate`
        if _data_type == "UtxoFeeRate":
            instance.actual_instance = UtxoFeeRate.from_json(json_str)
            return instance

        # deserialize data into FixedFeeRate
        try:
            instance.actual_instance = FixedFeeRate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EvmEip1559FeeRate
        try:
            instance.actual_instance = EvmEip1559FeeRate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EvmLegacyFeeRate
        try:
            instance.actual_instance = EvmLegacyFeeRate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UtxoFeeRate
        try:
            instance.actual_instance = UtxoFeeRate.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FeeRate with oneOf schemas: EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into FeeRate with oneOf schemas: EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], EvmEip1559FeeRate, EvmLegacyFeeRate, FixedFeeRate, UtxoFeeRate]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

