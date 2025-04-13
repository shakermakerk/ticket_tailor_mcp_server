# API Endpoint Implementation Template

This template provides a guide for implementing new Ticket Tailor API endpoints.

## Function Implementation

```python
# 📡 [EMOJI THAT REPRESENTS FUNCTION] [FUNCTION NAME]
@mcp.tool()
def [function_name](
    # Required parameters
    [param1]: [type] = "",
    # Optional parameters with defaults
    [param2]: [type] = "[default_value]",
    # Add as many parameters as needed
) -> [return_type]:
    """
    [Function description in docstring format].
    
    Args:
        [param1]: [Parameter description]
        [param2]: [Parameter description]
        ...
    
    Returns:
        [Description of return value]
    """
    # Parameter validation or transformation if needed
    
    # Build parameters for API call
    params = filter_params({
        "[api_param1]": [param1],
        "[api_param2]": [param2],
        # Map function parameters to API parameters
    })
    
    # Make API call
    return api_get("[endpoint]", params)
```

## Implementation Checklist

- [ ] Review the API endpoint documentation at [Ticket Tailor API Docs](https://developers.tickettailor.com/docs/api/)
- [ ] Identify required and optional parameters
- [ ] Determine appropriate parameter types and defaults
- [ ] Implement the function with proper documentation
- [ ] Add unit tests in `tests/test_ticket_tailor.py`
- [ ] Create an example script in `examples/`
- [ ] Update README.md if necessary
- [ ] Update ROADMAP.md to mark implementation as complete

## Example: Implementation for Get Single Event

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

## Testing Your Implementation

Create a test for your new function in `tests/test_ticket_tailor.py`:

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

## Example Usage Script

Create an example script in `examples/`:

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
    print(f"Tickets available: {event.get('tickets_available', 'Unknown')}")
    # ... print other relevant details

if __name__ == "__main__":
    main() 