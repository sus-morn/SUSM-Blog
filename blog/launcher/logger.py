import os
import sys
import logging
import logging.handlers
from loguru import logger

from pathlib import Path

log_path: Path = Path(__file__).parent / "log" / "launcher.log"

if not os.path.exists(log_path.parent):
    os.mkdir(log_path.parent)
if not os.path.exists(log_path):
    f = open(log_path, "x", encoding="utf-8")
    f.close()

default_format: str = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    # "<c>{function}:{line}</c>| "
    "{message}"
)

logger.remove()

if sys.stdout:
    stout_logger_id = logger.add(
        sys.stdout, level=0, diagnose=False, format=default_format
    )
    logger.debug("加载logger中，logger文件目录：{path}", path=log_path)

file_logger_id = logger.add(
    log_path,
    level=0,
    rotation="1 day",
    retention="1 week",
    delay=True,
    format=default_format,
)
logger.debug("加载logger成功")
logger = logger  # 发癫写法
