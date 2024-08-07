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
from enum import Enum
from typing_extensions import Self


class TransactionStatus(str, Enum):
    """
    The transaction status. Possible values include:    - `Submitted`: The transaction is submitted.   - `PendingScreening`: The transaction is pending screening by Risk Control.    - `PendingAuthorization`: The transaction is pending approvals.   - `PendingSignature`: The transaction is pending signature.    - `Broadcasting`: The transaction is being broadcast.   - `Confirming`: The transaction is waiting for the required number of confirmations.   - `Completed`: The transaction is completed.   - `Failed`: The transaction failed.   - `Rejected`: The transaction is rejected.   - `Pending`: The transaction is pending. 
    """

    """
    allowed enum values
    """
    SUBMITTED = 'Submitted'
    PENDINGSCREENING = 'PendingScreening'
    PENDINGAUTHORIZATION = 'PendingAuthorization'
    QUEUED = 'Queued'
    PENDINGSIGNATURE = 'PendingSignature'
    BROADCASTING = 'Broadcasting'
    CONFIRMING = 'Confirming'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


