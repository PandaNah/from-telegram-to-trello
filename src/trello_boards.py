import aiohttp
import typing
from settings import envSettings


class TrelloBase:
    def __init__(self):
        self.url = "https://api.trello.com/1/"
        self.headers = {'Accept': 'application/json'}
        self.query = {'key': envSettings.TRELLO_KEY,
                      'token': envSettings.TELEGRAM_TOKEN}

    def get_url(self):
        return self.url

    def set_url(self, value: typing.Optional[str]):
        self.url = self.url + value

    def get_headers(self):
        return self.headers

    def set_headers(self, **kwargs):
        for key, item in kwargs.items():
            self.headers[key] = item

    def get_query(self):
        return self.query

    def set_query(self, **kwargs):
        for key, item in kwargs.items():
            self.query[key] = item


class TrelloBoard(TrelloBase):
    def __init__(self):
        super().__init__()
        self.url += f'boards/{envSettings.BOARD_ID}'

    def get_memberships(self):
        response = requests.request(
            method='GET',
            url=self.url,
            headers=self.headers,
            params=self.query
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
