from datetime import datetime

from models.park_record_model import ParkRecord


class RecordService:
    @staticmethod
    def create_record(
        image: str, park_id: int, time: datetime, num_of_empty_space: int
    ) -> ParkRecord:
        ParkRecord.delete().where(park=park_id)
        record = ParkRecord.create(
            image=image, park=park_id, time=time, num_of_empty_space=num_of_empty_space
        )
        return record
