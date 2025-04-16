from pydantic import BaseModel
from typing import Optional
from datetime import date

class Vehicle(BaseModel):
    vin: str
    make: str
    model: str
    year: int
    license_plate: Optional[str] = None
    current_mileage: Optional[int] = None
    fuel_level_percent: Optional[int] = None

    available: bool = True
    lot_location: Optional[str] = None
    telematics_enabled: bool = False
    last_checkin_date: Optional[date] = None
    notes: Optional[str] = None