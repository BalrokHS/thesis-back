import os

from flask import Flask
from flask_restful import Api
from resources import BlockChainResource, SecurityNodeResource, ReceiveResource, TransactionRetrieveResource

# Indexing mechanism
import index

app = Flask(__name__)
api = Api(app)

api.add_resource(BlockChainResource, '/')
api.add_resource(SecurityNodeResource, '/security-node')
api.add_resource(ReceiveResource, '/receive-tx')
api.add_resource(TransactionRetrieveResource, '/tx/<string:category>')

if __name__ == '__main__':
    os.makedirs('./data', exist_ok=True)
    app.run()
