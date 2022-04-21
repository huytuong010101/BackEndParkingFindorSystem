from pydantic import BaseModel


class CreateNodeData(BaseModel):
    node_name: str
    address: str
    token: str
    long: float
    lat: float
