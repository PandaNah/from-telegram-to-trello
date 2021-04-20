from src.trello_base import TrelloBase


class TrelloList(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'lists/'
