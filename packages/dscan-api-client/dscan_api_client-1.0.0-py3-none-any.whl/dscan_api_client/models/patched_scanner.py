import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedScanner")


@attr.s(auto_attribs=True)
class PatchedScanner:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        s_type (Union[Unset, str]):
        config (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        comment (Union[Unset, None, str]):
        updated_at (Union[Unset, datetime.datetime]):
        version (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    s_type: Union[Unset, str] = UNSET
    config: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    version: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        s_type = self.s_type
        config = self.config
        enabled = self.enabled
        comment = self.comment
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if comment is not UNSET:
            field_dict["comment"] = comment
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        s_type = self.s_type if isinstance(self.s_type, Unset) else (None, str(self.s_type).encode(), "text/plain")
        config = self.config if isinstance(self.config, Unset) else (None, str(self.config).encode(), "text/plain")
        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        comment = self.comment if isinstance(self.comment, Unset) else (None, str(self.comment).encode(), "text/plain")
        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if comment is not UNSET:
            field_dict["comment"] = comment
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        s_type = d.pop("s_type", UNSET)

        config = d.pop("config", UNSET)

        enabled = d.pop("enabled", UNSET)

        comment = d.pop("comment", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        version = d.pop("version", UNSET)

        patched_scanner = cls(
            id=id,
            name=name,
            s_type=s_type,
            config=config,
            enabled=enabled,
            comment=comment,
            updated_at=updated_at,
            version=version,
        )

        patched_scanner.additional_properties = d
        return patched_scanner

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
