import os
from datetime import datetime

def get_timestamp():
    """Returns a string of the current date and time."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def ensure_folder_exists(path):
    """Creates the given folder if it does not already exist."""
    if not os.path.exists(path):
        os.makedirs(path)