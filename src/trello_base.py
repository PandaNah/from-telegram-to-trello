import typing
import requests
from abc import ABC
from copy import deepcopy

from requests import Response

from settings import trelloSettings
from collections import OrderedDict


class TrelloBase(ABC):
    def __init__(self):
        self.base_url: typing.Final = "https://api.trello.com/1/"
        self.base_headers: typing.Final = {'Accept': 'application/json'}
        self.base_query: typing.Final = OrderedDict({'key': trelloSettings.TRELLO_KEY,
                                                     'token': trelloSettings.TRELLO_TOKEN})

    def _make_response(self,
                       call_method: str,
                       primary_url: str,
                       secondary_url: typing.Optional[str] = None,
                       secondary_params: OrderedDict = None,
                       is_headers: bool = True,
                       is_params: bool = True
                       ) -> Response:
        """
        Base function to make get response form trello

        :param call_method: method to call the site
        :param primary_url: Primary key
        :param secondary_url: Secondary key
        :param secondary_params: Additional params for query
        :param is_headers: Sometimes no need in headers
        :param is_params: Sometimes no need in params
        :return: response from trello
        """

        _final_url = deepcopy(self.base_url) + primary_url
        _final_headers = deepcopy(self.base_headers) if is_headers else ''
        _final_params = deepcopy(self.base_query) if is_params else ''

        if secondary_url:
            _final_url += secondary_url
        if secondary_params:
            _final_params.update(secondary_params)

        response = requests.request(method=call_method,
                                    url=_final_url,
                                    headers=_final_headers,
                                    params=_final_params)
        return response
