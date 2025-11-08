import logging
from utils.helpers import get_timestamp
import os

def setup_logger(log_folder="logs"):
    """Creates the logs folder (if needed) and configures the logger."""
    from utils.helpers import ensure_folder_exists
    ensure_folder_exists(log_folder)

    log_file = os.path.join(log_folder, f"logs_{get_timestamp()}.txt")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logger initialized.")

def log_info(msg):
    """Logs an info-level message."""
    logging.info(msg)

def log_error(msg):
    """Logs an error-level message."""
    logging.error(msg)