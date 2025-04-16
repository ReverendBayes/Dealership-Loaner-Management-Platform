import os
from pathlib import Path
from fastapi import UploadFile
import shutil
from datetime import datetime

WALKAROUND_DIR = Path("walkaround_photos")
WALKAROUND_DIR.mkdir(parents=True, exist_ok=True)

def save_walkaround_image(file: UploadFile, vehicle_id: str, inspection_type: str = "checkout") -> str:
    """
    Save walkaround image to the filesystem.
    inspection_type: "checkout" or "return"
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{vehicle_id}_{inspection_type}_{timestamp}.jpg"
    output_path = WALKAROUND_DIR / filename

    with open(output_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(output_path)


def list_walkaround_images(vehicle_id: str) -> list:
    """
    List all stored images for a given vehicle.
    """
    return [
        str(p) for p in WALKAROUND_DIR.glob(f"{vehicle_id}_*.jpg")
    ]