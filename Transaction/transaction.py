from datetime import datetime


class Transaction:
    def __init__(self, sender: str, receiver: str, data: str, category: str = None, timestamp: datetime = None):
        self.sender = sender
        self.receiver = receiver
        self.data = data
        self.category = category
        self.timestamp = datetime.now() if timestamp is None else timestamp
