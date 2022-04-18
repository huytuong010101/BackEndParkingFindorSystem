from models.park_model import Park

class FindorService:
    @staticmethod
    def get_park():
        return Park.select()