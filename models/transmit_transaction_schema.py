from marshmallow import Schema, fields


class TransmitTransactionSchema(Schema):
    block_id = fields.Integer()
    tx_id = fields.Integer()
    sender = fields.Str(required=False)
    receiver = fields.Str()
    data = fields.Str()
    category = fields.Str()
    timestamp = fields.DateTime(required=False)
