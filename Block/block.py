import json
import sys
from hashlib import sha256

from Transaction import Transaction
from models import BlockSchema, TransactionSchema


def block_dir(x) -> str:
    return "data/{}.json".format(x)


class Block:
    def __init__(self, index: int, transactions: [], timestamp: float, previous_hash: str):
        self.index: int = index
        self.transactions: [] = transactions
        self.timestamp: float = timestamp
        self.previous_hash: str = previous_hash

        # Create Block file for persistence
        with open(block_dir(index), 'r+') as file:
            json.dump([], file)

    # Generates a hash based on the current state of the block
    @property
    def current_hash(self) -> str:
        block_string = BlockSchema().dumps(self)
        return sha256(block_string.encode()).hexdigest()

    def add_transaction(self, tx: Transaction) -> None:
        with open(block_dir(self.index), 'r') as file:
            file_data = json.load(file)
            file_data.append(TransactionSchema().dump(tx))

        with open(block_dir(self.index), 'w') as file:
            json.dump(file_data, file, indent=2)
            self.transactions.append(tx)

    @property
    def get_size_of_block(self) -> int:
        return sys.getsizeof(self.transactions)
