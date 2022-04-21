from fastapi import APIRouter
from controllers.services import FindorService
from views import Park, ParkRecord
from typing import List

findor_router = APIRouter(
    prefix="/findor",
    tags=["Findor"],
)

@findor_router.get("/", response_model=List[Park])
async def get_park(page:int = 1, num_per_page:int=20):
    parks = FindorService.get_park(page, num_per_page)
    return list(parks)

@findor_router.get("/search", response_model=List[ParkRecord])
async def seach_park(long:float, lat: float, min_empty_space=1, page:int = 1, num_per_page:int=20):
    parks = FindorService.find_park(long, lat, min_empty_space, page, num_per_page)
    return list(parks)