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





class CapabilitiesEnum(str, Enum):
    """
    This lets us know what capabilites in relation to ml/ cloud infrastructure you are opting into.
    """

    """
    allowed enum values
    """
    LOCAL = 'LOCAL'
    CLOUD = 'CLOUD'
    BLENDED = 'BLENDED'

    @classmethod
    def from_json(cls, json_str: str) -> CapabilitiesEnum:
        """Create an instance of CapabilitiesEnum from a JSON string"""
        return CapabilitiesEnum(json.loads(json_str))

