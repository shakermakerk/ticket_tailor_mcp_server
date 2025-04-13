# Ticket Tailor API Integration

A Python MCP wrapper for the Ticket Tailor API that makes it easy for LLM's to interact with the Ticket Tailor API. Still very early stages but the groundwork has all been done. Now its about building out functions for the various end points. We can also build out specific tools that dont just get/post/patch data but perform work on the data. I have functions to create events in code elsewhere that i will bring in later. 

## Features

- Retrieve events with flexible filtering options
- Fetch orders with comprehensive search parameters
- Built on FastMCP for easy integration into your applications

## Installation

```bash
# Clone the repository
git clone https://github.com/shakermakerk/ticket_tailor_mcp_server.git
cd ticket_tailor_mcp_server

# Install dependencies
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the root directory based on the `.env_example` file to add your Ticket Tailor API key

## Usage

### To use with Cursor (Not that we would generally want to do this):

edit mcp.json to add the following
```
    "tt-events": {
      "type": "command",
      "command": "mcp run /src/ticket_tailor/ticket_tailor_funcs.py" # you may need to edit this path
    }
```

### Advanced Usage
```
Using with our own agents. It depends on the agentic framework that you're using but you generally pass the MCP server in as a tool. Some frameworks like Openai-Agents SDK that are naturally async require some helper functions. I can provide examples if reqested. in ticket_tailor_mcp_server/src/ticket_tailor/example_langgraph_agent.py you will see a simple example using langchain react agents (not langgraph).

```

## API Reference

See the `src/ticket_tailor` directory for implementation details.

## Development Roadmap

We're working on implementing more Ticket Tailor API endpoints. See our [Roadmap](ROADMAP.md) for:

- Prioritized list of endpoints to implement
- Current implementation status
- Guidelines for adding new endpoints

If you'd like to contribute, please check the roadmap for endpoints that need implementation.

## Contributing

Contributions are welcome! Here's how you can help:

1. Check the [Roadmap](ROADMAP.md) for endpoints that need implementation
2. Review the [Contributing Guide](CONTRIBUTING.md) for guidelines
3. Create an issue to track your work
4. Submit a pull request with your implementation

We especially welcome contributions that implement new API endpoints following the patterns established in the existing code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 