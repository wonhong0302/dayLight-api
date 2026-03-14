import logging
from logging.handlers import TimedRotatingFileHandler
import os
from dotenv import load_dotenv

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    
load_dotenv()

LOGGER_FILE = os.getenv("LOGGER_FILE") == "True"

def setup_logger():
    # 로거 생성 (전체 최저 레벨을 DEBUG로 설정)
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)

    # 파일 핸들러 설정 (ERROR 이상만 기록)
    file_handler = TimedRotatingFileHandler(
        filename=os.path.join(LOG_DIR, "error.log"),
        when="midnight",
        interval=1,
        backupCount=30,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.ERROR) # 파일에는 ERROR만 저장
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # 콘솔 핸들러 설정 (DEBUG 이상 모두 출력)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG) # 콘솔
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)

    # 로거에 핸들러 등록
    if LOGGER_FILE: # LOGGER_FILE true 인 경우에만 파일로 저장
        logger.addHandler(file_handler)
        
    logger.addHandler(console_handler)

    return logger


app_logger = setup_logger()