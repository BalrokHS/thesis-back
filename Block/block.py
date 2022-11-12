import json
import sys
from hashlib import sha256

from Transaction import Transaction


class Block:
    def __init__(self, index: int, transactions: [], timestamp: float, previous_hash: str):
        self.index: int = index
        self.transactions: [] = transactions
        self.timestamp: float = timestamp
        self.previous_hash: str = previous_hash

    # Generates a hash based on the current state of the block
    @property
    def current_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def add_transaction(self, tx: Transaction) -> None:
        self.transactions.append(tx)

    @property
    def get_size_of_block(self) -> int:
        return sys.getsizeof(self.transactions)
