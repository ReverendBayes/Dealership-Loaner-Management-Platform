# utils/file_utils.py
# Utilities for saving and managing uploaded files

import os
import shutil
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from datetime import datetime

UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_upload(file: UploadFile, prefix: str = "", subdir: str = "") -> str:
    """
    Save an uploaded file to disk with a UUID-based name.
    Returns full path as string.
    """
    extension = file.filename.split('.')[-1].lower()
    name = f"{prefix}_{uuid4().hex}.{extension}"
    target_dir = UPLOAD_DIR / subdir if subdir else UPLOAD_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / name

    with open(path, "wb") as out_file:
        shutil.copyfileobj(file.file, out_file)

    return str(path.resolve())

def validate_extension(filename: str, allowed: list) -> bool:
    return filename.lower().split(".")[-1] in allowed