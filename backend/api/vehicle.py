from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

VEHICLES_DB = {}

router = APIRouter()

class VehicleIn(BaseModel):
    vin: str
    make: str
    model: str
    year: int
    mileage: Optional[int] = 0
    in_service_date: Optional[str]
    subsidy_eligible: bool = True

class VehicleOut(VehicleIn):
    id: str

@router.post("/create", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleIn):
    vehicle_id = str(uuid4())
    VEHICLES_DB[vehicle_id] = vehicle.dict()
    return {"id": vehicle_id, **vehicle.dict()}

@router.get("/{vehicle_id}", response_model=VehicleOut)
def get_vehicle(vehicle_id: str):
    if vehicle_id not in VEHICLES_DB:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"id": vehicle_id, **VEHICLES_DB[vehicle_id]}

@router.get("/fleet", response_model=List[VehicleOut])
def list_fleet():
    return [
        {"id": vid, **v} for vid, v in VEHICLES_DB.items()
    ]