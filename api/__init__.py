import requests
from helpers import SuiteTestData


class BaseApi:
    std = None
    __base_url__ = None
    __headers__ = {}

    def __init__(self, resource):
        self.std = SuiteTestData()
        if not self.__base_url__:
            self.__base_url__ = self.std.api_url + resource

    def get_url(self):
        try:
           return self.__base_url__
        except Exception as e:
            return False

    def add_query_param(self, key, value):
        try:
            if self.__base_url__[0] == '?':
                self.__base_url__ += f'{key}={value}'
            else:
                self.__base_url__ += f'&{key}={value}'
            return self.__base_url__
        except Exception as e:
            return False

    def get_headers(self):
        try:
            return self.__headers__
        except Exception as e:
            return False

    def add_header(self, key, value):
        try:
            self.__headers__.setdefault(key, value)
            return True
        except Exception as e:
            return False

    def request(self, method=None, url=None, data=None, json=None, headers=None, **kwargs):
        try:
            response = None
            headers = self.get_headers() if not headers else headers
            if method.lower() == 'get':
                response = requests.get(url=url, headers=headers, **kwargs)
            elif method.lower() == 'post':
                response = requests.post(url=url, json=json, headers=headers, **kwargs) if json else requests.post(
                    url=url, data=data, headers=headers, **kwargs)
            elif method.lower() == 'put':
                response = requests.put(url=url, json=json, headers=headers, **kwargs) if json else requests.put(
                    url=url, data=data, headers=headers, **kwargs)
            elif method.lower() == 'delete':
                response = requests.delete(url=url, headers=headers, **kwargs)
            return response
        except Exception as e:
            return False
