# UI/API Test Automation Framework

A Python-based test automation framework covering both UI and API testing layers, built on Playwright, httpx, and pytest. It follows the Page Object Model (POM) pattern and uses environment-variable-driven configuration.

> **Status: early scaffolding.** The directory structure and packaging are in place; most modules are stubs (comments only, no implementation yet). See "What's implemented" below.

## Project Structure

```
.
├── pages/
│   └── base_page.py        # Playwright page wrapper (WIP)
├── api/
│   ├── clients/
│   │   ├── base_client.py  # httpx wrapper: base_url, headers, auth, logging (stub)
│   │   ├── user_client.py  # (stub)
│   │   └── orders_client.py # (stub)
│   └── models/
│       ├── user.py         # response schema (stub)
│       └── order.py        # response schema (stub)
├── tests/
│   ├── UI/
│   │   └── conftest.py     # UI-only fixtures (stub)
│   └── API/
│       └── conftest.py     # API-only fixtures (stub)
├── utils/
│   └── helpers.py          # shared helpers: data builders, env config (stub)
├── conftest.py             # root fixtures: browser_context_args, ui_page
├── pyproject.toml
└── README.md
```

## Technology Stack

- **Test runner**: `pytest`
- **UI automation**: `playwright` (sync API, via `pytest-playwright`)
- **API client**: `httpx`
- **Reporting**: `pytest-html`, `allure-pytest`
- **Other**: `pytest-xdist` (parallel runs), `pytest-rerunfailures`, `python-dotenv`
- **Design pattern**: Page Object Model (POM)

## What's implemented

- Root `conftest.py`:
  - `browser_context_args` — overrides viewport (1920x1080) and sets `base_url` from `UI_BASE_URL` env var (defaults to `https://xqa.io/practice`).
  - `ui_page` — wraps Playwright's `page` fixture, navigating to `/` before each test.
- `pages/base_page.py` — `BasePage` base class taking a `Page` in its constructor; page objects will subclass this.

Everything else (`api/clients/*`, `api/models/*`, `utils/helpers.py`, `tests/UI/conftest.py`, `tests/API/conftest.py`) is a placeholder file with a comment describing its intended purpose — no logic yet.

## Setup and Running Tests

1. **Install dependencies**
   ```bash
   pip install -e .
   ```

2. **Install Playwright browser binaries**
   ```bash
   playwright install
   ```

3. **Run tests**
   ```bash
   pytest                    # run everything
   pytest tests/UI/          # UI tests only
   pytest tests/API/         # API tests only
   ```

   Or by marker (once tests are tagged):
   ```bash
   pytest -m ui
   pytest -m api
   ```

## Testing Philosophy

- **UI tests** (`tests/UI/`) will exercise end-to-end user flows through Playwright, driven by Page Object classes in `pages/`.
- **API tests** (`tests/API/`) will exercise backend contracts directly through the httpx-based client in `api/clients/`, independent of the browser.
- **Utilities** (`utils/`) hold cross-cutting concerns like configuration and data builders, shared by both layers.
