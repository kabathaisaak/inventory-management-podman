GET_PRODUCTS_DOC = {
    "tags": ["Products"],
    "summary": "Get all products",
    "description": "Retrieve a paginated list of products with optional filtering and sorting.",
    "produces": ["application/json"],
    "parameters": [
        {
            "name": "page",
            "in": "query",
            "type": "integer",
            "default": 1
        },
        {
            "name": "limit",
            "in": "query",
            "type": "integer",
            "default": 10
        },
        {
            "name": "name",
            "in": "query",
            "type": "string",
            "description": "Filter products by name"
        },
        {
            "name": "sort",
            "in": "query",
            "type": "string",
            "enum": ["id", "name", "price"],
            "default": "id"
        },
        {
            "name": "order",
            "in": "query",
            "type": "string",
            "enum": ["asc", "desc"],
            "default": "asc"
        }
    ],
    "responses": {
        200: {
            "description": "Products retrieved successfully"
        }
    }
}


GET_PRODUCT_DOC = {
    "tags": ["Products"],
    "summary": "Get product by ID",
    "description": "Retrieve a product by its ID.",
    "produces": ["application/json"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Product ID"
        }
    ],
    "responses": {
        200: {
            "description": "Product retrieved successfully"
        },
        404: {
            "description": "Product not found"
        }
    }
}


CREATE_PRODUCT_DOC = {
    "tags": ["Products"],
    "summary": "Create a product",
    "description": "Create a new product.",
    "security": [
        {
            "Bearer": []
        }
    ],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["name", "price"],
                "properties": {
                    "name": {
                        "type": "string",
                        "example": "Laptop"
                    },
                    "price": {
                        "type": "number",
                        "example": 50000
                    }
                }
            }
        }
    ],
    "responses": {
        201: {
            "description": "Product created successfully"
        },
        400: {
            "description": "Validation error"
        },
        401: {
            "description": "Unauthorized"
        },
        403: {
            "description": "Forbidden"
        }
    }
}


UPDATE_PRODUCT_DOC = {
    "tags": ["Products"],
    "summary": "Update a product",
    "description": "Update an existing product.",
    "security": [
        {
            "Bearer": []
        }
    ],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Product ID"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["name", "price"],
                "properties": {
                    "name": {
                        "type": "string",
                        "example": "Gaming Mouse"
                    },
                    "price": {
                        "type": "number",
                        "example": 3500
                    }
                }
            }
        }
    ],
    "responses": {
        200: {
            "description": "Product updated successfully"
        },
        400: {
            "description": "Validation error"
        },
        401: {
            "description": "Unauthorized"
        },
        403: {
            "description": "Forbidden"
        },
        404: {
            "description": "Product not found"
        }
    }
}


DELETE_PRODUCT_DOC = {
    "tags": ["Products"],
    "summary": "Delete a product",
    "description": "Delete a product by its ID.",
    "security": [
        {
            "Bearer": []
        }
    ],
    "produces": ["application/json"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Product ID"
        }
    ],
    "responses": {
        200: {
            "description": "Product deleted successfully"
        },
        401: {
            "description": "Unauthorized"
        },
        403: {
            "description": "Forbidden"
        },
        404: {
            "description": "Product not found"
        }
    }
}