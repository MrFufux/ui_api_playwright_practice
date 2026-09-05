from api.clients.base_client import BaseClient

class AuthClient(BaseClient):
    
    # Constructor: initializes AuthClient by calling BaseClient's constructor
    def __init__(self, base_url = None):
        super().__init__(base_url)
        
    # Login method
    def login(self, username: str, password: str):
        payload = {"username": username, "password": password}
        return self.client.post("auth/login", json=payload)