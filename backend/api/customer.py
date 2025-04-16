from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Placeholder database
CUSTOMERS_DB = {}

router = APIRouter()

class CustomerIn(BaseModel):
    name: str
    license_number: str
    phone: Optional[str] = None
    insurance_company: Optional[str] = None
    policy_number: Optional[str] = None

class CustomerOut(CustomerIn):
    id: str

@router.post("/create", response_model=CustomerOut)
def create_customer(customer: CustomerIn):
    import uuid
    customer_id = str(uuid.uuid4())
    customer_data = customer.dict()
    CUSTOMERS_DB[customer_id] = customer_data
    return {"id": customer_id, **customer_data}

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: str):
    if customer_id not in CUSTOMERS_DB:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"id": customer_id, **CUSTOMERS_DB[customer_id]}
