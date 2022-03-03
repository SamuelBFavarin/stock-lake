import sys
from crypto_api.crypto_api_endpoint_enum import EndpointEnum
sys.path.append(".")


def test_is_endpoint_key_valid():
    assert EndpointEnum.is_endpoint_key_valid('CHECK_STATUS') is True
    assert EndpointEnum.is_endpoint_key_valid('GLOBAL_CRYPTOCURRENCY') is True
    assert EndpointEnum.is_endpoint_key_valid('TRENDING_COINS') is True
    assert EndpointEnum.is_endpoint_key_valid('THIS_IS_FUN') is False
