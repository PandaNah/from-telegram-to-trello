import typing

from settings import trelloSettings
from src.trello_base import TrelloBase
from src.trello_dataclasses import BoardMembership, BoardList


class TrelloBoard(TrelloBase):
    def __init__(self):
        """
        Set self.primary_url with your BOARD_ID
        """
        super().__init__()
        self.primary_url = f'boards/{trelloSettings.BOARD_ID}/'

    def get_memberships(self) -> typing.List[BoardMembership]:
        """
        Get memberships of board

        :return: List[BoardMembership]
        """
        response = self._make_response(call_method='GET', primary_url=self.primary_url, secondary_url='memberships')
        members: typing.List[BoardMembership] = [BoardMembership.parse_obj(user) for user in response]

        return members

    def get_lists(self) -> typing.List[BoardList]:
        """
        Get available lists of board

        :return: List[BoardList]
        """
        response = self._make_response(call_method='GET', primary_url=self.primary_url, secondary_url='lists')
        board_lists: typing.List[BoardList] = [BoardList.parse_obj(board_list) for board_list in response]
        return board_lists
