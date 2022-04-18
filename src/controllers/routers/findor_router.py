from fastapi import APIRouter
from controllers.services import FindorService
from views import Park
from typing import List

findor_router = APIRouter(
    prefix="/findor",
    tags=["Findor"],
)

@findor_router.get("/", response_model=List[Park])
async def get_park():
    parks = FindorService.get_park()
    return list(parks)

@findor_router.get("/search")
async def seach_park():
    return None