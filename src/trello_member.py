from src.trello_base import TrelloBase


class TrelloMember(TrelloBase):
    def __init__(self):
        super().__init__()
        self.primary_url = 'members/'

    def foo(self):
        pass
