from models.park_model import Park
from models.park_record_model import ParkRecord
from peewee import fn, SQL
import geopy.distance


class FindorService:
    @staticmethod
    def get_park(name, page, num_per_page):
        return Park.select().where(Park.park_name.contains(name)).paginate(page, num_per_page)

    @staticmethod
    def find_park_available(long: float, lat: float, min_empty_space: int, page: int, num_per_page: int):
        results = list(
            ParkRecord.select(ParkRecord, Park, (fn.ABS((Park.long - long)) + fn.ABS((Park.lat - lat))).alias("distance"))
            .where(ParkRecord.num_of_empty_space >= min_empty_space)
            .join(Park)
            .order_by(SQL("distance"))
            .group_by(ParkRecord.park)
            .having(ParkRecord.time == fn.MAX(ParkRecord.time))
            .paginate(page, num_per_page)
        )
        for result in results:
            result.distance = geopy.distance.distance((lat, long), (result.park.lat, result.park.long)).km
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
        
