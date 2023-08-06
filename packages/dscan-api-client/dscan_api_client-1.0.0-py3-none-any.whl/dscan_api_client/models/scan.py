import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Scan")


@attr.s(auto_attribs=True)
class Scan:
    """
    Attributes:
        id (int):
        name (str):
        status (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        issues_found (Union[Unset, None, int]):
        comment (Union[Unset, None, str]):
        reason (Union[Unset, None, str]):
        s_type (Union[Unset, None, str]):
        n_type (Union[Unset, None, str]):
        program (Union[Unset, None, int]):
    """

    id: int
    name: str
    status: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    issues_found: Union[Unset, None, int] = UNSET
    comment: Union[Unset, None, str] = UNSET
    reason: Union[Unset, None, str] = UNSET
    s_type: Union[Unset, None, str] = UNSET
    n_type: Union[Unset, None, str] = UNSET
    program: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        issues_found = self.issues_found
        comment = self.comment
        reason = self.reason
        s_type = self.s_type
        n_type = self.n_type
        program = self.program

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if issues_found is not UNSET:
            field_dict["issues_found"] = issues_found
        if comment is not UNSET:
            field_dict["comment"] = comment
        if reason is not UNSET:
            field_dict["reason"] = reason
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if n_type is not UNSET:
            field_dict["n_type"] = n_type
        if program is not UNSET:
            field_dict["program"] = program

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        status = self.status if isinstance(self.status, Unset) else (None, str(self.status).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        issues_found = (
            self.issues_found
            if isinstance(self.issues_found, Unset)
            else (None, str(self.issues_found).encode(), "text/plain")
        )
        comment = self.comment if isinstance(self.comment, Unset) else (None, str(self.comment).encode(), "text/plain")
        reason = self.reason if isinstance(self.reason, Unset) else (None, str(self.reason).encode(), "text/plain")
        s_type = self.s_type if isinstance(self.s_type, Unset) else (None, str(self.s_type).encode(), "text/plain")
        n_type = self.n_type if isinstance(self.n_type, Unset) else (None, str(self.n_type).encode(), "text/plain")
        program = self.program if isinstance(self.program, Unset) else (None, str(self.program).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if issues_found is not UNSET:
            field_dict["issues_found"] = issues_found
        if comment is not UNSET:
            field_dict["comment"] = comment
        if reason is not UNSET:
            field_dict["reason"] = reason
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if n_type is not UNSET:
            field_dict["n_type"] = n_type
        if program is not UNSET:
            field_dict["program"] = program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        issues_found = d.pop("issues_found", UNSET)

        comment = d.pop("comment", UNSET)

        reason = d.pop("reason", UNSET)

        s_type = d.pop("s_type", UNSET)

        n_type = d.pop("n_type", UNSET)

        program = d.pop("program", UNSET)

        scan = cls(
            id=id,
            name=name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            issues_found=issues_found,
            comment=comment,
            reason=reason,
            s_type=s_type,
            n_type=n_type,
            program=program,
        )

        scan.additional_properties = d
        return scan

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
