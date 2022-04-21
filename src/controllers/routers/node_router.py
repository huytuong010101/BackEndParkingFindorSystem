from fastapi import APIRouter, File, Form, UploadFile
from controllers.datadef.node import CreateNodeData
from controllers.datadef.record import CreateRecordData
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
async def read_all_nodes():
    nodes = NodeService.get_all_node()
    return list(nodes)


@node_router.post("/register", response_model=Node)
def register_new_node(data: CreateNodeData):
    return NodeService.create_node(data)


@node_router.post("/upload-image")
def upload_image(file: UploadFile):
    print(file.content_type)
    s3_client.upload_fileobj(
        file.file,
        "pbl5-vy",
        file.filename + str(datetime.now()),
        ExtraArgs={"ContentType": file.content_type},
    )
    return {"url": _get_object_url(file.filename)}


def _get_object_url(object_name: str) -> str:
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location["LocationConstraint"],
        "pbl5-vy",
        object_name,
    )


@node_router.post("/record", response_model=ParkRecord)
def create_new_record(
    file: UploadFile = File(...),
    park_id: int = Form(...),
    time: datetime = Form(...),
    num_of_empty_space: int = Form(...),
):
    s3_client.upload_fileobj(
        file.file,
        "pbl5-vy",
        file.filename + str(datetime.now()),
        ExtraArgs={"ContentType": file.content_type},
    )  
    record = RecordService.create_record(_get_object_url(file.filename), park_id, time, num_of_empty_space)
    return record
