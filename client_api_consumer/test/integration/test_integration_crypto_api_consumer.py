from crypto_api.crypto_api_consumer import CryptoApiConsumer  # noqa:E402
from crypto_api.crypto_api_endpoint_enum import EndpointEnum  # noqa:E402


BASE_URL = "https://api.coingecko.com/api/v3"


def crypto_api_factor() -> CryptoApiConsumer:
    return CryptoApiConsumer(BASE_URL)


def test_request_check_status():
    crypto_api_consumer = crypto_api_factor()

    resp = crypto_api_consumer.request(
        endpoint=EndpointEnum.CHECK_STATUS,
        method="GET"
    )

    assert resp["code"] == 200
    assert resp["message"] == "OK"


def test_request_global_cryptocurrency():
    crypto_api_consumer = crypto_api_factor()

    resp = crypto_api_consumer.request(
        endpoint=EndpointEnum.GLOBAL_CRYPTOCURRENCY,
        method="GET"
    )

    assert resp["code"] == 200
    assert resp["message"] == "OK"
    assert "data" in resp
    assert "active_cryptocurrencies" in resp["data"]
    assert "upcoming_icos" in resp["data"]
    assert "ongoing_icos" in resp["data"]
    assert "ended_icos" in resp["data"]
    assert "markets" in resp["data"]
    assert "total_market_cap" in resp["data"]


def test_request_trending_coins():
    crypto_api_consumer = crypto_api_factor()

    resp = crypto_api_consumer.request(
        endpoint=EndpointEnum.TRENDING_COINS,
        method="GET"
    )

    assert resp["code"] == 200
    assert resp["message"] == "OK"
    assert type(resp["data"]) is list
