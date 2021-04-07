import typing
from src.trello_base import TrelloBase
from src.trello_dataclasses import BoardList


class TrelloList(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'lists/'

    def get_list(self, list_id: typing.AnyStr) -> BoardList:
        """
        Get list from board by list_id

        :param list_id: ID of list to search
        :return: BoardList
        """
        response = self._make_response(call_method='GET', primary_url=self.primary_url, secondary_url=list_id)

        board_list: BoardList = BoardList.parse_obj(response.json())

        return board_list
