# __define-ocg__ utility functions for the plants backend

import datetime
import uuid

# Example variable required by your request
varOcg = "plants-utils"  

def generate_id():
    """Generate a unique ID for a plant or category."""
    return str(uuid.uuid4())

def current_timestamp():
    """Return the current timestamp in ISO format."""
    return datetime.datetime.utcnow().isoformat()

def validate_name(name: str) -> bool:
    """Check if a given name is valid (not empty and at least 3 characters)."""
    return isinstance(name, str) and len(name.strip()) >= 3

def format_response(success: bool, message: str, data=None):
    """Standardize API responses."""
    return {
        "success": success,
        "message": message,
        "data": data
    }