"""
Ticket Tailor MCP Server - Main entry point
Run with: python -m ticket_tailor
"""

from .core import mcp

if __name__ == "__main__":
    print("Starting Ticket Tailor MCP Server...")
    mcp.run() 