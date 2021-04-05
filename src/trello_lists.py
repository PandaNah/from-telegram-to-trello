import typing
from src.trello_base import TrelloBase
from src.trello_dataclasses import BoardList


class TrelloList(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'lists/'

    def get_list(self, list_id: typing.AnyStr) -> BoardList:
        response = self._get_response(primary_url=self.primary_url,
                                      secondary_url=list_id)

        board_list: BoardList = BoardList.parse_obj(response)

        return board_list
