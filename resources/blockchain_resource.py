from http import HTTPStatus

import requests
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from Blockchain import blockchain
from Transaction import Transaction
from models import TransactionSchema, TransmitTransactionSchema

SECURITY_NODE_URL = "http://127.0.0.1:8000"
TRANSACTION_TRANSMIT_URL = "/transmit-transaction"


class BlockChainResource(Resource):

    def get(self):
        return blockchain.chain_length

    def post(self):
        try:
            parsed_tx = TransactionSchema().loads(request.get_data())
            sender = request.host.split(":")[0]
            tx = Transaction(sender, parsed_tx.get("receiver"), parsed_tx.get("data"), parsed_tx.get("category"))
            blockchain.add_transaction(tx)
            block_id = blockchain.chain_length - 1
            tx_id = len(blockchain.last_block.transactions) - 1
            status_code, status_message, transmit_tx = self.transmit_transaction_to_receiver(tx, block_id, tx_id)
            if status_code == HTTPStatus.OK:
                return TransmitTransactionSchema().dump(transmit_tx), HTTPStatus.CREATED
            else:
                return status_message, status_code
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST

    @staticmethod
    def transmit_transaction_to_receiver(tx: Transaction, block_id: int, tx_id: int) -> tuple[int, str, dict]:
        transmit_tx = dict(block_id=block_id, tx_id=tx_id, sender=tx.sender, receiver=tx.receiver, data=tx.data,
                           category=tx.category, timestamp=tx.timestamp)
        data = TransmitTransactionSchema().dumps(transmit_tx)
        req = requests.post(url=SECURITY_NODE_URL + TRANSACTION_TRANSMIT_URL, data=data)
        return req.status_code, req.text, transmit_tx
