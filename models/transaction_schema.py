from marshmallow import Schema, fields


class TransactionSchema(Schema):
    sender = fields.Str()
    receiver = fields.Str()
    data = fields.Str()
