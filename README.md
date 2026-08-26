# UI/API Test Automation Framework

A Python-based test automation framework covering both UI and API testing layers, built on Playwright, httpx, and pytest. It follows the Page Object Model (POM) pattern and uses environment-variable-driven configuration.

## Project Structure

```
.
├── pages/                  # Page Object Model classes for UI tests
│   ├── base_page.py        # Playwright wrapper with centralized 
│   ├── login_page.py
│   └── home_page.py
├── api/
│   ├── base_client.py      # httpx wrapper with shared headers/timeout
│   └── endpoints/
│       └── users_client.py
├── tests/
│   ├── ui/                 # UI test cases
│   └── api/                # API test cases
├── utils/
│   └── config.py           # Environment-variable-driven configuration
├── conftest.py             # Shared pytest fixtures
├── pyproject.toml
└── README.md
```

All packages (`pages/`, `api/`, `tests/`, `utils/`) include `__init__.py` files following standard Python packaging conventions.

## Technology Stack

- **Test runner**: `pytest`
- **UI automation**: `playwright` (sync API)
- **API client**: `httpx`
- **Design pattern**: Page Object Model (POM)

## Design Principles

- **Business-method pattern**: Page objects expose high-level actions (e.g. `login_page.log_in(user, password)`) rather than raw locator interactions, keeping tests readable and resilient to UI changes.
- **Property-based locators**: Locators are defined as properties on page objects rather than inline selectors, improving maintainability.
- **Fixture isolation**: `conftest.py` provides a session-scoped browser fixture, a per-test page/context fixture, and an API client fixture. The `screenshot_on_failure` autouse hook conditionally resolves the `page` fixture via `request.getfixturevalue("page")` — checking `request.fixturenames` first — so that pure API tests never trigger browser instantiation.

## Setup and Running Tests

1. **Install dependencies**
   ```bash
   pip install -r pyproject.toml
   ```

2. **Install Playwright browser binaries**
   ```bash
   playwright install
   ```

3. **Run tests**
   ```bash
   pytest                    # run everything
   pytest tests/ui/          # UI tests only
   pytest tests/api/         # API tests only
   ```

## Testing Philosophy

- **UI tests** (`tests/ui/`) exercise end-to-end user flows through Playwright, driven by Page Object classes in `pages/`.
- **API tests** (`tests/api/`) exercise backend contracts directly through the httpx-based client in `api/`, independent of the browser.
- **Utilities** (`utils/`) hold cross-cutting concerns like configuration, kept separate so both layers can share them without duplication.
- Fixtures are scoped and isolated so that UI-only overhead (browser startup) is never paid by API-only tests, and vice versa.
