from pydantic import BaseModel
from typing import Optional
from datetime import date

class LoanerSubsidy(BaseModel):
    vehicle_id: str
    brand: str  # e.g., "BMW"
    loan_date: date
    return_date: Optional[date]
    customer_name: str
    repair_order_number: str

    subsidy_type: Optional[str] = "OEM"
    subsidy_amount: Optional[float] = 0.0
    subsidy_reason: Optional[str] = None
    submitted_to_oem: bool = False
    reimbursed: bool = False
    notes: Optional[str] = None