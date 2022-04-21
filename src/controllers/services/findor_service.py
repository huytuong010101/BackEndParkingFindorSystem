from models.park_model import Park
from models.park_record_model import ParkRecord
from peewee import fn
import math


class FindorService:
    @staticmethod
    def get_park(page, num_per_page):
        return Park.select().paginate(page, num_per_page)

    @staticmethod
    def find_park_available(long: float, lat: float, min_empty_space, page, num_per_page):
        results = list(
            ParkRecord.select()
            .where(ParkRecord.num_of_empty_space >= min_empty_space)
            .order_by(ParkRecord.time)
            .group_by(ParkRecord.park)
            .paginate(page, num_per_page)
        )
        for result in results:
            result.distance = math.sqrt((long - result.park.long)**2 + (lat - result.park.lat)**2)
        results.sort(key=lambda item: item.distance)
        return results
    
    @staticmethod
    def get_park_by_id(park_id: int):
        return Park.get(park_id)
    
    @staticmethod
    def find_park_record(park_id: int):
        result = (
            ParkRecord.select()
            .where(ParkRecord.park == park_id)
            .order_by(ParkRecord.time.desc())
            .first()
        )
        return result
        
