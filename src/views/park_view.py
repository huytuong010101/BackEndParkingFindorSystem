import pydantic
from datetime import time
from typing import Optional
from .node_view import Node
from views.PeeweeGetterDict import PeeweeGetterDict

class Park(pydantic.BaseModel):
    id: int
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