def initiate_payment(phone_number, amount):
    """Simulate a PayHero payment initiation."""
    return {
        "status": "success",
        "message": f"Payment of {amount} to {phone_number} initiated."
    }
