"""
Author: Christy Lee
LinkedIn: https://www.linkedin.com/in/christy-lee-798b53276/
GitHub Repository: https://github.com/christy511/Moderator-Program.git
"""

from datetime import datetime

def is_valid_name(name):
    """
    Check if the name is valid.
    - Contains only English characters (A-Z, a-z), space, and dash (-)
    - Is not empty or only spaces
    """
    if not isinstance(name, str) or name.strip() == "":
        return False
    for char in name:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -":
            return False
    return True

def is_chronological(earlier_dt, later_dt):
    """
    Check if later_dt is chronologically after earlier_dt.
    - Both inputs must be valid datetime strings in the format YYYY-MM-DDTHH:MM:SS
    """
    if not isinstance(earlier_dt, str) or not isinstance(later_dt, str):
        return False
    try:
        format = "%Y-%m-%dT%H:%M:%S"
        earlier = datetime.strptime(earlier_dt, format)
        later = datetime.strptime(later_dt, format)
        return later > earlier
    except ValueError:
        # This catches strings that don't match the datetime format
        return False

