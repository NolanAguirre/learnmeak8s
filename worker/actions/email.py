import json


#TODO move these reusable schema functions into their own file
EMAIL_ACTION_SCHEMA = {
    "email": "email"
}

class TypeValidationError(Exception):
    pass

def is_str(value):
    return isinstance(value, str)

def is_email(value):
    return isinstance(value, str) and "@" in value and "." in value

TYPE_CHECKS = {
    "str": is_str,
    "email": is_email
}

def verify_payload(payload, schema):
    verification = {}
    for field, field_type in schema.items():
        value = payload.get(field)
        if value is None:
            raise TypeValidationError(f"Missing field: {field}")
        if field_type in TYPE_CHECKS:
            if TYPE_CHECKS[field_type](value):
                verification[field] = f"{field} is valid {field_type}"
            else:
                raise TypeValidationError(f"{field} is not a valid {field_type}: {value}")
        else:
            raise TypeValidationError(f"Unknown type {field_type} for {field}")
    return verification

def email_action(payload_json):
    if isinstance(payload_json, str):
        payload = json.loads(payload_json)
    else:
        payload = payload_json

    verification = verify_payload(payload, EMAIL_ACTION_SCHEMA)
    status = "completed"
    output_data = {"received": payload, "verification": verification}
    return (status, output_data)






