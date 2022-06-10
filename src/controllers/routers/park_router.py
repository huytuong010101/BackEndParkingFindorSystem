from fastapi import APIRouter, Depends, HTTPException, status
from controllers.routers.auth_router import auth_login
from controllers.services import ParkService
from views import ParkView, ParkUpdate, ParkCreate
from typing import List

park_router = APIRouter(
    prefix="/park",
    tags=["Park"],
)

@park_router.get("/", response_model=List[ParkView])
async def get_park(name:str="", page:int = 1, num_per_page:int=20):
    parks = ParkService.get_park(name, page, num_per_page)
    return list(parks)

@park_router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_park(id: int, data: ParkUpdate, auth_login = Depends(auth_login)):
    try:
        ParkService.update_park(id, data.dict(exclude_none=True))
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE) 
    
@park_router.post("/", response_model=ParkView)
async def create_park(data: ParkCreate, auth_login = Depends(auth_login)):
    try:
        return ParkService.create_park(data.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE) 
    
@park_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_park(id: int, auth_login = Depends(auth_login)):
    try:
        return ParkService.delete_park(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE) 

