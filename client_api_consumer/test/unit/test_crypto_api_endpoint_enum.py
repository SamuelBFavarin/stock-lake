from enum import Enum
import unittest

from client_api_consumer.crypto_api.crypto_api_endpoint_enum import EndpointEnum

class TestCryptoApiEndpointEnum(unittest.TestCase):

    def setUp(self):
        self.endpoint_enum = EndpointEnum

    def test_is_endpoint_key_valid(self):
        self.assertTrue(self.endpoint_enum.is_endpoint_key_valid('CHECK_STATUS'))
        self.assertTrue(self.endpoint_enum.is_endpoint_key_valid('GLOBAL_CRYPTOCURRENCY'))
        self.assertTrue(self.endpoint_enum.is_endpoint_key_valid('TRENDING_COINS'))
        self.assertFalse(self.endpoint_enum.is_endpoint_key_valid('THIS_IS_FUN'))
    

if __name__ == '__main__':
    unittest.main()