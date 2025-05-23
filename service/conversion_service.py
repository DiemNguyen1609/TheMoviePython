from bson import ObjectId
from bson.decimal128 import Decimal128
import re

def convert_objectid_and_decimal(document):
    if '_id' in document:
        document['_id'] = str(document['_id'])
    for key, value in document.items():
        if isinstance(value, Decimal128):
            document[key] = float(value.to_decimal())
        elif isinstance(value, ObjectId):
            document[key] = str(value)
    return document

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def safe_int(value, default=0):
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        # Extract digits from the string
        digits = re.findall(r'\d+', value)
        if digits:
            return int(digits[0])
    return default

def safe_str(value):
    return value if isinstance(value, str) else ""