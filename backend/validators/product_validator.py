from exceptions.validation import ValidationException
def validate_product(data):
    """
    Validate a product payload.
    """

    if data is None:
        raise ValidationException(
            "Request body is required."
        )

    name = data.get("name")
    price = data.get("price")

    if name is None:
        raise ValidationException(
            "Product name is required."
        )

    if not isinstance(name, str):
        raise ValidationException(
            "Product name must be a string."
        )

    name = name.strip()

    if len(name) == 0:
        raise ValidationException(
            "Product name cannot be empty."
        )

    if len(name) > 100:
        raise ValidationException(
            "Product name cannot exceed 100 characters."
        )

    if price is None:
        raise ValidationException(
            "Price is required."
        )

    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValidationException(
            "Price must be a valid number."
        )

    if price <= 0:
        raise ValidationException(
            "Price must be greater than zero."
        )

    return {
        "name": name,
        "price": price
    }