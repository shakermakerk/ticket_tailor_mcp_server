# Implementation of GET /events/{id} Endpoint

This PR implements the GET single event endpoint from the Ticket Tailor API, which allows retrieving detailed information about a specific event.

## Implementation Checklist

- [ ] Added `get_ticket_tailor_event` function to `ticket_tailor.py`
- [ ] Added proper type hints and docstrings
- [ ] Added unit tests in `tests/test_ticket_tailor.py`
- [ ] Created example script in `examples/get_event.py`
- [ ] Updated ROADMAP.md to mark implementation as complete

## Function Implementation

```python
# 🎪 Get a single event
@mcp.tool()
def get_ticket_tailor_event(
    id: str = "",
) -> Dict:
    """
    Retrieve a single event from the Ticket Tailor API.
    
    Args:
        id: The ID of the event to retrieve
    
    Returns:
        Event information as a dictionary
    """
    if not id:
        raise ValueError("Event ID is required")
        
    return api_get(f"events/{id}", {})
```

## Test Implementation

```python
@patch('ticket_tailor.httpx.Client')
def test_get_ticket_tailor_event(self, mock_client):
    # Mock response setup
    mock_response = Mock()
    mock_response.json.return_value = {"data": {"id": "evt-123", "name": "Test Event"}}
    mock_response.raise_for_status.return_value = None
    
    # Mock client setup
    mock_client_instance = Mock()
    mock_client_instance.get.return_value = mock_response
    mock_client.return_value.__enter__.return_value = mock_client_instance
    
    # Call function
    result = get_ticket_tailor_event(id="evt-123")
    
    # Assertions
    mock_client_instance.get.assert_called_once_with(
        "https://api.tickettailor.com/v1/events/evt-123",
        headers=ANY,
        params={}
    )
    self.assertEqual(result, {"id": "evt-123", "name": "Test Event"})
```

## Example Script

```python
#!/usr/bin/env python3
"""
Example script to retrieve a single event from Ticket Tailor.
"""

import os
import sys
import argparse
from dotenv import load_dotenv

# Add parent directory to path to import ticket_tailor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ticket_tailor import get_ticket_tailor_event

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Retrieve a single Ticket Tailor event')
    parser.add_argument('--id', required=True, help='Event ID to retrieve')
    args = parser.parse_args()
    
    print(f"Fetching event {args.id}...")
    event = get_ticket_tailor_event(id=args.id)
    
    if not event:
        print("Event not found.")
        return
    
    print(f"\nEvent Details:\n")
    print(f"Name: {event.get('name', 'Unnamed Event')}")
    print(f"Status: {event.get('status', 'Unknown')}")
    print(f"Start: {event.get('start', {}).get('iso', 'Unknown')}")
    print(f"End: {event.get('end', {}).get('iso', 'Unknown')}")
    print(f"Venue: {event.get('venue', {}).get('name', 'No venue')}")
    print(f"Tickets available: {event.get('tickets_available', 'Unknown')}")
    print(f"Tickets sold: {event.get('tickets_sold', 'Unknown')}")
    print(f"URL: {event.get('url', 'Unknown')}")

if __name__ == "__main__":
    main()
```

## API Documentation Reference

Implementation is based on the [GET /events/{id} endpoint documentation](https://developers.tickettailor.com/docs/api/get-a-single-event). 