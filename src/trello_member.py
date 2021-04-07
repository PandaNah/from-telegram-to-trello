import typing
from src.trello_base import TrelloBase
from src.trello_dataclasses import BoardMember


class TrelloMember(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'members/'

    def get_member(self, member_id: typing.AnyStr) -> BoardMember:
        """
        Get a member by member_id

        :param member_id: ID of member
        :return: BoardMember
        """
        response = self._make_response(call_method='GET', primary_url=self.primary_url, secondary_url=member_id)

        member_data: BoardMember = BoardMember.parse_obj(response.json())

        return member_data

