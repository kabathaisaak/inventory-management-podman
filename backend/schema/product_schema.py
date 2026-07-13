from marshmallow import Schema, fields, validate


class ProductSchema(Schema):

    name = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=100
        )
    )

    price = fields.Float(
        required=True,
        validate=validate.Range(
            min=0.01
        )
    )