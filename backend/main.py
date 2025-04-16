from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import insurance, agreement, customer, vehicle

app = FastAPI(
    title="Dealership Loaner Management Platform",
    description="Backend API for managing check-ins, insurance verification, agreements, and fleet activity",
    version="1.0.0"
)

# CORS setup for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider limiting in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(insurance.router, prefix="/api/insurance", tags=["Insurance"])
app.include_router(agreement.router, prefix="/api/agreements", tags=["Agreements"])
app.include_router(customer.router, prefix="/api/customers", tags=["Customers"])
app.include_router(vehicle.router, prefix="/api/vehicles", tags=["Vehicles"])

# Health check
@app.get("/ping")
def ping():
    return {"status": "ok"}
