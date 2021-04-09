import typing
from src.trello_base import TrelloBase
from src.trello_boards import TrelloBoard
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

    def get_members_names(self) -> typing.List[BoardMember]:
        """
        Get all members names

        :return: List[BoardMember.full_name]
        """
        board = TrelloBoard()
        board_memberships_id = [member.member_id for member in board.get_memberships()]
        members_names = [self.get_member(member_id).member_fullname for member_id in board_memberships_id]

        return members_names
