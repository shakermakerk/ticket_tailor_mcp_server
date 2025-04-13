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

from util_funcs import convert_date_to_unix, safe_unix, get_auth_header, api_get, filter_params

# 🚀 Create MCP server instance
tt_mcp = FastMCP("tt-events")


# 📅 Retrieve Ticket Tailor events
@tt_mcp.tool()
def get_ticket_tailor_events(
    start_date: str = "",
    end_date: str = "",
    limit: str = "20",
    status: str = "published"
) -> List[Dict]:
    """
    Retrieve events from the Ticket Tailor API based on specified filters.
    Returns results wrapped in an object with a .content attribute containing the JSON string.

    Args:
        start_date: Optional. The start date for filtering events (ISO 8601 format, e.g., 'YYYY-MM-DDTHH:MM:SSZ'). Defaults to empty string (no specific start date).
        end_date: Optional. The end date for filtering events (ISO 8601 format). Defaults to 60 days after the start date if provided, otherwise uses current time + 60 days.
        limit: Optional. The maximum number of events to retrieve. Defaults to '20'.
        status: Optional. The status of the events to retrieve (e.g., 'published', 'draft', 'cancelled'). Defaults to 'published'.
    """
    start_ts = safe_unix(start_date)
    end_ts = safe_unix(end_date, fallback=start_ts + (60 * 24 * 60 * 60))  # 60 days ahead

    params = filter_params({
        "start_at.gte": start_ts,
        "end_at.lte": end_ts,
        "status": status,
        "limit": limit
    })

    result = api_get("events", params)
    # Return the raw result data
    return result


# 🧾 Retrieve Ticket Tailor orders
@tt_mcp.tool()
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
    Retrieve orders from the Ticket Tailor API based on various filters.
    Returns a list of order objects.

    Args:
        event_id: Optional. Filter orders by a specific event ID.
        status: Optional. Filter orders by status (e.g., 'completed', 'pending', 'cancelled'). Defaults to 'completed'.
        limit: Optional. Maximum number of orders per page. Defaults to '50'.
        page: Optional. Page number for pagination. Defaults to '1'.
        created_at_min: Optional. Filter orders created on or after this date (ISO 8601 format).
        created_at_max: Optional. Filter orders created on or before this date (ISO 8601 format).
        updated_at_min: Optional. Filter orders updated on or after this date (ISO 8601 format).
        updated_at_max: Optional. Filter orders updated on or before this date (ISO 8601 format).
        include: Optional. Comma-separated list of related resources to include (e.g., 'tickets').
        sort_field: Optional. Field to sort orders by (e.g., 'created_at').
        sort_direction: Optional. Sort direction ('asc' or 'desc').
        search: Optional. Search term to filter orders by (searches across multiple fields like name, email).
        ticket_type_id: Optional. Filter orders by a specific ticket type ID.
        checkout_email: Optional. Filter orders by the email used during checkout.
        email: Optional. Filter orders by the buyer's email address.
        phone: Optional. Filter orders by the buyer's phone number.
        payment_method: Optional. Filter orders by payment method (e.g., 'stripe', 'paypal').
        offline_payment_status: Optional. Filter orders by offline payment status (e.g., 'paid', 'unpaid').
        tag: Optional. Filter orders by a specific tag.
        name: Optional. Filter orders by the buyer's name.
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

    result = api_get("orders", filter_params(params))
    return result


# ⏰ Get current date and time
@tt_mcp.tool()
def get_current_datetime(format: str = "iso") -> Dict[str, str]:
    """
    Get the current date and time in the specified format.
    
    Args:
        format: Optional. The format to return the date in. Options:
               - "iso": ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
               - "date": Date only (YYYY-MM-DD)
               - "unix": Unix timestamp (seconds since epoch)
               - "all": Return all formats in a dictionary
               Defaults to "iso".
    
    Returns:
        A dictionary containing the current date and time in the requested format(s).
    """
    now = datetime.datetime.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + datetime.timedelta(days=1)
    
    # Format according to the requested format
    if format == "all":
        return {
            "iso": now.isoformat() + "Z",
            "date": now.strftime("%Y-%m-%d"),
            "unix": int(now.timestamp()),
            "today_start_iso": today.isoformat() + "Z",
            "today_end_iso": tomorrow.isoformat() + "Z",
            "today_start_unix": int(today.timestamp()),
            "today_end_unix": int(tomorrow.timestamp())
        }
    elif format == "date":
        return {"date": now.strftime("%Y-%m-%d")}
    elif format == "unix":
        return {"unix": int(now.timestamp())}
    else:  # Default to ISO format
        return {"iso": now.isoformat() + "Z"}


if __name__ == "__main__":
    tt_mcp.run(transport="stdio")