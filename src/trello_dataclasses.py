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


class TrelloCardBadges(BaseModel):
    cardbadges_attachments: typing.Optional[int] = Field(alias='attachments')
    cardbadges_comments: typing.Optional[int] = Field(alias='comments')
    cardbadges_description: bool = Field(alias='description')


class TrelloCardCover(BaseModel):
    cardcover_brightness: typing.Optional[str] = Field('brightness')
    cardcover_color: typing.Optional[str] = Field('color')
    cardcover_size: typing.Optional[str] = Field('size')


class TrelloCardLabels(BaseModel):
    cardlabel_color: typing.Optional[str] = Field(alias='color')
    cardlabel_id: typing.Optional[str] = Field(alias='id')
    cardlabel_board_id: typing.Optional[str] = Field(alias='idBoard')
    cardlabel_name: typing.Optional[str] = Field(alias='name')


class TrelloCardBase(BaseModel):
    card_badges: typing.Optional[TrelloCardBadges] = Field(alias='badges')
    card_close: bool = Field(alias='closed')
    card_cover: typing.Optional[TrelloCardCover] = Field(alias='cover')
    card_lastactivity: typing.Optional[str] = Field(alias='dateLastActivity')
    card_description: typing.Optional[str] = Field(alias='desc')
    card_daedline: typing.Optional[str] = Field(alias='due')
    card_deadline_closed: bool = Field(alias='dueComplete')
    card_deadline_reminder: typing.Optional[int] = Field(alias='dueReminder')
    card_id: typing.Optional[str] = Field(alias='id')
    board_id: typing.Optional[str] = Field(alias='idBoard')
    labels_id: typing.List[typing.Optional[str]] = Field(alias='idLabels')
    list_id: typing.Optional[str] = Field(alias='idList')
    card_members_id: typing.List[typing.Optional[str]] = Field(alias='idMembers')
    card_short_id: typing.Optional[str] = Field(alias='idShort')
    card_labels: typing.List[TrelloCardLabels] = Field(alias='labels')
    card_header: typing.Optional[str] = Field(alias='name')
    card_pos: typing.Optional[int] = Field(alias='pos')
    card_shortlink: typing.Optional[str] = Field(alias='shortLink')
    card_shorturl: typing.Optional[str] = Field(alias='shortUrl')
