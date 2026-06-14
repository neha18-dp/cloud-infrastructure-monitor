import logging
from pathlib import Path


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # Ensure logs directory exists
    Path("logs").mkdir(exist_ok=True)

    logger = logging.getLogger("cloud_monitor")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        "logs/monitor.log",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger