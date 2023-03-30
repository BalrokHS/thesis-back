from http import HTTPStatus

from flask_restful import Resource

from index import retrieve_transactions_by_category


class TransactionRetrieveResource(Resource):
    def get(self, category: str):
        txs = retrieve_transactions_by_category(category)
        return txs, HTTPStatus.OK
