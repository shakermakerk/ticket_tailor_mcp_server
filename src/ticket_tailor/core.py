# ✅ Load environment variables before using them
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
import httpx
import base64
import datetime
from typing import List, Dict

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


# 🚀 Create MCP server instance
mcp = FastMCP("tt-events")


# 📅 Retrieve Ticket Tailor events
@mcp.tool()
def get_ticket_tailor_events(
    start_date: str = "",
    end_date: str = "",
    limit: str = "20",
    status: str = "published"
) -> List[Dict]:
    """
    Retrieve events from the Ticket Tailor API.
    """
    start_ts = safe_unix(start_date)
    end_ts = safe_unix(end_date, fallback=start_ts + (60 * 24 * 60 * 60))  # 60 days ahead

    params = filter_params({
        "start_at.gte": start_ts,
        "end_at.lte": end_ts,
        "status": status,
        "limit": limit
    })

    return api_get("events", params)


# 🧾 Retrieve Ticket Tailor orders
@mcp.tool()
def get_ticket_tailor_orders(
    event_id: str = "",
    status: str = "completed",
    limit: str = "50",
    page: str = "1",
    created_at_min: str = "",
    created_at_max: str = "",
    updated_at_min: str = "",
    updated_at_max: str = "",
    include: str = "",
    sort_field: str = "",
    sort_direction: str = "",
    search: str = "",
    ticket_type_id: str = "",
    checkout_email: str = "",
    email: str = "",
    phone: str = "",
    payment_method: str = "",
    offline_payment_status: str = "",
    tag: str = "",
    name: str = ""
) -> List[Dict]:
    """
    Retrieve orders from the Ticket Tailor API.
    """
    # Convert date filters to Unix timestamps if provided
    params = {
        "created_at.gte": safe_unix(created_at_min) if created_at_min else "",
        "created_at.lte": safe_unix(created_at_max) if created_at_max else "",
        "updated_at.gte": safe_unix(updated_at_min) if updated_at_min else "",
        "updated_at.lte": safe_unix(updated_at_max) if updated_at_max else "",
        "event_id": event_id,
        "status": status,
        "limit": limit,
        "page": page,
        "include": include,
        "sort": sort_field,
        "sort_direction": sort_direction,
        "search": search,
        "ticket_type_id": ticket_type_id,
        "checkout.email": checkout_email,
        "buyer.email": email,
        "buyer.phone": phone,
        "payment_method": payment_method,
        "offline_payment_status": offline_payment_status,
        "tag": tag,
        "buyer.name": name
    }

    return api_get("orders", filter_params(params))


# 👋 Greeting example resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!" 