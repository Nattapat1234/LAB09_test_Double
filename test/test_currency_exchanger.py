import unittest
import os, sys
CURRENTDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENTDIR))
from unittest.mock import patch
from source.currency_exchanger import CurrencyExchanger
from utils import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.currency_exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
        self.mock_api_response = get_mock_currency_api_response()

    @patch("source.currency_exchanger.requests.get")
    def test_currency_exchange(self, mock_get):
        #Assign mock's return value
        mock_get.return_value = self.mock_api_response
        
        amount_in_thb = 500
        expected_krw = 500 * 38.69

        #Act - Execute the currency exchange function
        result = self.currency_exchanger.currency_exchange(amount_in_thb)

        #Check if the API call was made once
        mock_get.assert_called_once_with(self.currency_exchanger.currency_api, params={'from': 'THB', 'to': 'KRW'})

        #Assert the expected result
        self.assertEqual(result, expected_krw)



if __name__ == "__main__":
    unittest.main()




