from fastapi import APIRouter
from controllers.services import FindorService
from views import ParkView, ParkRecord
from typing import List

findor_router = APIRouter(
    prefix="/findor",
    tags=["Findor"],
)

@findor_router.get("/park", response_model=List[ParkView])
async def get_park(name:str="", page:int = 1, num_per_page:int=20):
    parks = FindorService.get_park(name, page, num_per_page)
    return list(parks)

@findor_router.get("/:park_id", response_model=ParkView)
async def get_park(park_id: int):
    park = FindorService.get_park_by_id(park_id)
    return park

@findor_router.get("/:park_id/park-record", response_model=ParkRecord)
async def get_park(park_id: int):
    park = FindorService.find_park_record(park_id)
    return park

@findor_router.get("/search", response_model=List[ParkRecord])
async def seach_park_record(long:float, lat: float, min_empty_space=1, page:int = 1, num_per_page:int=20):
    parks = FindorService.find_park_available(long, lat, min_empty_space, page, num_per_page)
    return list(parks)
