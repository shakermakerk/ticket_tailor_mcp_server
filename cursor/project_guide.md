# Ticket Tailor MCP Server - Project Guide

## Project Overview

The Ticket Tailor MCP (model context protocol) Server is a Python wrapper for the Ticket Tailor API that makes it easy for AI agents to interact with the Ticket Tailor Platform. It is built on FastMCP for easy integration into applications. The project provides a simple, well-documented interface for accessing Ticket Tailor data programmatically.

## Project Structure

```
ticket_tailor_mcp_server/
├── .github/                # GitHub-specific files (CODEOWNERS, etc)
├── cursor/                 # Cursor-specific files for IDE integration
├── docs/                   # Documentation files
│   ├── implementation_template.md  # Template for implementing new endpoints
│   └── PR_TEMPLATE_GET_EVENT.md    # PR template for specific endpoints
├── examples/               # Example scripts demonstrating usage
│   ├── list_events.py      # Example for listing events
│   └── list_orders.py      # Example for listing orders
├── tests/                  # Unit tests
│   └── test_ticket_tailor.py  # Tests for the main module
├── .gitignore              # Git ignore file
├── CODE_OF_CONDUCT.md      # Project code of conduct
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # Project license (MIT)
├── README.md               # Project readme
├── ROADMAP.md              # Development roadmap and progress
├── requirements.txt        # Project dependencies
├── requirements-dev.txt    # Development dependencies
├── setup.py                # Package setup script
└── ticket_tailor.py        # Main module implementation
```

## Key Files

### `ticket_tailor.py`

This is the main module that contains the implementation of the Ticket Tailor API wrapper. It includes:
- Environment configuration and validation
- Utility functions for date conversion and API authentication
- MCP tool definitions for accessing Ticket Tailor endpoints
- Currently implemented endpoints:
  - `get_ticket_tailor_events` - List all events with filtering options
  - `get_ticket_tailor_orders` - List all orders with extensive filtering options

### `examples/`

The `examples/` directory contains example scripts that demonstrate how to use the library:
- `list_events.py` - Shows how to retrieve and display events
- `list_orders.py` - Shows how to retrieve and display orders for a specific event

### `docs/`

The `docs/` directory contains documentation:
- `implementation_template.md` - A template for implementing new API endpoints
- `PR_TEMPLATE_GET_EVENT.md` - A specific PR template for the GET /events/{id} endpoint

### `ROADMAP.md`

The roadmap outlines the planned implementation of Ticket Tailor API endpoints, prioritized based on their usefulness. It tracks:
- Implemented endpoints (marked with ✅)
- Pending endpoints to be implemented
- Implementation priorities (1-5)

## Getting Started

To use the library, you need to:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your Ticket Tailor API key in a `.env` file:
   ```
   TICKET_TAILOR_API_KEY=your_api_key_here
   ```

3. Import and use the functions:
   ```python
   from ticket_tailor import get_ticket_tailor_events, get_ticket_tailor_orders
   
   # Get published events for the next 60 days
   events = get_ticket_tailor_events()
   
   # Get orders for a specific event
   orders = get_ticket_tailor_orders(event_id="evt-abcd1234")
   ```

## Development Workflow

The project follows a structured workflow for implementing new features:

1. Check the `ROADMAP.md` for endpoints that need implementation
2. Follow the implementation template in `docs/implementation_template.md`
3. Add tests for the new functionality in `tests/test_ticket_tailor.py`
4. Create example scripts in the `examples/` directory
5. Update documentation as needed

## Tech Stack

- **FastMCP**: Provides the server functionality and tool definitions
- **HTTPX**: Modern HTTP client for making API requests
- **python-dotenv**: For loading environment variables
- **Python 3.6+**: The base language

## Future Development

The project roadmap (`ROADMAP.md`) outlines the planned implementation of additional Ticket Tailor API endpoints. These are organized by priority:

1. **Core Event & Order Management** - Essential functionality for managing events and orders
2. **Ticket & Attendee Management** - Managing individual tickets and attendees
3. **Extended Event Management** - More detailed management capabilities
4. **Advanced Features** - Additional functionality for specific scenarios
5. **Administrative Functions** - Administrative capabilities

## Contributing

Contributions are welcome, particularly for implementing new API endpoints. See `CONTRIBUTING.md` for detailed guidelines.
