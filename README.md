# Ticket Tailor API Integration

A Python wrapper for the Ticket Tailor API that makes it easy to interact with events and orders from your Ticket Tailor account.

## Features

- Retrieve events with flexible filtering options
- Fetch orders with comprehensive search parameters
- Built on FastMCP for easy integration into your applications

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ticket_tailor_mcp_server.git
cd ticket_tailor_mcp_server

# Install dependencies
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the root directory
2. Add your Ticket Tailor API key:
   ```
   TICKET_TAILOR_API_KEY=your_api_key_here
   ```

## Usage

### Basic Example

```python
from ticket_tailor import mcp, get_ticket_tailor_events

# Get published events for the next 60 days
events = get_ticket_tailor_events()
```

### Advanced Usage

```python
# Get events within a specific date range
events = get_ticket_tailor_events(
    start_date="2023-10-01T00:00:00Z",
    end_date="2023-12-31T23:59:59Z",
    limit="50",
    status="published"
)

# Get orders for a specific event
from ticket_tailor import get_ticket_tailor_orders

orders = get_ticket_tailor_orders(
    event_id="evt-abcd1234",
    status="completed",
    limit="100"
)
```

## API Reference

### `get_ticket_tailor_events`

Retrieve events from the Ticket Tailor API.

Parameters:
- `start_date` (ISO format date string): Start date for event filtering
- `end_date` (ISO format date string): End date for event filtering
- `limit` (string): Maximum number of events to return
- `status` (string): Event status, default is "published"

### `get_ticket_tailor_orders`

Retrieve orders from the Ticket Tailor API with extensive filtering options.

See source code or Ticket Tailor API documentation for the full list of parameters.

## Development Roadmap

We're working on implementing more Ticket Tailor API endpoints. See our [Roadmap](ROADMAP.md) for:

- Prioritized list of endpoints to implement
- Current implementation status
- Guidelines for adding new endpoints

If you'd like to contribute, please check the roadmap for endpoints that need implementation.

## Examples

The `examples/` directory contains scripts demonstrating how to use this package:

- `list_events.py` - Shows how to retrieve and display events
- `list_orders.py` - Shows how to retrieve and display orders for a specific event

Run the examples after setting up your environment:

```bash
python examples/list_events.py
python examples/list_orders.py --event-id evt-abcd1234
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Check the [Roadmap](ROADMAP.md) for endpoints that need implementation
2. Review the [Contributing Guide](CONTRIBUTING.md) for guidelines
3. Create an issue to track your work
4. Submit a pull request with your implementation

We especially welcome contributions that implement new API endpoints following the patterns established in the existing code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 