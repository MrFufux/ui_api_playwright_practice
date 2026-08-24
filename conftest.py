# Heart of Pytest
# Dependency injection hub
# Holds all the fixtures (setup and teardowns)
# Tests file stay clean

import pytest
import os
from playwright.sync_api import Page
from typing import Generator


# ----------------------------------------------------------------------
# 1. PLAYWRIGHT BROWSER CONTEXT CONFIGURATION
# ----------------------------------------------------------------------

# Intercepts and overrides the default Playwright browser context.
# Demonstrates environment control for CI/CD consistency.
@pytest.fixture(scope='session')
def browser_context_args(browser_context_args: dict) -> dict:
    
    # Fallback to a default if the env varuiable isn't set
    base_url = os.getenv('UI_BASE_URL', 'https://demoqa.com/')
    
    return {
        # **: takes all the existing key-value pairs from the 
        # default browser_context_args dict and modifies it into
        # a new dict that I'm creating.
        # Add custom settings without losing the original data
        **browser_context_args,
        "viewport": {"width":1920, "height":1080},
        "base_url": {base_url}
    }

# ----------------------------------------------------------------------
# 2. CUSTOM UI PAGE WRAPPER
# ----------------------------------------------------------------------

# Custom fixture that wraps  the default Playwright page.
# It automatically navigates to the base URL before the test starts,
# keeping our test files DRY
@pytest.fixture(scope='function')
def ui_page(page:Page) -> Generator:
    # Setup: Go to the homepage before the test begins
    page.goto('/')
    # yield hands control over to the actual test function
    yield page
    
    # Yield encapsulates the setup and teardown logic into a single function
    # Yield pauses the fixture, allows the test to run and then,
    # the cleanup happens and don't leave any garbage when the test finishes.
    
    