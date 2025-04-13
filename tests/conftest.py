"""
Pytest configuration for Ticket Tailor tests.
"""

import os
import pytest
import re
from dotenv import load_dotenv
from vcr.filters import replace_headers, replace_query_parameters

# Load environment variables for the API key
load_dotenv()

# Define sensitive information patterns
API_KEY = os.environ.get('TICKET_TAILOR_API_KEY', '')
print(f"Conftest: API key exists: {bool(API_KEY)}")

@pytest.fixture(scope='session')
def vcr_config():
    """Configure VCR for recording API responses."""
    # If no API key is set, skip recording
    if not API_KEY:
        print("No API key found in environment variables")
        return pytest.skip("No API key found - set TICKET_TAILOR_API_KEY to run integration tests")
    
    print("API key found, configuring VCR")
    return {
        # Save cassettes in tests/cassettes directory
        "cassette_library_dir": "tests/cassettes",
        
        # Record new responses when cassettes don't exist
        "record_mode": "once",
        
        # Filter sensitive information from requests/responses
        "filter_headers": [
            ('authorization', 'FILTERED'),
        ],
        
        # Only match on the path, not query parameters (which may change)
        "match_on": ["method", "scheme", "host", "path"],
        
        # Allow real HTTP requests when no cassette exists
        "allow_playback_repeats": True,
    }

@pytest.fixture(scope='session')
def vcr_cassette_name(request):
    """Generate cassette names based on the test function name."""
    return f"{request.node.name}" 