from enum import Enum


class EndpointEnum(Enum):
    """
    Provides a set of endpoint constants composed of a dict with
    information about the endpoint path, the JSON key name that
    contains the response's records.
    """

    CHECK_STATUS = {
        "endpoint": "/ping",
        "description": "Check API server status",
        "records_key": "gecko_says",
    },

    GLOBAL_CRYPTOCURRENCY = {
        "endpoint": "/global",
        "description": "Get cryptocurrency global data",
        "records_key": "data",
    },

    TRENDING_COINS = {
        "endpoint": "/search/trending",
        "description": """Top-7 trending coins on CoinGecko
                          as searched by users in the last 24 hours
                          (Ordered by most popular first)""",
        "records_key": "coins",
    }

    @classmethod
    def is_endpoint_key_valid(cls, endpoint):
        """
        Check if the endpoint is valid by searching over the enum keys

        @param endpoint: the endpoint key to be checked
        @return: bool
        """
        return endpoint in cls._member_names_
