# Heart of Pytest
# Dependency injection hub
# Holds all the fixtures (setup and teardowns)
# Tests file stay clean

import pytest
import os


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
        # default browser_context_args dict and modifys it into
        # a new dict that I'm creating.
        # Add custom settings without losing the original data
        **browser_context_args,
        "viewport": {"width":1920, "height":1080},
        "base_url": {base_url}
    }