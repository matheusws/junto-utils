import logging
from datetime import datetime

logging.root.setLevel(logging.INFO)

def logInfo(message):
    logging.info(f"[{datetime.now()}] {message}")

def logWarning(message):
    logging.warning(f"[{datetime.now()}] {message}")

def logError(message):
    logging.error(f"[{datetime.now()}] {message}")