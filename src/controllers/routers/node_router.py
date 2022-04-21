from fastapi import APIRouter, UploadFile
from controllers.datadef.node import CreateNodeData
from views import Node
from typing import Dict, List
from controllers.services import s3_client, bucket_location, NodeService

node_router = APIRouter(
    prefix="/node",
    tags=["Node"],
)


@node_router.get("/", response_model=List[Node])
async def read_all_nodes():
    nodes = NodeService.get_all_node()
    return list(nodes)

@node_router.post("/register", response_model=Node)
def register_new_node(data: CreateNodeData):
    return NodeService.create_node(data)

@node_router.post("/upload-image")
def upload_image(file: UploadFile):
    print(file.content_type)
    s3_client.upload_fileobj(file.file, "pbl5-vy", file.filename, ExtraArgs={'ContentType': file.content_type})    
    return {"url": _get_object_url(file.filename)}


def _get_object_url(object_name: str) -> str:
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location["LocationConstraint"],
        "pbl5-vy",
        object_name,
    )