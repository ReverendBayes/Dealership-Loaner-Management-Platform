from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class Customer(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    driver_license_number: Optional[str] = None
    driver_license_state: Optional[str] = None
    license_expiration_date: Optional[date] = None
    driver_license_image_url: Optional[str] = None
    insurance_card_image_url: Optional[str] = None

    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None

    previous_repair_orders: Optional[List[str]] = []  # RO numbers linked to this customer
    previous_loaner_agreements: Optional[List[str]] = []  # Agreement IDs
    linked_vehicles: Optional[List[str]] = []  # VINs the customer has been associated with

    notes: Optional[str] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None