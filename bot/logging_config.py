from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

logger.add(
    "logs/trading_bot.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger