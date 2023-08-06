import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..types import Unset

T = TypeVar("T", bound="Program")


@attr.s(auto_attribs=True)
class Program:
    """
    Attributes:
        id (int):
        subdomain (List[str]):
        name (str):
        url (str):
        bounty (bool):
        enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    subdomain: List[str]
    name: str
    url: str
    bounty: bool
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        subdomain = self.subdomain

        name = self.name
        url = self.url
        bounty = self.bounty
        enabled = self.enabled
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subdomain": subdomain,
                "name": name,
                "url": url,
                "bounty": bounty,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        _temp_subdomain = self.subdomain
        subdomain = (None, json.dumps(_temp_subdomain).encode(), "application/json")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        bounty = self.bounty if isinstance(self.bounty, Unset) else (None, str(self.bounty).encode(), "text/plain")
        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "subdomain": subdomain,
                "name": name,
                "url": url,
                "bounty": bounty,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        subdomain = cast(List[str], d.pop("subdomain"))

        name = d.pop("name")

        url = d.pop("url")

        bounty = d.pop("bounty")

        enabled = d.pop("enabled")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        program = cls(
            id=id,
            subdomain=subdomain,
            name=name,
            url=url,
            bounty=bounty,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
        )

        program.additional_properties = d
        return program

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
