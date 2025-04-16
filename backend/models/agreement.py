from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TireCondition(BaseModel):
    position: str  # 'front_left', 'front_right', etc.
    tread_depth_32nds: Optional[float] = None  # Optional - not required
    pressure_psi: Optional[int] = None         # Optional - not required
    damage_type: Optional[str] = None

class DamageAnnotation(BaseModel):
    zone: str  # e.g., 'left_rear_bumper'
    severity: str  # 'scratched', 'dented', etc.
    image_url: Optional[str] = None
    shared_with_customer: bool = False
    auto_detected: bool = False  # Flag for auto-detected damage from images

class LoanerAgreement(BaseModel):
    agreement_id: str                 # Tracks unique agreement ID
    customer_id: str                  # Links to customer record
    vehicle_id: str                   # Tracks VIN
    insurance_policy_id: Optional[str]  # Links insurance policy

    repair_order_number: str          # Tracks repair order (RO)
    check_out_time: datetime          # Timestamp of checkout
    expected_return_time: datetime    # Expected return
    actual_return_time: Optional[datetime] = None  # Timestamp when returned

    fuel_at_checkout_percent: Optional[int]         # Records fuel level at start
    mileage_at_checkout: Optional[int]              # Odometer out
    mileage_at_return: Optional[int]                # Odometer in

    condition_checkout_photos: Optional[List[str]] = []  # Links walkaround photo set
    condition_return_photos: Optional[List[str]] = []    # Return walkaround photo set

    tire_condition_checkout: Optional[List[TireCondition]] = []  # Optional fields
    tire_condition_return: Optional[List[TireCondition]] = []    # Optional fields

    checkout_damage_annotations: Optional[List[DamageAnnotation]] = []  # Includes auto-detect flag
    return_damage_annotations: Optional[List[DamageAnnotation]] = []

    media_shared_with_customer: Optional[List[str]] = []  # URLs of shared photos
    media_internal_only: Optional[List[str]] = []         # URLs for internal use only

    digital_signature_url: Optional[str] = None      # Stores digital signature URL
    agreement_pdf_url: Optional[str] = None          # Stores generated PDF URL
    validated_by: Optional[str] = None               # Tracks who signed off
    created_at: datetime = datetime.utcnow()         # Audit: creation time
    updated_at: Optional[datetime] = None            # Audit: last edit time
    notes: Optional[str] = None                      # Optional freeform notes

# Tracks VIN, RO, insurance ID, and timestamps
# Links walkaround photo sets
# Tracks per-tire condition, PSI, and damage
# Stores generated PDF and signature URLs
# Annotates walkaround damage with zones and severity
# Flags if damage annotations were auto-filled from photo analysis
# Allows auditing via validator and timestamp metadata
# Supports customer-facing media sharing
