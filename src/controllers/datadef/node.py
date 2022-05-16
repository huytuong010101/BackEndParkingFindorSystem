from typing import Optional
from pydantic import BaseModel
    
class CreateNodeData(BaseModel):
    node_name: str
    address: str
    token: str
    long: float
    lat: float

class UpdateNodeData(BaseModel):
    node_name: Optional[str] = None
    address: Optional[str] = None
    long: Optional[float] = None
    lat: Optional[float] = None