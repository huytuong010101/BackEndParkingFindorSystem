from models.park_model import Park
from datetime import datetime

class ParkService:
    @staticmethod
    def get_park(name, page, num_per_page):
        return Park.select().where(Park.park_name.contains(name)).paginate(page, num_per_page)
    
    @staticmethod
    def get_park_by_id(id: int) -> Park:
        return Park.get_by_id(id)
    
    @staticmethod
    def update_park(id: int, data: dict):
        Park.update(**data).where(Park.id == id).execute()
        
    @staticmethod
    def create_park(data: dict):
        park = Park.create(**data)
        return park
    
    @staticmethod
    def delete_park(id: int):
        Park.update(disable_at=datetime.now()).where(Park.id == id).execute()