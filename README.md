# UI/API Playwright Practice Framework

This repository contains a practice framework for automating UI interactions and API testing using Python, Playwright, and HTTP clients.

## Project Structure

The project is organized to separate concerns between UI automation, API testing, and utility functions.

- **`pages/`**: Contains page object definitions and page-specific logic.
    - `base_page.py`: Base class for common page elements and methods.
- **`test/API/`**: Directory for tests focusing on API endpoints.
- **`test/UI/`**: Directory for tests focusing on UI interactions.
- **`utils/`**: Contains helper functions and utilities.
    - `helpers.py`: Utility functions for common operations.
- **`conftest.py`**: Pytest fixtures and setup configurations for Playwright and testing environments.
- **`pyproject.toml`**: Project metadata, dependencies, and pytest configuration.

## Technology Stack

- **Testing**: `pytest`
- **UI Automation**: `playwright`
- **HTTP Requests**: `httpx` / `requests`
- **Language**: Python

## Setup and Running Tests

To set up the environment and run tests, follow these steps:

1.  **Install Dependencies**: Install all required packages listed in `pyproject.toml`.
    ```bash
    pip install -r requirements.txt # Assuming you have a requirements.txt or similar dependency list
    # Or install directly from pyproject.toml
    pip install pytest pytest-playwright playwright httpx requests
    ```

2.  **Install Browser Binaries**: Ensure Playwright browsers are installed.
    ```bash
    playwright install
    ```

3.  **Run Tests**: Execute your tests using `pytest`.
    ```bash
    pytest
    ```

## Testing Philosophy

This framework promotes a clear separation of concerns:
- **API Tests**: Focus on backend logic and API contracts.
- **UI Tests**: Focus on end-to-end user flows via Playwright.
- **Utilities**: Keep reusable functions separate for maintainability.