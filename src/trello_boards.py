import typing

from settings import envSettings
from src.trello_base import TrelloBase
from src.trello_dataclasses import Membership


class TrelloBoard(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = f'boards/{envSettings.BOARD_ID}/'

    def get_memberships(self):
        response = self._get_response(primary_url=self.primary_url,
                                      secondary_url='memberships')
        members: typing.List[Membership] = [Membership.parse_obj(user) for user in response]

        return members
