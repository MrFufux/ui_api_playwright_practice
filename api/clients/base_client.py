# wraps httpx.Client: base_url, headers, auth, logging

import httpx
import os

class BaseClient:
    def __init__(self, base_url: str | None = None):
        # fall back to API_BASE_URL env var, then dummyjson as a last resort
        base_url = base_url or os.getenv('API_BASE_URL', 'https://dummyjson.com/')
        self.client = httpx.Client(base_url = base_url)

    def set_auth_token(self, token: str):
        # attaches a bearer token to all subsequent requests on this client
        self.client.headers.update({'Authorization': f'Bearer {token}'})
        
        