from marshmallow import Schema, fields


class TransactionSchema(Schema):
    sender = fields.Str(required=False)
    receiver = fields.Str()
    data = fields.Str()
    category = fields.Str()
    timestamp = fields.DateTime(required=False)
