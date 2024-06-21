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
from Pieces._pieces_lib.pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class Auth0Identity(BaseModel):
    """
    Contains info retrieved from the identity provider with which the user originally authenticates. Users may also link their profile to multiple identity providers; those identities will then also appear in this array. The contents of an individual identity provider object varies by provider, but it will typically include the following. Link: [https://auth0.com/docs/rules/user-object-in-rules]  Currently left out: - profile_data: (Object) User information associated with the connection. When profiles are linked, it is populated with the associated user info for secondary accounts.  # noqa: E501
    """
    connection: Optional[StrictStr] = Field(None, description="Name of the Auth0 connection used to authenticate the user. ")
    is_social: Optional[StrictBool] = Field(None, alias="isSocial", description="Indicates whether the connection is a social one. ")
    provider: Optional[StrictStr] = Field(None, description="mapped from user_id  -> id")
    user_id: Optional[StrictStr] = Field(None, description="User's unique identifier for this connection/provider.")
    access_token: Optional[StrictStr] = None
    expires_in: Optional[StrictInt] = None
    __properties = ["connection", "isSocial", "provider", "user_id", "access_token", "expires_in"]

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
    def from_json(cls, json_str: str) -> Auth0Identity:
        """Create an instance of Auth0Identity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Auth0Identity:
        """Create an instance of Auth0Identity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Auth0Identity.parse_obj(obj)

        _obj = Auth0Identity.parse_obj({
            "connection": obj.get("connection"),
            "is_social": obj.get("isSocial"),
            "provider": obj.get("provider"),
            "user_id": obj.get("user_id"),
            "access_token": obj.get("access_token"),
            "expires_in": obj.get("expires_in")
        })
        return _obj


