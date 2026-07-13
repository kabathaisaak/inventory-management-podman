from marshmallow import Schema, fields, validate


class ProductSchema(Schema):

    name = fields.String(
        required=True,
        error_messages={
            "required": "Product name is required."
        },
        validate=validate.Length(
            min=3,
            max=100
        )
    )

    price = fields.Float(
        required=True,
        error_messages={
            "required": "Price is required."
        },
        validate=validate.Range(
            min=0.01,
            error="Price must be greater than zero."
        )
    )