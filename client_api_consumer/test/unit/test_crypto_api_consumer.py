from crypto_api.crypto_api_consumer import CryptoApiConsumer  # noqa:E402
from crypto_api.crypto_api_endpoint_enum import EndpointEnum  # noqa:E402
from requests import Response


BASE_URL = "https://baseurl/v1"


def crypto_api_factor() -> CryptoApiConsumer:
    return CryptoApiConsumer(BASE_URL)


def test_constructor():
    crypto_api_consumer = crypto_api_factor()
    assert crypto_api_consumer.base_url == BASE_URL


def test_set_credentials():
    CREDENTIALS = "this_is_is_a_key"
    crypto_api_consumer = crypto_api_factor()
    crypto_api_consumer.set_credentials(CREDENTIALS)

    assert crypto_api_consumer.api_token == CREDENTIALS


def test_check_is_success_status_code():
    crypto_api_consumer = crypto_api_factor()
    mock_response = Response()

    mock_response.status_code = 199
    assert crypto_api_consumer._check_is_success_status_code(mock_response) is False

    mock_response.status_code = 200
    assert crypto_api_consumer._check_is_success_status_code(mock_response) is True

    mock_response.status_code = 206
    assert crypto_api_consumer._check_is_success_status_code(mock_response) is True

    mock_response.status_code = 207
    assert crypto_api_consumer._check_is_success_status_code(mock_response) is False


def test_request_method_not_allowed():
    crypto_api_consumer = crypto_api_factor()

    resp = crypto_api_consumer.request(
        endpoint=EndpointEnum.CHECK_STATUS,
        method="PUT"
    )

    assert resp["code"] == 405
    assert resp["code"] != 407
    assert resp["message"] == "Method Not Allowed"
