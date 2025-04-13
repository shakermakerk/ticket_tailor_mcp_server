#!/usr/bin/env python3
"""
Example script to list upcoming Ticket Tailor events.

Make sure to set your TICKET_TAILOR_API_KEY environment variable
or create a .env file with this key before running.
"""

import os
import sys
import datetime
from dotenv import load_dotenv

# Import from the package (the pythonic way)
from ticket_tailor import get_ticket_tailor_events

# Load environment variables
load_dotenv()

def main():
    # Get today's date in ISO format
    today = datetime.datetime.now().isoformat()
    
    # Get events for the next 30 days
    print("Fetching upcoming events...")
    events = get_ticket_tailor_events(
        start_date=today,
        limit="10",
        status="published"
    )
    
    # Display the events
    if not events:
        print("No upcoming events found.")
        return
    
    print(f"\nFound {len(events)} upcoming events:\n")
    for event in events:
        event_id = event.get('id', 'Unknown ID')
        name = event.get('name', 'Unnamed Event')
        start = event.get('start', {}).get('iso')
        venue = event.get('venue', {}).get('name', 'No venue')
        
        print(f"* {name}")
        print(f"  ID: {event_id}")
        print(f"  Date: {start}")
        print(f"  Venue: {venue}")
        print("")

if __name__ == "__main__":
    main() 