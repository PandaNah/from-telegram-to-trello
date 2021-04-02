import typing
from src.trello_base import TrelloBase
from src.trello_dataclasses import Member


class TrelloMember(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'members/'

    def get_member(self, id_member: typing.AnyStr):
        response = self._get_response(primary_url=self.primary_url,
                                      secondary_url=id_member)

        member_data: Member = Member.parse_obj(response)

        return member_data

