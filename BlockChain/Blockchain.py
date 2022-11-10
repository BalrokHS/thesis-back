from time import time
from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []

    # Genesis Block Creation
    def create_genesis_block(self) -> None:
        genesis_block = Block(0, [], time(), "0")
        genesis_block.hash = genesis_block.current_hash()
        self.chain.append(genesis_block)

    # Adds a block
    def add_block(self) -> None:
        block = Block(self.chain_length, [], time(), self.last_block.current_hash())
        self.chain.append(block)

    # Returns the size of the chain
    @property
    def chain_length(self) -> int:
        return len(self.chain)

    # Returns the last block
    @property
    def last_block(self) -> Block:
        return self.chain[-1]
