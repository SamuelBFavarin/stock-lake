from api_consumer import ApiConsumer
from crypto_api_endpoint_enum import EndpointEnum
import json


class CryptoApiConsumer(ApiConsumer):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.base_url = base_url

    def set_credentials(self, api_token: str):
        self.api_token = api_token

    def request(self, endpont: EndpointEnum, method: str, is_paginated: bool = False) -> json:
        super().request(endpont, method, is_paginated)
        pass
