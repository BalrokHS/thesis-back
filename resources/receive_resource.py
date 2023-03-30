from http import HTTPStatus

from flask_restful import Resource

from Blockchain import blockchain
from Transaction import Transaction
from models import TransactionSchema
from flask import request


class ReceiveResource(Resource):
    def post(self):
        received_data = TransactionSchema().loads(request.get_data())

        tx = Transaction(received_data.get('sender'), received_data.get('receiver'), received_data.get('data'),
                         received_data.get('category'), received_data.get('timestamp'))

        blockchain.add_transaction(tx)

        return '', HTTPStatus.OK
