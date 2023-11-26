import datetime
from datetime import timedelta, timezone

def get_current_date_time() -> datetime.datetime:
    """
    Returns the current date and time in UTC timezone.

    Returns:
        datetime.datetime: A datetime object representing the current date and time in UTC timezone.
    """
    return datetime.datetime.now(timezone.utc)