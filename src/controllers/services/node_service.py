from models import Node

class NodeService:
    @staticmethod
    def get_all_node():
        return Node.select()