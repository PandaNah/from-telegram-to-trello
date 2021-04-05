import typing
from pydantic import BaseModel
from pydantic import Field


class BoardMembership(BaseModel):
    member_id: typing.Optional[str] = Field(alias='idMember')
    member_type: typing.Optional[str] = Field(alias='memberType')


class BoardMember(BaseModel):
    member_id: typing.Optional[str] = Field(alias='id')
    member_username: typing.Optional[str]
    member_fullname: typing.Optional[str] = Field(alias='fullName')


class BoardList(BaseModel):
    list_id: typing.Optional[str] = Field(alias='id')
    list_name: typing.Optional[str] = Field(alias='name')
