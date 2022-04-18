from fastapi import APIRouter
from controllers.services import NodeService
from views import Node
from typing import List

node_router = APIRouter(
    prefix="/node",
    tags=["Node"],
)

@node_router.get("/", response_model=List[Node])
async def read_all_nodes():
    nodes = NodeService.get_all_node()
    return list(nodes)