from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from Blockchain import blockchain
from Transaction import Transaction
from models import TransactionSchema


class BlockChainResource(Resource):
    def get(self):
        return blockchain.chain_length

    def post(self):
        try:
            parsed_tx = TransactionSchema().loads(request.get_data())
            sender = request.remote_addr + ":" + str(request.environ['REMOTE_PORT'])
            tx = Transaction(sender, parsed_tx.get("receiver"), parsed_tx.get("data"))
            blockchain.add_transaction(tx)
            return TransactionSchema().dump(tx)
        except ValidationError as err:
            return err.messages, 400
