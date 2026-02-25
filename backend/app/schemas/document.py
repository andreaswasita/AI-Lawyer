from marshmallow import Schema, fields

class DocumentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    title = fields.Str()
    content = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class DocumentGenerateSchema(Schema):
    type = fields.Str(required=True)
    title = fields.Str(required=True)
    template_data = fields.Dict(load_default={})
