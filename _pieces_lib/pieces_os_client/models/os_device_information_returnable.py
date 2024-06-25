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
from Pieces._pieces_lib.pydantic import BaseModel, Field, StrictStr
from Pieces._pieces_lib.pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from Pieces._pieces_lib.pieces_os_client.models.os_device_dependencies_information import OSDeviceDependenciesInformation
from Pieces._pieces_lib.pieces_os_client.models.os_device_hardware_information import OSDeviceHardwareInformation

class OSDeviceInformationReturnable(BaseModel):
    """
    This is the returnable model for the /os/device/information.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    dependencies: Optional[OSDeviceDependenciesInformation] = None
    name: Optional[StrictStr] = Field(None, description="this is the name of the device")
    version: Optional[StrictStr] = Field(None, description="this is the version of the device")
    hardware: Optional[OSDeviceHardwareInformation] = None
    __properties = ["schema", "dependencies", "name", "version", "hardware"]

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
    def from_json(cls, json_str: str) -> OSDeviceInformationReturnable:
        """Create an instance of OSDeviceInformationReturnable from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dependencies
        if self.dependencies:
            _dict['dependencies'] = self.dependencies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hardware
        if self.hardware:
            _dict['hardware'] = self.hardware.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OSDeviceInformationReturnable:
        """Create an instance of OSDeviceInformationReturnable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OSDeviceInformationReturnable.parse_obj(obj)

        _obj = OSDeviceInformationReturnable.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "dependencies": OSDeviceDependenciesInformation.from_dict(obj.get("dependencies")) if obj.get("dependencies") is not None else None,
            "name": obj.get("name"),
            "version": obj.get("version"),
            "hardware": OSDeviceHardwareInformation.from_dict(obj.get("hardware")) if obj.get("hardware") is not None else None
        })
        return _obj

