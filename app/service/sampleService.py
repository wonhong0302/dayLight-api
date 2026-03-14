from app.core.dbUtils import transactional
from typing import List
from sqlalchemy.orm import Session
from app.repositories import sampleRepository
from datetime import datetime
from app.model.sampleParam import sampleParam
from app.core.messages import Msg

@transactional
def update_samples(db: Session, param_list: List[sampleParam]):
    if not param_list:
        raise Exception(Msg.NULL_REQUEST_PARAMETER)

    now = datetime.now()
    totalCount = 0
    # 건바이건 작업
    for param in param_list:
        param.modify_date = now
        cnt = sampleRepository.update_sample(db, param)
        if cnt == 0:
            raise Exception(Msg.update_error_occur("TB_SAMPLE UPDATE FAIL."))
        totalCount += cnt

    return totalCount

def select_sample_all(db: Session, param: dict):
    return sampleRepository.select_sample_all(db, param)

def select_sample_detail(db: Session, param: dict):
    return sampleRepository.select_sample_detail(db, param)