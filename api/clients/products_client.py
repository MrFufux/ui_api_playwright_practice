from api.clients.base_client import BaseClient

class ProductsClient(BaseClient):
    
    # Constructor: initializes ProductsClient by calling BaseClient's constructor.
    def __init__(self, base_url = None):
        super().__init__(base_url)
        
    # Fetches all products from the API, optionally paginated via `limit`/`skip`.
    # These are only added to the query params when explicitly provided, so an
    # omitted value is left out of the request instead of being sent as the
    # literal string "None" (which the API would not interpret as "no limit").
    def get_all_products(self, limit: str | None = None, skip: str | None = None ):
        
        # empty dict
        params = {}
        
        if limit is not None:
            params['limit'] = limit
        
        if skip is not None:
            params['skip'] = skip
            
        return self.client.get("/products,", params=params)
    
    # Fetches the products by id from the API
    def get_products_by_id(self, product_id: int):
        return self.client.get(f"/products/{product_id}")
    
    # Fetches the product by search from the API
    def get_products_by_search(self, query_product: str):
        return self.client.get("products/search", params={"q": query_product})
            
        