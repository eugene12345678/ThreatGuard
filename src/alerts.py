def alert_admin(log_entry):
    """Alert the admin of a detected threat."""
    print(f"Threat detected! Log entry: {log_entry.to_dict()}")
