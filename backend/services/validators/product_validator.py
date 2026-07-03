def validate_product(data):
    if not data:
        return "Request body is required"

    if "name" not in data:
        return "Product name is required"

    if "price" not in data:
        return "Product price is required"

    if not isinstance(data["name"], str):
        return "Product name must be a string"

    if data["name"].strip() == "":
        return "Product name cannot be empty"

    try:
        price = float(data["price"])
    except (ValueError, TypeError):
        return "Product price must be a number"

    if price <= 0:
        return "Product price must be greater than zero"

    return None