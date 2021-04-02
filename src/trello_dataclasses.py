import typing
from pydantic import BaseModel
from pydantic import Field


class Membership(BaseModel):
    id_member: typing.Optional[str] = Field(alias='idMember')
    member_type: typing.Optional[str] = Field(alias='memberType')


class Member(BaseModel):
    id_member: typing.Optional[str] = Field(alias='id')
    username: typing.Optional[str]
    full_name: typing.Optional[str] = Field(alias='fullName')
