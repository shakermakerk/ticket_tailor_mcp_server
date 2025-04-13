#!/usr/bin/env python3
"""
Ticket Tailor MCP Server Runner

This script provides a convenient way to start the MCP server.
Run with: python run_server.py
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import and run the MCP server
from src.ticket_tailor.core import mcp

if __name__ == "__main__":
    print("Starting Ticket Tailor MCP Server...")
    print(f"API Key exists: {bool(os.environ.get('TICKET_TAILOR_API_KEY', ''))}")
    mcp.run() 