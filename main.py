from flask import Flask

from Blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()
blockchain.create_genesis_block()


@app.route('/')
def hello_world():
    return str(blockchain.chain_length)


if __name__ == '__main__':
    app.run()
