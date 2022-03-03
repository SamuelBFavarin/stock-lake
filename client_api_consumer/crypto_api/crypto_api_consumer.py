from enum import Enum
from api_consumer import ApiConsumer
from crypto_api_endpoint_enum import EndpointEnum

class CryptoApiConsumer(ApiConsumer):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.base_url = base_url

    def set_credentials(self, api_token:str):    
        super().set_credentials(api_token)
        self.api_token = api_token

    def request(self, endpont: EndpointEnum, method: str, is_paginated: bool = False):
        super().request(endpont, method, is_paginated)
        pass
