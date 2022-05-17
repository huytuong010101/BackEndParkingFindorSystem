from datetime import datetime
import pydantic
from typing import Optional
from views.PeeweeGetterDict import PeeweeGetterDict


class Node(pydantic.BaseModel):
    id: int
    node_name: str
    address: Optional[str] = None
    token: Optional[str] = None
    long: Optional[float] = None
    lat: Optional[float] = None
    disable_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
