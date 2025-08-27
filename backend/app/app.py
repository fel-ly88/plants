from utils import generate_id, current_timestamp, validate_name, format_response


new_id = generate_id()
print("Generated ID:", new_id)

print("Timestamp:", current_timestamp())
print("Valid name?", validate_name("Rose"))
