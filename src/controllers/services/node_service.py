from datetime import datetime
from unicodedata import name
from controllers.datadef.node import CreateNodeData, UpdateNodeData
from models import Node
import uuid

class NodeService:
    @staticmethod
    def get_all_node(page, num_per_page):
        return Node.select().where(Node.disable_at == None).paginate(page, num_per_page)

    @staticmethod
    def create_node(data: CreateNodeData) -> Node:
        node = Node.create(
            node_name=data.node_name,
            address=data.address,
            token=str(uuid.uuid4()),
            long=data.long,
            lat=data.lat,
        )

        return node
    
    @staticmethod
    def get_node_by_id(node_id: int):
        return Node.get(node_id)
    
    @staticmethod
    def update_node(id: int, data: UpdateNodeData) -> Node:
        data = data.dict()
        # remove None field
        data = {k: v for k, v in data.items() if v}
        return Node.update(**data).where(Node.id == id).execute()

    @staticmethod
    def delete_node(id: int):
        Node.update(disable_at = datetime.now()).where(Node.id == id).execute()