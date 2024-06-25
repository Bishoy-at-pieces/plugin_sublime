# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from Pieces._pieces_lib.aenum import Enum, no_arg





class QGPTStreamEnum(str, Enum):
    """
    This is a specific Enum used for the QGPT Stream.
    """

    """
    allowed enum values
    """
    CANCELED = 'CANCELED'
    INITIALIZED = 'INITIALIZED'
    IN_MINUS_PROGRESS = 'IN-PROGRESS'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    UNKNOWN = 'UNKNOWN'
    STOPPED = 'STOPPED'
    RESET = 'RESET'

    @classmethod
    def from_json(cls, json_str: str) -> QGPTStreamEnum:
        """Create an instance of QGPTStreamEnum from a JSON string"""
        return QGPTStreamEnum(json.loads(json_str))

