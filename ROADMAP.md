# Ticket Tailor API Roadmap

This roadmap outlines the planned implementation of Ticket Tailor API endpoints, prioritized based on their usefulness for AI agents.

## Priority 1: Core Event & Order Management

These endpoints provide the essential functionality for managing events and orders:

- ✅ GET /events - List all events (already implemented)
- ✅ GET /orders - List all orders (already implemented)
- [ ] GET /events/{id} - Get a single event (high priority)
- [ ] GET /orders/{id} - Get a single order (high priority)
- [ ] GET /ticket-types - List all ticket types
- [ ] GET /ticket-types/{id} - Get a single ticket type

## Priority 2: Ticket & Attendee Management

These endpoints are useful for managing individual tickets and attendees:

- [ ] GET /issued-tickets - List all issued tickets
- [ ] GET /issued-tickets/{id} - Get a single issued ticket
- [ ] PATCH /issued-tickets/{id} - Update an issued ticket
- [ ] POST /issued-tickets/{id}/check-in - Check in an issued ticket

## Priority 3: Extended Event Management

These endpoints provide more detailed management capabilities:

- [ ] PATCH /events/{id} - Update an event
- [ ] POST /events - Create an event
- [ ] GET /events/{id}/ticket-types - Get event ticket types
- [ ] POST /orders - Create a new order
- [ ] PATCH /orders/{id} - Update an order

## Priority 4: Advanced Features

These endpoints provide additional functionality that may be useful in specific scenarios:

- [ ] GET /discount-codes - List all discount codes
- [ ] POST /discount-codes - Create a discount code
- [ ] GET /voucher-codes - List all voucher codes
- [ ] GET /waitlists - List all waitlists

## Priority 5: Administrative Functions

These endpoints might be less commonly used by AI agents but provide useful administrative capabilities:

- [ ] POST /events/{id}/publish - Publish an event
- [ ] POST /events/{id}/unpublish - Unpublish an event
- [ ] POST /orders/{id}/payment-confirmation - Confirm offline payment

## Implementation Guidelines

When implementing new endpoints, please follow these guidelines:

1. Add the new function to `src/ticket_tailor/ticket_tailor_funcs.py`
2. Include comprehensive type hints and docstrings
3. Create an example script in the `src/ticket_tailor/examples` directory if needed
4. Update the README.md to document the new functionality

## Contribution Process

1. Pick an endpoint from the roadmap that isn't yet implemented
2. Create an issue in the repository to track your work
3. Create a branch and implement the endpoint following the guidelines above
4. Submit a pull request referencing the issue

## API Documentation

For detailed information about the Ticket Tailor API, please refer to the [official API documentation](https://developers.tickettailor.com/docs/api/). 