from typing import Any, Iterable

import requests


class Dragon:
    __base_url: str
    __response_content_type: str
    __logger: Any
    __logger_method: str
    __headers: dict

    def __init__(self, base_url: str, *, response_content_type: str = "json", logger: Any = None,
                 logger_method: str = None, headers: dict = None):
        if headers is None:
            headers = dict()
        self.__base_url = base_url
        self.__response_content_type = response_content_type
        self.__logger = logger
        self.__logger_method = logger_method
        self.__headers = headers

    def fire(self, method: str, url: str = "", **kwargs):
        headers = self.__headers.update(kwargs.get('headers', dict()))
        kwargs['headers'] = headers
        response: requests.Response = requests.request(method, self.__base_url + url, **kwargs)
        if self.__logger is not None:
            pass  # TODO: Logging
        if self.__response_content_type == 'json':
            try:
                return response.json()
            except requests.JSONDecodeError:
                return {
                    "content": response.content.decode()
                }

    def __dir__(self) -> Iterable[str]:
        return ['fire']
