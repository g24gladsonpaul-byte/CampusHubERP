
import logging
from pathlib import Path


# Create logs folder in the project root
BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Log file location
LOG_FILE = LOG_DIR / "application.log"

# Configure application logger
logger = logging.getLogger("CampusHubERP")
logger.setLevel(logging.INFO)

# Prevent duplicate log handlers
if not logger.handlers:

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
