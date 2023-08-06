from typing import Any, Iterable

import requests

from dragonfirerequests.response import DragonResponse


def _make_string(response):
    return f'\n\tRequest: {response.request.body.decode()}\n'\
           f'\tResponse: {response.content.decode()}'


class Dragon:
    __base_url: str
    __response_content_type: str
    __logger: Any
    __logger_method: str
    __headers: dict

    def __init__(self, base_url: str, *, response_content_type: str = "json", logger: Any = None,
                 logger_method: str = "info", headers: dict = None):
        if headers is None:
            headers = dict()
        self.__base_url = base_url
        self.__response_content_type = response_content_type
        self.__logger = logger
        self.__logger_method = logger_method
        self.__headers = headers

    def update_headers(self, new_headers: dict):
        self.__headers.update(new_headers)

    def __log(self, response: requests.Response):
        string_to_log = _make_string(response)
        log = getattr(self.__logger, self.__logger_method, print)
        try:
            log(string_to_log)
        except Exception as e:
            print(e)

    def fire(self, method: str, url: str = "", **kwargs) -> DragonResponse:
        # TODO: Durations
        headers = self.__headers | kwargs.get('headers', dict())
        kwargs['headers'] = headers
        response: requests.Response = requests.request(method, self.__base_url + url, **kwargs)
        success = True
        if self.__logger is not None:
            self.__log(response)
        if self.__response_content_type == 'json':
            try:
                data = response.json()
            except requests.JSONDecodeError:
                data = {}
                success = False
            return DragonResponse(response, data, success, response.request)

    def fire_post(self, *args, **kwargs):
        return self.fire("POST", *args, **kwargs)

    def fire_get(self, *args, **kwargs):
        return self.fire("GET", *args, **kwargs)

    def fire_put(self, *args, **kwargs):
        return self.fire("PUT", *args, **kwargs)

    def __dir__(self) -> Iterable[str]:
        return ['fire', 'update_headers']
