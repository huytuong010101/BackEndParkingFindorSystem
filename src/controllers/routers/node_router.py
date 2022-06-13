from fastapi import APIRouter, Depends, File, Form, UploadFile, status, HTTPException
from controllers.datadef.node import CreateNodeData, UpdateNodeData
from controllers.datadef.record import CreateRecordData
from controllers.routers.auth_router import auth_login
from controllers.services.park_service import ParkService
from controllers.services.record_service import RecordService
from views import Node
from typing import Dict, List
from controllers.services import s3_client, bucket_location, NodeService
from datetime import datetime

from views.park_record_view import ParkRecord

node_router = APIRouter(
    prefix="/node",
    tags=["Node"],
)


@node_router.get("/", response_model=List[Node])
async def read_all_nodes(page: int = 1, num_per_page: int = 20):
    nodes = NodeService.get_all_node(page, num_per_page)
    return list(nodes)


@node_router.get("/{node_id}", response_model=Node)
async def get_node(node_id: int):
    node = NodeService.get_node_by_id(node_id)
    return node

@node_router.post("/", response_model=Node)
def register_new_node(data: CreateNodeData, auth_login = Depends(auth_login)):
    return NodeService.create_node(data)

@node_router.put("/{id}")
def update_node(id: int, data: UpdateNodeData, auth_login = Depends(auth_login)):
    NodeService.update_node(id, data)

@node_router.delete("/{id}")
def delete_node(id: int, auth_login = Depends(auth_login)):
    NodeService.delete_node(id)

def _get_object_url(object_name: str) -> str:
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location["LocationConstraint"],
        "pbl5-vy",
        object_name,
    )


# @node_router.post("/record", response_model=ParkRecord)
@node_router.post("/record")
def create_new_record(
    file: UploadFile = File(...),
    park_id: int = Form(...),
    time: datetime = Form(...),
    num_of_empty_space: int = Form(...),
    token: str =  Form(...),
):
    park = ParkService.get_park_by_id(park_id)
    if park.node.token != token:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Token is not valid") 

    file_name = file.filename + str(datetime.now())
    s3_client.upload_fileobj(
        file.file,
        "pbl5-vy",
        file_name,
        ExtraArgs={"ContentType": file.content_type},
    )
    record = RecordService.create_record(_get_object_url(
        file_name), park_id, time, num_of_empty_space)
    return record
