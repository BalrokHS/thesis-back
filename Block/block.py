import json
import os
import sys
from hashlib import sha256

from Transaction import Transaction
from index import index_new_data
from models import BlockSchema, TransactionSchema


def block_dir(x) -> str:
    return "data/block-{}.json".format(x)


class Block:
    def __init__(self, index: int, transactions: [], timestamp: float, previous_hash: str):
        self.index: int = index
        self.transactions: [] = transactions
        self.timestamp: float = timestamp
        self.previous_hash: str = previous_hash

        # Create Block file for persistence
        if os.path.isfile(block_dir(index)) is False:
            with open(block_dir(index), 'w+') as file:
                json.dump({'indexes': {}, 'data': []}, file)

    # Generates a hash based on the current state of the block
    @property
    def current_hash(self) -> str:
        block_string = BlockSchema().dumps(self)
        return sha256(block_string.encode()).hexdigest()

    # Add transactions into a block + index
    def add_transaction(self, tx: Transaction) -> None:
        with open(block_dir(self.index), 'r') as file:
            file_data = json.load(file)
            file_data['data'].append(TransactionSchema().dump(tx))

        with open(block_dir(self.index), 'w') as file:
            json.dump(file_data, file, indent=2)

        self.transactions.append(tx)
        index_new_data(self.index, len(self.transactions) - 1, tx.category)

    @property
    def get_size_of_block(self) -> int:
        return sys.getsizeof(self.transactions)
