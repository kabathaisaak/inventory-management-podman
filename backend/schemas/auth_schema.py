from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):

    username = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=50
        )
    )

    password = fields.String(
        required=True,
        validate=validate.Length(
            min=8
        )
    )


class LoginSchema(Schema):

    username = fields.String(required=True)

    password = fields.String(required=True)


class RefreshSchema(Schema):

    refresh_token = fields.String(required=True)