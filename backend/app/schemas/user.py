from marshmallow import Schema, fields, validate

class UserRegistrationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
    name = fields.Str(required=True)

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email()
    name = fields.Str()
    role = fields.Str()
    created_at = fields.DateTime(dump_only=True)
