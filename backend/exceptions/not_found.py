class ProductNotFoundError(Exception):
    """Exception raised when a product is not found in the database."""
    def __init__(self, product_id):
        self.message = f"Product with ID {product_id} not found."
        super().__init__(self.message)