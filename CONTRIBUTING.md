# Contributing to Ticket Tailor API Integration

Thank you for your interest in contributing to this project! Here's how you can help.

## Getting Started

1. Check the [Roadmap](ROADMAP.md) for endpoints that need implementation
2. Fork the repository
3. Clone your fork: `git clone https://github.com/yourusername/ticket_tailor_mcp_server.git`
4. Create a branch for your feature: `git checkout -b feature-name`

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # for development dependencies
   ```

2. Create a `.env` file with your Ticket Tailor API key for testing.

## Implementing New API Endpoints

We welcome contributions that implement new Ticket Tailor API endpoints. Please follow these steps:

1. Choose an endpoint from the [Roadmap](ROADMAP.md) that isn't yet implemented
2. Create an issue in the repository indicating which endpoint you're working on
3. Implement the endpoint following the established patterns in `src/ticket_tailor/ticket_tailor_funcs.py`
4. Create an example script if needed
5. Update the README.md if necessary
6. Submit a pull request

## Making Changes

1. Make your changes to the codebase
2. Ensure your code follows our coding standards

## Submitting a Pull Request

1. Push your changes to your fork
2. Submit a pull request to the main repository
3. Describe your changes in detail in the PR description
4. Link any related issues using keywords like "Fixes #123"
5. Update the ROADMAP.md to mark the implemented endpoint as complete

## Pull Request Process

1. Update the README.md or documentation with details of changes if applicable
2. The PR will be reviewed by maintainers
3. Address any feedback or requested changes
4. Once approved, your PR will be merged

## Coding Standards

- Follow PEP 8 guidelines for Python code
- Write docstrings for functions and classes
- Include type hints where appropriate
- Keep functions focused and concise
- Maintain consistent emoji usage in function comments (see existing code)

## Testing

- Manual testing is encouraged for new features or bug fixes
- Document how to test your changes in the PR description

## Reporting Bugs

If you find a bug, please open an issue with:

- A clear title and description
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any relevant logs or screenshots

## Suggesting Features

Feature suggestions are welcome! Please open an issue with:

- A clear title and description
- The problem the feature would solve
- Any potential implementation ideas

Thank you for contributing! 