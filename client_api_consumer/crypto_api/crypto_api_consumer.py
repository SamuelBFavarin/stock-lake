from urllib import response
from api_consumer import ApiConsumer
from .crypto_api_endpoint_enum import EndpointEnum
import json
import requests


class CryptoApiConsumer(ApiConsumer):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.base_url = base_url

    def set_credentials(self, api_token: str):
        self.api_token = api_token

    def request(self, endpoint: EndpointEnum, method: str, is_paginated: bool = False) -> json:
        super().request(endpoint, method, is_paginated)

        URL = f"""{self.base_url}{endpoint.value["endpoint"]}"""
        resp = None

        if method.upper() == "GET":
            resp = requests.get(URL)

        elif method.upper() == "POST":
            resp = requests.post(URL)

        else:
            return {
                "code": 405,
                "message": "Method Not Allowed",
            }

        if self._check_is_success_status_code(resp):
            return {
                "code": resp.status_code,
                "message": resp.reason,
                "data": resp.json()[endpoint.value["records_key"]],
            }

        else:
            return {
                "code": resp.status_code,
                "message": resp.reason,
            }

    def _check_is_success_status_code(self, resp: response) -> bool:

        if resp.status_code >= 200 and resp.status_code <= 206:
            return True

        return False
