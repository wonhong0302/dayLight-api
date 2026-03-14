from typing import Annotated
from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.service import sampleService
from typing import List
from app.model.sampleParam import sampleParam

router = APIRouter(
    prefix="/sample",
    # tags=["Sample"]
)

DB = Annotated[Session, Depends(get_db)]

@router.post("/sample-update")
def sample_update(db: DB, param: List[sampleParam]):
    updated_count = sampleService.update_samples(db, param)

    return {
        "status": "success",
        "message": f"{updated_count}건의 데이터가 성공적으로 처리되었습니다."
    }

@router.get("/sample-select-all")
def select_sample_all(db: DB, request: Request):
    param = dict(request.query_params)
    return sampleService.select_sample_all(db, param)

@router.get("/sample-select-detail")
def select_sample_detail(db: DB, request: Request):
    param = dict(request.query_params)
    return sampleService.select_sample_detail(db, param)