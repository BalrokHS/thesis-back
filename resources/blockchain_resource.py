from http import HTTPStatus

import requests
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from Blockchain import blockchain
from Transaction import Transaction
from models import TransactionSchema

SECURITY_NODE_URL = "http://127.0.0.1:8000"
TRANSACTION_TRANSMIT_URL = "/transmit-transaction"


class BlockChainResource(Resource):

    def get(self):
        return blockchain.chain_length

    def post(self):
        try:
            parsed_tx = TransactionSchema().loads(request.get_data())
            tx = Transaction(request.host, parsed_tx.get("receiver"), parsed_tx.get("data"))
            status_code, status_message = self.transmit_transaction_to_receiver(tx)
            if status_code == HTTPStatus.OK:
                blockchain.add_transaction(tx)
                return TransactionSchema().dump(tx), HTTPStatus.CREATED
            else:
                return status_message, status_code
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST

    @staticmethod
    def transmit_transaction_to_receiver(tx: Transaction) -> tuple[int, str]:
        data = TransactionSchema().dumps(tx)
        req = requests.post(url=SECURITY_NODE_URL + TRANSACTION_TRANSMIT_URL, data=data)
        return req.status_code, req.text
