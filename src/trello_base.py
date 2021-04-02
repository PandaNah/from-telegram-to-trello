import typing
import requests
from copy import deepcopy
from settings import envSettings


class TrelloBase:
    def __init__(self):
        self.base_url = "https://api.trello.com/1/"
        self.base_headers = {'Accept': 'application/json'}
        self.base_query = {'key': envSettings.TRELLO_KEY,
                           'token': envSettings.TRELLO_TOKEN}

    def _get_response(self,
                      primary_url: str,
                      secondary_url: typing.Optional[str] = None,
                      secondary_headers: typing.Optional[typing.Dict[str, str]] = None,
                      secondary_params: typing.Optional[typing.Dict[str, str]] = None,
                      ) -> dict:

        _final_url = deepcopy(self.base_url) + primary_url
        _final_headers = deepcopy(self.base_headers)
        _final_params = deepcopy(self.base_query)

        if isinstance(secondary_url, str):
            _final_url += secondary_url
        if isinstance(secondary_headers, dict):
            _final_headers = {**self.base_headers, **secondary_headers}
        if isinstance(secondary_params, dict):
            _final_params = {**self.base_query, **secondary_params}

        response = requests.request(method='GET',
                                    url=_final_url,
                                    headers=_final_headers,
                                    params=_final_params)

        return response.json()

