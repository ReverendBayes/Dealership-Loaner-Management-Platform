# scripts/seed_vehicles.py
# Pre-populate the vehicle table with sample fleet entries

from backend.db.session import SessionLocal
from backend.models.vehicle import Vehicle

vehicles = [
    Vehicle(vin="P7N04476", make="BMW", model="330i", year=2024, license_plate="X12ABC", current_mileage=1500),
    Vehicle(vin="PCN69371", make="BMW", model="X3", year=2023, license_plate="Y34DEF", current_mileage=2200),
    Vehicle(vin="R9U10991", make="BMW", model="530e", year=2022, license_plate="Z56GHI", current_mileage=3100),
]

def seed():
    db = SessionLocal()
    for v in vehicles:
        existing = db.query(Vehicle).filter_by(vin=v.vin).first()
        if not existing:
            db.add(v)
    db.commit()
    db.close()

if __name__ == '__main__':
    seed()
    print("✅ Vehicle seed complete.")