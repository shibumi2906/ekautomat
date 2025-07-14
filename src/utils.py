from loguru import logger
from pathlib import Path

# создаём папку логов, если нет
LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# файл логов
logger.add(LOG_DIR / "app.log", rotation="500 KB", retention="10 days", level="DEBUG")

__all__ = ["logger"]
