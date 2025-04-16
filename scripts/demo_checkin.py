# scripts/demo_checkin.py
# Simulates a full check-in flow using placeholder data

from backend.models.customer import Customer
from backend.models.vehicle import Vehicle
from backend.models.insurance import InsurancePolicy
from backend.models.agreement import LoanerAgreement
from backend.db.session import SessionLocal
from datetime import datetime, timedelta


def create_demo_entry():
    db = SessionLocal()

    customer = Customer(
        full_name="Demo User",
        driver_license_number="D1234567",
        phone="555-123-4567",
        email="demo@demo.com"
    )

    vehicle = db.query(Vehicle).filter_by(vin="P7N04476").first()
    if not vehicle:
        vehicle = Vehicle(vin="P7N04476", make="BMW", model="330i", year=2024)
        db.add(vehicle)

    insurance = InsurancePolicy(
        provider="Progressive",
        policy_number="PRG123456",
        full_coverage=True,
        effective_date=datetime.today() - timedelta(days=30),
        expiration_date=datetime.today() + timedelta(days=335),
        vin="P7N04476"
    )

    agreement = LoanerAgreement(
        customer=customer,
        vehicle=vehicle,
        insurance=insurance,
        ro_number="282504",
        agreement_pdf_url="/generated_pdfs/agreement_demo.pdf",
        signature_image_url="/uploaded_files/signature_demo.png",
        check_out_time=datetime.now(),
        validator="demo_script"
    )

    db.add_all([customer, insurance, agreement])
    db.commit()
    db.close()
    print("✅ Demo check-in record created.")


if __name__ == '__main__':
    create_demo_entry()