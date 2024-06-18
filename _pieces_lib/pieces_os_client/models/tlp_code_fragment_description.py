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


from typing import Optional, Union
from Pieces._pieces_lib.pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class TLPCodeFragmentDescription(BaseModel):
    """
    Model for ML big query Code Description.  # noqa: E501
    """
    description: Optional[StrictStr] = Field(None, description="This is the stringified json of a TLPDescription object")
    asset: StrictStr = Field(..., description="This is the asset id.")
    created: StrictStr = Field(..., description="timestamp of creation")
    model: StrictStr = Field(..., description="this is the model version")
    latency: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="the time it takes to run this model.")
    user: StrictStr = Field(..., description="the uuid of the user the description was created for.")
    context: Optional[StrictStr] = Field(None, description="the application this description was created from.")
    os: Optional[StrictStr] = Field(None, description="This is the UUID of the OS that this context is currently connected to.")
    __properties = ["description", "asset", "created", "model", "latency", "user", "context", "os"]

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
    def from_json(cls, json_str: str) -> TLPCodeFragmentDescription:
        """Create an instance of TLPCodeFragmentDescription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TLPCodeFragmentDescription:
        """Create an instance of TLPCodeFragmentDescription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TLPCodeFragmentDescription.parse_obj(obj)

        _obj = TLPCodeFragmentDescription.parse_obj({
            "description": obj.get("description"),
            "asset": obj.get("asset"),
            "created": obj.get("created"),
            "model": obj.get("model"),
            "latency": obj.get("latency"),
            "user": obj.get("user"),
            "context": obj.get("context"),
            "os": obj.get("os")
        })
        return _obj


