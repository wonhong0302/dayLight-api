# db util 파일
import os
from functools import wraps
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.core.logger import app_logger
from dotenv import load_dotenv
from app.core.messages import Msg

load_dotenv()

logger = os.getenv('LOGGER') == 'True'

def transactional(func):
    @wraps(func)
    def wrapper(db, *args, **kwargs):
        try:
            # 원본 비즈니스 로직 실행
            result = func(db, *args, **kwargs)
            db.commit()
            return result

        except SQLAlchemyError as e:
            # DB 에러
            db.rollback()
            if logger:
                app_logger.error(Msg.db_error_occur(str(e)))
            raise HTTPException(
                status_code=500,
                detail=Msg.DB_PROCESSING_ERROR
            )

        except Exception as e:
            # 기타 에러
            db.rollback()
            if logger:
                app_logger.error(Msg.logic_error_occur(str(e)))

            raise HTTPException(
                status_code=400,
                detail=Msg.request_error_occur(str(e))
            )

    return wrapper

# SELECT
def execute_sel(db: Session, query: str, params: dict = None):
    try:
        result = db.execute(text(query), params or {})
        if logger:
            app_logger.debug(
                f"SQL 실행 --------------------------------\n"
                f"{query.strip()}\n"
                f"Parameters: {params or {}}\n"
                f"-----------------------------------------"
            )
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]
    except SQLAlchemyError as e:
        # DB 에러
        if logger:
            app_logger.error(Msg.db_error_occur(str(e)))
        raise HTTPException(
            status_code=500,
            detail=Msg.RUN_QUERY_ERROR
        )
    except Exception as e:
        # 기타 에러
        if logger:
            app_logger.error(Msg.logic_error_occur(str(e)))
        raise HTTPException(
            status_code=400,
            detail=Msg.request_error_occur(str(e))
        )

# INSERT, UPDATE, DELETE
def execute_mod(db: Session, query: str, params: dict = None):
    result = db.execute(text(query), params or {})
    if logger:
        app_logger.debug(
            f"SQL 수정 --------------------------------\n"
            f"{query.strip()}\n"
            f"Parameters: {params or {}}\n"
            f"-----------------------------------------"
        )
    return result.rowcount

