import pydantic
from datetime import datetime
from typing import Optional
from .node_view import Node
from .park_view import ParkView
from views.PeeweeGetterDict import PeeweeGetterDict


class ParkRecord(pydantic.BaseModel):
    id: int
    park: ParkView
    time: datetime
    image: str
    num_of_empty_space: int
    distance: Optional[float] = None
    

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
