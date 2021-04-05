import typing
import requests
from abc import ABC
from copy import deepcopy
from settings import envSettings
from collections import OrderedDict


class TrelloBase(ABC):
    def __init__(self):
        self.base_url: typing.Final = "https://api.trello.com/1/"
        self.base_headers: typing.Final = {'Accept': 'application/json'}
        self.base_query: typing.Final = OrderedDict({'key': envSettings.TRELLO_KEY,
                                                     'token': envSettings.TRELLO_TOKEN})

    def _get_response(self,
                      primary_url: str,
                      secondary_url: typing.Optional[str] = None,
                      secondary_params: typing.Optional[str] = None,
                      is_headers: bool = True
                      ) -> dict:
        """
        Base function to make get response form trello

        :param primary_url: Primary key
        :param secondary_url: Secondary key
        :param secondary_params: Additional params for query
        :param is_headers: Sometimes no need in headers
        :return: response from trello
        """

        _final_url = deepcopy(self.base_url) + primary_url
        _final_headers = None
        _final_params = deepcopy(self.base_query)

        if isinstance(secondary_url, str):
            _final_url += secondary_url
        if is_headers:
            _final_headers = deepcopy(self.base_headers)
        if isinstance(secondary_params, str):
            _final_params.update({'query': secondary_params})

        response = requests.request(method='GET',
                                    url=_final_url,
                                    headers=_final_headers,
                                    params=_final_params)

        return response.json()
