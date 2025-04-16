# utils/date_parser.py
# Extract and normalize date formats from noisy OCR text

import re
from datetime import datetime
from typing import Optional

def extract_dates(text: str) -> list:
    """
    Return list of detected date strings from text.
    Matches MM/DD/YYYY, MM-DD-YYYY, YYYY-MM-DD, etc.
    """
    pattern = r'(\d{2}[\/\-]\d{2}[\/\-]\d{4}|\d{4}[\/\-]\d{2}[\/\-]\d{2})'
    return re.findall(pattern, text)

def parse_date(date_str: str) -> Optional[datetime]:
    """
    Attempt to parse a date string to datetime object.
    """
    date_str = date_str.replace('-', '/').strip()
    formats = ["%m/%d/%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def extract_date_range(text: str) -> tuple[Optional[datetime], Optional[datetime]]:
    """
    Attempt to return (start_date, end_date) from OCR text.
    """
    raw_dates = extract_dates(text)
    parsed_dates = [parse_date(d) for d in raw_dates if parse_date(d)]
    if len(parsed_dates) >= 2:
        return tuple(sorted(parsed_dates[:2]))
    return (None, None)