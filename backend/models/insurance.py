from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

class Coverage(BaseModel):
    code: str
    label: str
    limit_per_accident: Optional[float] = None
    limit_per_person: Optional[float] = None
    deductible: Optional[float] = None
    applies_to_rental: Optional[bool] = False

class InsuredPerson(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    license_number: Optional[str] = None
    license_state: Optional[str] = None
    is_primary: bool = True

class InsurancePolicy(BaseModel):
    policy_number: str
    carrier: str
    status: str = "active"
    effective_date: date
    expiration_date: date
    full_coverage: bool
    rental_vehicle_coverage: bool = False
    vin_match: bool = False
    premium: Optional[float] = None
    address: Optional[str] = None

    insureds: List[InsuredPerson]
    coverages: List[Coverage]
    term: Optional[str] = None
    documents: Optional[List[str]] = []
    validated: bool = False
    validation_notes: Optional[List[str]] = []