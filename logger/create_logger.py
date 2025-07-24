import os
import logging

from logging.handlers import TimedRotatingFileHandler

from configs import configs


LOGS_DIR = os.path.join("./", configs.LOGS_FOLDER)
os.makedirs(LOGS_DIR, exist_ok=True)
LOGS_FILENAME = 'ai'
LOGS_FORMATTER = "%(asctime)s - %(levelname)s - %(message)s"
LOGS_NAME = 'ai_logger'
handler = TimedRotatingFileHandler(os.path.join(LOGS_DIR, LOGS_FILENAME + '.log'), 
                                when="midnight", 
                                interval=1, 
                                backupCount=30,
                                encoding="utf-8")
handler.setFormatter(logging.Formatter(LOGS_FORMATTER))

logger = logging.getLogger(LOGS_NAME)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
