
def validate_customer(customer_id, customer_name, age):

    # Validate Customer ID
    if not isinstance(customer_id, int) or isinstance(customer_id, bool):
        return "Invalid"

    if customer_id <= 0:
        return "Invalid"

    # Validate Customer Name
    if not isinstance(customer_name, str):
        return "Invalid"

    if not customer_name.strip() or customer_name.strip().lower() == "empty":
        return "Invalid"

    # Validate Customer Age
    if not isinstance(age, int) or isinstance(age, bool):
        return "Invalid"

    if age < 0:
        return "Invalid"

    return "Valid"
