# API Testing — Step-by-Step Learning Guide

## Context

The user is studying test automation and wants to build the API-testing side of their
framework (currently only comment-placeholders exist under `api/` and `tests/API/`)
against `https://dummyjson.com`. This is explicitly a **learning exercise** — the user
will write the code themselves, following guidance one step at a time. No files should
be created or edited by the assistant as part of this plan; this document is the
lesson/step sequence to walk through together in conversation, confirming each step
before moving to the next.

Existing conventions to follow (observed in `pages/base_page.py`, `pages/text_box_page.py`,
`tests/UI/test_text_box.py`):
- Heavy explanatory comments — the user is using this codebase to learn OOP concepts
  (inheritance, encapsulation) as much as testing.
- AAA pattern (`# 1. Arrange`, `# 2. Act`, `# 3. Assert`) in every test.
- `pytest.mark.ui` / `pytest.mark.api` markers already defined in `pyproject.toml`.
- Page objects inherit from `BasePage`; the API equivalent should be client classes
  inheriting from a `BaseClient`.

Known scaffold mismatch to address during the walkthrough: `api/clients/orders_client.py`
and `api/models/order.py` were empty placeholders that don't match dummyjson (which has
`carts`, not `orders`) — already partially addressed (`api/models/carts.py` now exists).

## Guide Structure

Walk the user through these steps **one at a time**, in the chat — explain the concept,
show a small code sketch as an example (not written to their files), then let them write
it themselves and confirm before moving on. Do not batch all steps into one dump.

### Step 1 — Understand the client/resource pattern ✅ done
### Step 2 — Explore the target API ✅ done
### Step 3 — Build `BaseClient` ✅ done
### Step 4 — Build `AuthClient` ✅ done
### Step 5 — Build `ProductsClient` ✅ done

### Step 6 — Wire up `tests/API/conftest.py`
Session-scoped fixtures: `api_base_url` (env-driven, like `browser_context_args` does for
UI), a `products_client` fixture, and an `auth_token` fixture that logs in once per
session via `AuthClient`.

### Step 7 — Write the first test file
`tests/API/test_products.py` using the same AAA-commented style as `test_text_box.py`:
status code assertions, key fields present in the JSON body, pagination params respected.

### Step 8 — Write auth tests
`tests/API/test_auth.py`: successful login (token present), invalid credentials (401).

### Step 9 — Run and verify
`pytest -m api -v` (or the project's existing `addopts`), check `report.html` is
generated, confirm both `ui` and `api` marker suites still collect independently.

### Step 10 — Only after Steps 1–9 land
Revisit any remaining `carts`/`users` client scaffolding and repeat the Step 3–7 pattern
for additional resources if the user wants to keep going.

## Verification

No automated verification from the assistant side for this plan — it's a teaching
sequence. Verification per step is the user successfully running the code they wrote
(e.g. `pytest -m api -v` passing) before moving to the next step.
