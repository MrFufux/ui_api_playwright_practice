# API-only fixture: http client, auth token, etc.

import os
import pytest
from api.clients.products_client import ProductsClient
from api.clients.auth_client import AuthClient

# fixture for each session
@pytest.fixture(scope='session')
def api_base_url():
    return os.getenv("API_BASE_URL", "https://dummyjson.com")

# fixture that gives a ready ProductsClient instance to the test
@pytest.fixture(scope='session')
def products_client(api_base_url):
    return ProductsClient(base_url=api_base_url)

# fixture to log in once per test session and returns the token string
@pytest.fixture(scope='session')
def auth_token(api_base_url):
    auth_client = AuthClient(base_url=api_base_url)
    response = auth_client.login("emilys", "emilyspass") # this will change
    return response.json()["accessToken"]