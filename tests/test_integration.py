"""
Integration tests for the Ticket Tailor API wrapper.
These tests use real API calls when running for the first time.
Subsequent runs use recorded responses (cassettes).
"""

import os
import pytest
import datetime
from dotenv import load_dotenv
from ticket_tailor import get_ticket_tailor_events, get_ticket_tailor_orders

# Load environment variables for the API key
load_dotenv()

# Debug: Print API key existence (not the actual key)
api_key = os.environ.get('TICKET_TAILOR_API_KEY', '')
print(f"API key exists: {bool(api_key)}")

@pytest.mark.vcr()
def test_get_events_api():
    """Test getting events from the real API."""
    # Get events for the next 10 days
    today = datetime.datetime.now().isoformat()
    events = get_ticket_tailor_events(
        start_date=today,
        limit="5",
        status="published"
    )
    
    # We should at least get back a list (might be empty if no events)
    assert isinstance(events, list)
    
    # If we have events, check their structure
    if events:
        event = events[0]
        assert 'id' in event
        assert 'name' in event
        assert 'status' in event
        assert event['status'] == 'published'

@pytest.mark.vcr()
def test_get_orders_api():
    """Test getting orders from the real API."""
    # First get some events to find an event ID
    events = get_ticket_tailor_events(limit="1")
    
    # Skip if no events found
    if not events:
        pytest.skip("No events found to test orders")
    
    event_id = events[0]['id']
    
    # Get orders for this event
    orders = get_ticket_tailor_orders(
        event_id=event_id,
        limit="5"
    )
    
    # We should get back a list (might be empty if no orders)
    assert isinstance(orders, list)
    
    # If we have orders, check their structure
    if orders:
        order = orders[0]
        assert 'id' in order
        assert 'status' in order 