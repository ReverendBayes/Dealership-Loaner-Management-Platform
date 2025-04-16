from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

AGREEMENTS_DB = {}

router = APIRouter()

class AgreementIn(BaseModel):
    customer_id: str
    vehicle_id: str
    ro_number: Optional[str]
    check_out_time: Optional[datetime] = None
    signature_data: Optional[str]  # Base64 or vector data
    insurance_verified: bool = False

class AgreementOut(AgreementIn):
    id: str
    created_at: datetime

@router.post("/create", response_model=AgreementOut)
def create_agreement(data: AgreementIn):
    agreement_id = str(uuid4())
    now = datetime.utcnow()
    AGREEMENTS_DB[agreement_id] = {
        **data.dict(),
        "created_at": now
    }
    return {"id": agreement_id, "created_at": now, **data.dict()}

@router.get("/{agreement_id}", response_model=AgreementOut)
def get_agreement(agreement_id: str):
    if agreement_id not in AGREEMENTS_DB:
        raise HTTPException(status_code=404, detail="Agreement not found")
    return {"id": agreement_id, **AGREEMENTS_DB[agreement_id]}

@router.get("/customer/{customer_id}", response_model=List[AgreementOut])
def list_customer_agreements(customer_id: str):
    return [
        {"id": aid, **a}
        for aid, a in AGREEMENTS_DB.items()
        if a["customer_id"] == customer_id
    ]
