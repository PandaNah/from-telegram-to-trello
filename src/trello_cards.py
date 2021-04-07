import typing
from collections import OrderedDict

from requests import Response

from src.trello_base import TrelloBase
from src.trello_dataclasses import TrelloCardBase


class TrelloCard(TrelloBase):
    def __init__(self):
        """
        Set self.primary_url with 'cards/'
        """
        super().__init__()
        self.primary_url = 'cards/'

    def get_card(self, card_id: typing.Union[str]) -> TrelloCardBase:
        """
        Get a card by card id

        :param card_id: ID card
        :return: TrelloCardBase
        """
        response = self._make_response(call_method='GET',
                                       primary_url=self.primary_url,
                                       secondary_url=card_id)

        card: TrelloCardBase = TrelloCardBase.parse_obj(response.json())

        return card

    def post_card(self, **kwargs) -> Response:
        """
        Post card to trello

        Possible kwargs:
            - name: The name for the card
            - desc: The description for the card
            - pos: The position of the new card. One of [top, bottom]
            - due: A due date for the card
            - idList: REQUIRED: The ID of the list the card should be created in
            - idMembers: Comma-separated list of member IDs to add to the card
            - idLabels: Comma-separated list of label IDs to add to the card

        :param kwargs: additional query to trello.
        :return: Response
        """
        additional_params = OrderedDict(kwargs)
        response = self._make_response(call_method='POST',
                                       primary_url=self.primary_url,
                                       secondary_params=additional_params,
                                       is_headers=False)

        return response

    def delete_card(self, card_id: typing.Union[str]) -> Response:
        """
        Delete a card

        :param card_id: Card id on board
        :return: Response
        """
        response = self._make_response(call_method='DELETE',
                                       primary_url=self.primary_url,
                                       secondary_url=card_id,
                                       is_headers=False)

        return response
