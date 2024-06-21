# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from Pieces._pieces_lib.pydantic import BaseModel, Field
from Pieces._pieces_lib.pieces_os_client.models.classification import Classification
from Pieces._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class TLPCodeFragmentClassificationMetadata(BaseModel):
    """
    TLPCodeFragmentClassificationMetadata
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    context: Optional[Classification] = None
    prior: Optional[Classification] = None
    __properties = ["schema", "context", "prior"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TLPCodeFragmentClassificationMetadata:
        """Create an instance of TLPCodeFragmentClassificationMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prior
        if self.prior:
            _dict['prior'] = self.prior.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TLPCodeFragmentClassificationMetadata:
        """Create an instance of TLPCodeFragmentClassificationMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TLPCodeFragmentClassificationMetadata.parse_obj(obj)

        _obj = TLPCodeFragmentClassificationMetadata.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "context": Classification.from_dict(obj.get("context")) if obj.get("context") is not None else None,
            "prior": Classification.from_dict(obj.get("prior")) if obj.get("prior") is not None else None
        })
        return _obj


