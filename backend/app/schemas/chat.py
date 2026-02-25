from marshmallow import Schema, fields, validate

class ChatQuerySchema(Schema):
    query = fields.Str(required=True, validate=validate.Length(min=1))
    conversation_history = fields.List(fields.Dict(), load_default=[])

class ChatResponseSchema(Schema):
    response = fields.Str()
    confidence = fields.Float()
    disclaimer = fields.Str()
