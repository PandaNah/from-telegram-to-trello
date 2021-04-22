import typing

from pydantic import BaseModel
from pydantic import Field


class SerializedMember(BaseModel):
    member_id: str = Field(alias='id')
    email: typing.Optional[str]
    fullName: typing.Optional[str]
    url: typing.Optional[str]
    username: typing.Optional[str]
    avatarUrl: typing.Optional[str]


class SerializedList(BaseModel):
    list_id: str = Field(alias='id')
    name: typing.Optional[str]
    closed: typing.Optional[bool]
    idBoard: typing.Optional[str]


class SerializedCardLabels(BaseModel):
    label_id: typing.Optional[str] = Field(alias='id')
    idBoard: typing.Optional[str]
    name: typing.Optional[str]
    color: typing.Optional[str]


class SerializedCard(BaseModel):
    card_id: str = Field(alias='id')
    dateLastActivity: typing.Optional[str]
    desc: typing.Optional[str]
    idBoard: typing.Optional[str]
    idList: typing.Optional[str]
    idLabels: typing.List[str]
    name: typing.Optional[str]
    due: typing.Optional[str]
    idMembers: typing.List[str]
    labels: typing.List[SerializedCardLabels]
    shortUrl: typing.Optional[str]
