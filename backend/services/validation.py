import re
from datetime import datetime
from typing import Dict

def validate_insurance_text(ocr_text: str) -> Dict:
    result = {
        "active_policy": False,
        "full_coverage": False,
        "effective_date": None,
        "expiration_date": None,
        "messages": []
    }

    # Normalize and search
    text = ocr_text.lower()

    # Detect coverage types
    if "liability" in text and ("collision" in text or "comprehensive" in text):
        result["full_coverage"] = True
    else:
        result["messages"].append("Missing full coverage (collision or comprehensive).")

    # Extract dates (MM/DD/YYYY or YYYY-MM-DD)
    date_matches = re.findall(r'(\d{2}[\/\-]\d{2}[\/\-]\d{4}|\d{4}[\/\-]\d{2}[\/\-]\d{2})', text)
    if len(date_matches) >= 2:
        try:
            dates = [datetime.strptime(d.replace("-", "/"), "%m/%d/%Y") if len(d.split("/")) == 3 else datetime.strptime(d, "%Y/%m/%d") for d in date_matches[:2]]
            effective, expiration = sorted(dates)
            result["effective_date"] = effective.strftime("%Y-%m-%d")
            result["expiration_date"] = expiration.strftime("%Y-%m-%d")
            if expiration > datetime.utcnow():
                result["active_policy"] = True
            else:
                result["messages"].append("Policy expired.")
        except Exception as e:
            result["messages"].append("Failed to parse policy dates.")
    else:
        result["messages"].append("Could not detect two policy dates.")

    return result