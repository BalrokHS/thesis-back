from marshmallow import Schema, fields
from models import TransactionSchema


class BlockSchema(Schema):
    id = fields.Integer()
    timestamp = fields.Float()
    previous_hash = fields.Str()
    transactions = fields.List(fields.Nested(TransactionSchema))