# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.1.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.estimated_evm_eip1559_fee import EstimatedEvmEip1559Fee
from cobo_waas2.models.estimated_evm_legacy_fee import EstimatedEvmLegacyFee
from cobo_waas2.models.estimated_fixed_fee import EstimatedFixedFee
from cobo_waas2.models.estimated_utxo_fee import EstimatedUtxoFee
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ESTIMATEDFEE_ONE_OF_SCHEMAS = ["EstimatedEvmEip1559Fee", "EstimatedEvmLegacyFee", "EstimatedFixedFee", "EstimatedUtxoFee"]

class EstimatedFee(BaseModel):
    """
    EstimatedFee
    """
    # data type: EstimatedFixedFee
    oneof_schema_1_validator: Optional[EstimatedFixedFee] = None
    # data type: EstimatedEvmEip1559Fee
    oneof_schema_2_validator: Optional[EstimatedEvmEip1559Fee] = None
    # data type: EstimatedEvmLegacyFee
    oneof_schema_3_validator: Optional[EstimatedEvmLegacyFee] = None
    # data type: EstimatedUtxoFee
    oneof_schema_4_validator: Optional[EstimatedUtxoFee] = None
    actual_instance: Optional[Union[EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee]] = None
    one_of_schemas: Set[str] = { "EstimatedEvmEip1559Fee", "EstimatedEvmLegacyFee", "EstimatedFixedFee", "EstimatedUtxoFee" }

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
        instance = EstimatedFee.model_construct()
        error_messages = []
        match = 0
        # validate data type: EstimatedFixedFee
        if not isinstance(v, EstimatedFixedFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EstimatedFixedFee`")
        else:
            match += 1
        # validate data type: EstimatedEvmEip1559Fee
        if not isinstance(v, EstimatedEvmEip1559Fee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EstimatedEvmEip1559Fee`")
        else:
            match += 1
        # validate data type: EstimatedEvmLegacyFee
        if not isinstance(v, EstimatedEvmLegacyFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EstimatedEvmLegacyFee`")
        else:
            match += 1
        # validate data type: EstimatedUtxoFee
        if not isinstance(v, EstimatedUtxoFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EstimatedUtxoFee`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EstimatedFee with oneOf schemas: EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EstimatedFee with oneOf schemas: EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee. Details: " + ", ".join(error_messages))
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

        # check if data type is `EstimatedEvmEip1559Fee`
        if _data_type == "EVM_EIP_1559":
            instance.actual_instance = EstimatedEvmEip1559Fee.from_json(json_str)
            return instance

        # check if data type is `EstimatedEvmLegacyFee`
        if _data_type == "EVM_Legacy":
            instance.actual_instance = EstimatedEvmLegacyFee.from_json(json_str)
            return instance

        # check if data type is `EstimatedFixedFee`
        if _data_type == "Fixed":
            instance.actual_instance = EstimatedFixedFee.from_json(json_str)
            return instance

        # check if data type is `EstimatedUtxoFee`
        if _data_type == "UTXO":
            instance.actual_instance = EstimatedUtxoFee.from_json(json_str)
            return instance

        # check if data type is `EstimatedEvmEip1559Fee`
        if _data_type == "EstimatedEvmEip1559Fee":
            instance.actual_instance = EstimatedEvmEip1559Fee.from_json(json_str)
            return instance

        # check if data type is `EstimatedEvmLegacyFee`
        if _data_type == "EstimatedEvmLegacyFee":
            instance.actual_instance = EstimatedEvmLegacyFee.from_json(json_str)
            return instance

        # check if data type is `EstimatedFixedFee`
        if _data_type == "EstimatedFixedFee":
            instance.actual_instance = EstimatedFixedFee.from_json(json_str)
            return instance

        # check if data type is `EstimatedUtxoFee`
        if _data_type == "EstimatedUtxoFee":
            instance.actual_instance = EstimatedUtxoFee.from_json(json_str)
            return instance

        # deserialize data into EstimatedFixedFee
        try:
            instance.actual_instance = EstimatedFixedFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EstimatedEvmEip1559Fee
        try:
            instance.actual_instance = EstimatedEvmEip1559Fee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EstimatedEvmLegacyFee
        try:
            instance.actual_instance = EstimatedEvmLegacyFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EstimatedUtxoFee
        try:
            instance.actual_instance = EstimatedUtxoFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EstimatedFee with oneOf schemas: EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into EstimatedFee with oneOf schemas: EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], EstimatedEvmEip1559Fee, EstimatedEvmLegacyFee, EstimatedFixedFee, EstimatedUtxoFee]]:
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


