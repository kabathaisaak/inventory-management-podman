from exceptions.validation import ValidationException


def validate_product(data):

    if not data:
        raise ValidationException(
            "Request body is required"
        )

    if "name" not in data:
        raise ValidationException(
            "Name is required"
        )

    if not str(data["name"]).strip():
        raise ValidationException(
            "Name cannot be empty"
        )

    if "price" not in data:
        raise ValidationException(
            "Price is required"
        )

    try:
        price = float(data["price"])
    except (ValueError, TypeError):
        raise ValidationException(
            "Price must be a number"
        )

    if price <= 0:
        raise ValidationException(
            "Price must be greater than zero"
        )