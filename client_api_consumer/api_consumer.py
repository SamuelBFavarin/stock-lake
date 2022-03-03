from abc import ABC, abstractmethod
from enum import Enum


class ApiConsumer(ABC):

    @abstractmethod
    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def set_credentials(self, api_token: str):
        pass

    @abstractmethod
    def request(self, endpont: Enum, method: str, is_paginated: bool = False):
        pass
