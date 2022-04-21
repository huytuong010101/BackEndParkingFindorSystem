from models.park_model import Park
from models.park_record_model import ParkRecord
from peewee import fn

class FindorService:
    @staticmethod
    def get_park(page, num_per_page):
        return Park.select().paginate(page, num_per_page)
    
    @staticmethod
    def find_park(long: float, lat: float, min_empty_space, page, num_per_page):
        results = list(
            ParkRecord.select()
            .where(ParkRecord.num_of_empty_space >= min_empty_space)
            .order_by(ParkRecord.time)
            .group_by(ParkRecord.park)
            .paginate(page, num_per_page)
        )
        results.sort(key=lambda item: abs(long - item.park.long) + abs(lat - item.park.lat))
        return results
        