# config.py
# Centralized application configuration loader

import os
from dotenv import load_dotenv

# Load .env file values into environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dealership.db")
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
PDF_OUTPUT_DIR = os.getenv("PDF_OUTPUT_DIR", "generated_pdfs")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploaded_files")
OCR_ENGINE = os.getenv("OCR_ENGINE", "tesseract")

# Optional keys for integration if enabled
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AWS_TEXTRACT_KEY = os.getenv("AWS_TEXTRACT_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")