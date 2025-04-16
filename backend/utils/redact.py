# utils/redact.py
# Stub for future PII redaction using spaCy or Microsoft Presidio

from typing import List
import re

# Very basic placeholder implementation
# Replace phone numbers and policy numbers with '[REDACTED]'

def simple_redact(text: str) -> str:
    text = re.sub(r'\b\d{3}[-.\s]?\d{2,3}[-.\s]?\d{4}\b', '[REDACTED_PHONE]', text)
    text = re.sub(r'policy\s?#?:?\s?\w{6,}', '[REDACTED_POLICY]', text, flags=re.IGNORECASE)
    return text

# Future: integrate Presidio or spaCy for names, addresses, license numbers

def placeholder_redact_entities(text: str) -> List[str]:
    return ["REDACT_NAME", "REDACT_PHONE", "REDACT_DOB"]
