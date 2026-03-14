from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class sampleParam(BaseModel):
    sample_code : Optional[int] = None
    sample_desc : Optional[str] = None
    insert_id   : Optional[str] = None
    insert_date : Optional[datetime] = None
    modify_id   : Optional[str] = None
    modify_date : Optional[datetime] = None
