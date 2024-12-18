# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.associated_host import AssociatedHost
from ipam.models.host_associated_server import HostAssociatedServer
from typing import Optional, Set
from typing_extensions import Self


class DHCPServiceInstance(BaseModel):
    """
    A DHCP Service (_dhcp/service_) object associates DHCP configuration with the DHCP host services.   Automatically created and destroyed based on the hosts known to the platform.
    """ # noqa: E501
    associated_hosts: Optional[List[AssociatedHost]] = None
    associated_server: Optional[HostAssociatedServer] = None
    comment: Optional[StrictStr] = Field(
        default=None, description="The comment for the service.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    ip_space: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    name: Optional[StrictStr] = Field(
        default=None, description="The display name of the service.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The tags of the service host in JSON format.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "associated_hosts", "associated_server", "comment", "id", "ip_space",
        "name", "tags"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DHCPServiceInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "comment",
            "id",
            "name",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in associated_hosts (list)
        _items = []
        if self.associated_hosts:
            for _item in self.associated_hosts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associated_hosts'] = _items
        # override the default output from pydantic by calling `to_dict()` of associated_server
        if self.associated_server:
            _dict['associated_server'] = self.associated_server.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DHCPServiceInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_hosts": [
                AssociatedHost.from_dict(_item)
                for _item in obj["associated_hosts"]
            ] if obj.get("associated_hosts") is not None else None,
            "associated_server":
            HostAssociatedServer.from_dict(obj["associated_server"])
            if obj.get("associated_server") is not None else None,
            "comment":
            obj.get("comment"),
            "id":
            obj.get("id"),
            "ip_space":
            obj.get("ip_space"),
            "name":
            obj.get("name"),
            "tags":
            obj.get("tags")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj