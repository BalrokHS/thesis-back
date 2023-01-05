from flask import Flask
from flask_restful import Api
from resources import BlockChainResource, SecurityNodeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(BlockChainResource, '/')
api.add_resource(SecurityNodeResource, '/security-node')


if __name__ == '__main__':
    app.run()
