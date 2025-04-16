from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ocr_engine import extract_text_from_image
from services.validation import validate_insurance_text

router = APIRouter()

@router.post("/verify")
async def verify_insurance(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Use JPG or PNG.")

    # Extract text from image
    ocr_text = await extract_text_from_image(file)
    if not ocr_text:
        raise HTTPException(status_code=422, detail="Could not extract text from image.")

    # Validate insurance content
    result = validate_insurance_text(ocr_text)

    return {
        "raw_text": ocr_text,
        "validation": result
    }