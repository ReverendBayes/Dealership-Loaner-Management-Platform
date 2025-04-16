# scripts/test_ocr_flow.py
# Manual test for OCR engine against a sample insurance card

from backend.services.ocr_engine import extract_text_from_image
from backend.utils.date_parser import extract_date_range

sample_path = "./tests/sample_insurance_card.png"  # Replace with your actual path

if __name__ == '__main__':
    print("🧪 Testing OCR on:", sample_path)
    text = extract_text_from_image(sample_path)
    print("--- Extracted Text ---")
    print(text)

    start_date, end_date = extract_date_range(text)
    print("\n--- Parsed Coverage Dates ---")
    print("Effective:", start_date)
    print("Expires:", end_date)
