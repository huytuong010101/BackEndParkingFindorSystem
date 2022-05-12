import pydantic
from datetime import time
from datetime import datetime
from typing import Optional
from .node_view import Node
from views.PeeweeGetterDict import PeeweeGetterDict


class ParkBase(pydantic.BaseModel):
    park_name: str
    address: Optional[str] = None
    long: Optional[float] = None
    lat: Optional[float] = None
    open_close: Optional[time] = None
    close_time: Optional[time] = None
    node: Node

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        
class ParkView(ParkBase):
    id: int
    disable_at: Optional[datetime]
    
class ParkCreate(ParkBase):
    park_name: str
    address: Optional[str]
    long: Optional[float]
    lat: Optional[float]
    open_close: Optional[time]
    close_time: Optional[time]
    node: int
    
class ParkUpdate(ParkBase):
    park_name: Optional[str]
    address: Optional[str]
    long: Optional[float]
    lat: Optional[float]
    open_close: Optional[time]
    close_time: Optional[time]
    node: Optional[int]