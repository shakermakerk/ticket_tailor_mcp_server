#!/usr/bin/env python3
"""
Example script to list Ticket Tailor orders for a specific event.

Make sure to set your TICKET_TAILOR_API_KEY environment variable
or create a .env file with this key before running.
"""

import os
import sys
import argparse
from dotenv import load_dotenv

# Add parent directory to path to import ticket_tailor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ticket_tailor import get_ticket_tailor_orders

# Load environment variables
load_dotenv()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Retrieve orders for a Ticket Tailor event')
    parser.add_argument('--event-id', help='Event ID to retrieve orders for')
    parser.add_argument('--limit', default='10', help='Maximum number of orders to retrieve')
    parser.add_argument('--status', default='completed', help='Order status to filter by')
    args = parser.parse_args()
    
    # If no event ID provided, show usage
    if not args.event_id:
        print("Please provide an event ID using the --event-id parameter.")
        print("Example: python list_orders.py --event-id evt-abcd1234")
        return
    
    # Get orders for the specified event
    print(f"Fetching orders for event {args.event_id}...")
    orders = get_ticket_tailor_orders(
        event_id=args.event_id,
        status=args.status,
        limit=args.limit
    )
    
    # Display the orders
    if not orders:
        print("No orders found.")
        return
    
    print(f"\nFound {len(orders)} orders:\n")
    for order in orders:
        order_id = order.get('id', 'Unknown ID')
        status = order.get('status', 'Unknown status')
        
        # Handle total_paid which might be a dict or a simple value
        total_paid = order.get('total_paid', {})
        if isinstance(total_paid, dict):
            total = total_paid.get('formatted', 'Unknown amount')
        else:
            total = f"{total_paid} (no currency info)"
            
        buyer_name = order.get('buyer', {}).get('name', 'Unknown buyer')
        ticket_count = len(order.get('tickets', []))
        
        print(f"* Order {order_id}")
        print(f"  Status: {status}")
        print(f"  Buyer: {buyer_name}")
        print(f"  Total: {total}")
        print(f"  Tickets: {ticket_count}")
        print("")

if __name__ == "__main__":
    main() 