import pytesseract
from PIL import Image
from fastapi import UploadFile
import tempfile
import shutil

async def extract_text_from_image(file: UploadFile) -> str:
    # Save uploaded file to a temporary location
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Open and OCR the image
        image = Image.open(tmp_path)
        text = pytesseract.image_to_string(image)
        return text.strip()

    except Exception as e:
        print(f"OCR error: {e}")
        return ""

    finally:
        file.file.close()
