from unicodedata import name
from controllers.datadef.node import CreateNodeData
from models import Node


class NodeService:
    @staticmethod
    def get_all_node():
        return Node.select()

    @staticmethod
    def create_node(data: CreateNodeData) -> Node:
        node = Node.create(
            node_name=data.node_name,
            address=data.address,
            token=data.token,
            long=data.long,
            lat=data.lat,
        )

        return node
