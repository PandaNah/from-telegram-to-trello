import typing

from settings import trelloSettings
from src.trello_base import TrelloBase
from src.trello_dataclasses import BoardMembership, BoardList, TrelloCardBase, TrelloCardLabels


class TrelloBoard(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = f'boards/{trelloSettings.BOARD_ID}/'

    def get_memberships(self) -> typing.List[BoardMembership]:
        """
        Get memberships of board

        :return: List[BoardMembership]
        """
        response = self._make_response(call_method='GET',
                                       primary_url=self.primary_url,
                                       secondary_url='memberships')
        members: typing.List[BoardMembership] = [BoardMembership.parse_obj(user) for user in response.json()]

        return members

    def get_lists(self) -> typing.List[BoardList]:
        """
        Get available lists of board

        :return: List[BoardList]
        """
        response = self._make_response(call_method='GET',
                                       primary_url=self.primary_url,
                                       secondary_url='lists')
        board_lists: typing.List[BoardList] = [BoardList.parse_obj(board_list) for board_list in response.json()]

        return board_lists

    def get_cards(self) -> typing.List[TrelloCardBase]:
        """
        Get cards on a board

        :return: List[TrelloCardBase]
        """
        response = self._make_response(call_method='GET',
                                       primary_url=self.primary_url,
                                       secondary_url='cards/')

        card_list: typing.List[TrelloCardBase] = [TrelloCardBase.parse_obj(card) for card in response.json()]

        return card_list

    def get_labels(self) -> typing.List[TrelloCardLabels]:
        """
        Get labels on a board

        :return: List[TrelloCardLabels]
        """
        response = self._make_response(call_method='GET',
                                       primary_url=self.primary_url,
                                       secondary_url='labels',
                                       is_headers=False)

        label_list: typing.List[TrelloCardLabels] = [TrelloCardLabels.parse_obj(label) for label in response.json()]

        return label_list
