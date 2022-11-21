from marshmallow import fields, Schema


class CreateSchema(Schema):
    name = fields.Str(required=True)

class ClientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    user_id = fields.Int(dump_only=True)
    client_id = fields.Str(dump_only=True)
    client_secret = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)