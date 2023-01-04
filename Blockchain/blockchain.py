import sys
from time import time

from Block import Block
from Transaction import Transaction

# The size is in bytes (1MB)
MAX_BLOCK_SIZE = pow(2, 20)


class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []

    # Returns the last block
    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    # Returns the size of the chain
    @property
    def chain_length(self) -> int:
        return len(self.chain)

    # Genesis Block Creation
    def create_genesis_block(self) -> None:
        genesis_block = Block(0, [], time(), "0")
        self.chain.append(genesis_block)

    # Adds a block
    def add_block(self) -> None:
        block = Block(self.chain_length, [], time(), self.last_block.current_hash)
        self.chain.append(block)

    # Method that adds a transaction to the latest block of the chain
    def add_transaction(self, tx: Transaction) -> None:
        size = self.last_block.get_size_of_block

        if size + sys.getsizeof(tx) > MAX_BLOCK_SIZE:
            self.add_block()

        self.last_block.transactions.append(tx)
