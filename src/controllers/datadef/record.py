from datetime import datetime
from pydantic import BaseModel


class CreateRecordData(BaseModel):
    park_id: int
    time: datetime
    num_of_empty_space: int

    class Config:
        orm_mode = True
