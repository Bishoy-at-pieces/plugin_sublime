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





class AnnotationTypeEnum(str, Enum):
    """
    This is used to describe a specific type of annotation. NOTE** This is linked to the annotation_type_filter in the parameters folder(if you change an enum here, please adjust the enum there.)
    """

    """
    allowed enum values
    """
    DESCRIPTION = 'DESCRIPTION'
    COMMENT = 'COMMENT'
    DOCUMENTATION = 'DOCUMENTATION'
    SUMMARY = 'SUMMARY'
    EXPLANATION = 'EXPLANATION'
    GIT_COMMIT = 'GIT_COMMIT'

    @classmethod
    def from_json(cls, json_str: str) -> AnnotationTypeEnum:
        """Create an instance of AnnotationTypeEnum from a JSON string"""
        return AnnotationTypeEnum(json.loads(json_str))


