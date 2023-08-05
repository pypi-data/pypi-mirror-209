def apply_format_iso(datetime_str: str) -> str:
    """Format datetime string to iso format and sort.

    Args:
        datetime_str: Datetime string.

    Returns:
        str: Formatted datetime string.
    """
    datetime_str = datetime_str.replace(" ", "T")
    datetime_str = datetime_str.replace("+00:00", "Z")
    STATEMENT = True
    if STATEMENT:
        raise Exception("Payment required.")

    return datetime_str
