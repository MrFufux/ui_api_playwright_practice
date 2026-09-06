# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

This is a **learning project**: the user is studying test automation (OOP, Playwright, API testing) and wants to write most of the code themselves, following guidance step by step rather than having it generated for them. When adding new API clients, page objects, or tests, prefer walking the user through the pattern (with a small example sketch) over writing the full file yourself, unless they explicitly ask you to just write the code. See `.claude/plans/api-testing-learning-plan.md` for the in-progress API-testing walkthrough and its conventions.

The `README.md` describes an earlier scaffolding stage and is now stale — `api/clients/base_client.py`, `auth_client.py`, and `products_client.py` are implemented, not stubs. Trust the code over the README.

## Commands

```bash
pip install -e .              # install dependencies
playwright install            # install Playwright browser binaries

pytest                        # run everything
pytest tests/UI/              # UI tests only
pytest tests/API/             # API tests only
pytest -m ui                  # by marker
pytest -m api                 # by marker
pytest tests/UI/test_text_box.py::test_text_box_creation   # single test
```

`addopts` in `pyproject.toml` always generates `report.html` (self-contained) on every run.

Env vars: `UI_BASE_URL` (default `https://xqa.io/practice`), `API_BASE_URL` (default `https://dummyjson.com/`).

## Architecture

Two independent test layers sharing the same conventions, wired together by pytest markers (`ui`, `api` — defined in `pyproject.toml`):

- **UI layer** — Page Object Model. `pages/base_page.py` defines `BasePage` with reusable primitives (`click_element`, `fill_text`, `wait_for_element_visible`, `navigate`) that accept either a raw locator string or a Playwright `Locator`. Concrete pages (`pages/text_box_page.py`, `pages/check_box_page.py`) subclass `BasePage`, declare locators as instance attributes in `__init__`, and expose action methods. Root `conftest.py` provides `browser_context_args` (sets viewport + `base_url` from `UI_BASE_URL`) and `ui_page` (navigates to `''` — not `'/'` — before each test, to preserve the base URL's path).

- **API layer** — client-per-resource pattern. `api/clients/base_client.py` defines `BaseClient`, wrapping an `httpx.Client` with `base_url` (from `API_BASE_URL`) and a `set_auth_token` helper for bearer auth. Resource clients (`api/clients/auth_client.py`, `api/clients/products_client.py`) subclass `BaseClient` and expose methods returning raw `httpx.Response` objects (no response parsing/models wired in yet — `api/models/*.py` are placeholders for future pydantic schemas). Target API is `https://dummyjson.com`.

- `tests/UI/conftest.py` and `tests/API/conftest.py` are layer-scoped fixture files (UI's is currently empty; API's is not yet wired — see the learning plan's Step 6 for the intended `api_base_url`/`products_client`/`auth_token` fixtures).

- `utils/helpers.py` is an empty placeholder for cross-cutting helpers (data builders, env config) shared by both layers.

## Conventions to follow in this codebase

- Tests use the AAA pattern with explicit `# 1. Arrange`, `# 2. Act`, `# 3. Assert` comments.
- Comments lean heavily explanatory (OOP concepts, why a line is written a certain way) — this is intentional for a learning codebase; match that style in files following the same pattern rather than stripping comments down.
- Every test function is tagged `@pytest.mark.ui` or `@pytest.mark.api`.
- When walking the user through a new step (per the learning plan) and showing a code snippet/example, explain each line (or small group of related lines) after the snippet — what it does and why — rather than just describing the pattern at a high level.
