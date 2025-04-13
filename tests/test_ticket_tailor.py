import datetime
import unittest
from unittest.mock import patch, MagicMock

import pytest

# Import functions to test
from ticket_tailor.core import (
    convert_date_to_unix,
    safe_unix,
    get_auth_header,
    filter_params
)


class TestTicketTailor(unittest.TestCase):
    
    def test_convert_date_to_unix(self):
        # Test with a known date
        test_date = "2023-01-01T00:00:00Z"
        expected_timestamp = int(datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp())
        self.assertEqual(convert_date_to_unix(test_date), expected_timestamp)
    
    def test_safe_unix(self):
        # Test with a valid date
        test_date = "2023-01-01T00:00:00Z"
        expected_timestamp = int(datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp())
        self.assertEqual(safe_unix(test_date), expected_timestamp)
        
        # Test with empty date and fallback
        fallback = 1672531200  # 2023-01-01 00:00:00 UTC
        self.assertEqual(safe_unix("", fallback=fallback), fallback)
    
    @patch('ticket_tailor.core.TICKET_TAILOR_API_KEY', 'test_api_key')
    def test_get_auth_header(self):
        # Expected header
        import base64
        auth_str = "test_api_key:"
        base64_auth = base64.b64encode(auth_str.encode()).decode()
        expected_header = {
            "Authorization": f"Basic {base64_auth}",
            "Accept": "application/json",
        }
        
        # Test
        self.assertEqual(get_auth_header(), expected_header)
    
    def test_filter_params(self):
        # Test with mixed params
        params = {
            "param1": "value1",
            "param2": "",
            "param3": None,
            "param4": "value4"
        }
        expected = {
            "param1": "value1",
            "param4": "value4"
        }
        self.assertEqual(filter_params(params), expected)


if __name__ == '__main__':
    unittest.main() 