# ✅ Load environment variables before using them
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
import httpx
import base64
import datetime
from typing import List, Dict
import json
import sys


# Load env vars from .env file
load_dotenv()
TICKET_TAILOR_API_KEY = os.getenv("TICKET_TAILOR_API_KEY")
API_BASE = "https://api.tickettailor.com/v1"

# Fail early if key is missing
if not TICKET_TAILOR_API_KEY:
    raise EnvironmentError("Missing Ticket Tailor API key. Set it as TICKET_TAILOR_API_KEY in your environment variables.")


# 🔧 Converts ISO date strings to Unix timestamps
def convert_date_to_unix(date_string: str) -> int:
    try:
        dt = datetime.datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return int(dt.timestamp())
    except Exception as e:
        print(f"Error converting date: {e}")
        return int(datetime.datetime.now().timestamp())  # fallback


# 🔧 Wrapper to safely handle empty or missing dates
def safe_unix(date_string: str, fallback: int = None) -> int:
    return convert_date_to_unix(date_string) if date_string else (fallback or int(datetime.datetime.now().timestamp()))


# 🔐 Generate Ticket Tailor API auth headers
def get_auth_header() -> Dict[str, str]:
    auth_str = f"{TICKET_TAILOR_API_KEY}:"
    base64_auth = base64.b64encode(auth_str.encode()).decode()
    return {
        "Authorization": f"Basic {base64_auth}",
        "Accept": "application/json",
    }


# 📡 Generic GET request wrapper for Ticket Tailor API
def api_get(endpoint: str, params: Dict) -> List[Dict]:
    url = f"{API_BASE}/{endpoint}"
    try:
        with httpx.Client() as client:
            response = client.get(url, headers=get_auth_header(), params=params)
            response.raise_for_status()
            return response.json().get("data", [])
    except httpx.HTTPStatusError as e:
        print(f"HTTP error while accessing {endpoint}: {e}")
        return []


# 🧠 Utility to filter out empty parameters
def filter_params(params: Dict[str, str]) -> Dict[str, str]:
    return {k: v for k, v in params.items() if v}