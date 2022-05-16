import datetime
from uuid import uuid4


class AnimalIdentifier:
    def __init__(self, uuid: str, timestamp: datetime.datetime):
        self.uuid: str = uuid
        self.timestamp: datetime.datetime = timestamp

    @classmethod
    def generate(cls) -> 'AnimalIdentifier':
        uuid = uuid4().hex
        timestamp = datetime.datetime.utcnow()
        return cls(uuid=uuid, timestamp=timestamp)

    def __str__(self):
        timestamp_formatted = self.timestamp.strftime('%Y%m%d_%H%M%S')
        return f"{timestamp_formatted}_{self.uuid}"