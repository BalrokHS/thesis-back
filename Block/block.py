import json
from hashlib import sha256


class Block:
    def __init__(self, index: int, transactions: list, timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    # Generates a hash based on the current state of the block
    def current_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

