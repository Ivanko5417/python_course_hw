import logging
from datetime import datetime
from urllib.parse import urlparse


def configure_logger(ulr):
    site_name = urlparse(ulr).netloc
    filename = f"{datetime.now().isoformat()}_{site_name}.log"
    logging.basicConfig(filename=filename, level=logging.DEBUG)
    logging.info("Logger successfully configured")
