from app.core.dbUtils import execute_sel, execute_mod
from app.model.sampleParam import sampleParam

def select_sample_all(db, param=None):
    query = """
        SELECT 
              SAMPLE_CODE 
            , SAMPLE_DESC
        FROM TB_SAMPLE
    """
    return execute_sel(db, query, param)

def select_sample_detail(db, param):
    query = """
        SELECT 
              SAMPLE_CODE
            , SAMPLE_DESC
            , INSERT_ID
            , INSERT_DATE
            , MODIFY_ID
            , MODIFY_DATE
        FROM TB_SAMPLE 
        WHERE 1=1
        AND SAMPLE_CODE = :sample_code
    """
    if param.get("sample_desc"):
        query += """AND SAMPLE_DESC LIKE CONCAT('%', :sample_desc, '%')"""
    return execute_sel(db, query, param)

def update_sample(db, param: sampleParam):
    query = """
        UPDATE TB_SAMPLE SET 
              SAMPLE_DESC = :sample_desc 
            , MODIFY_ID = :modify_id
            , MODIFY_DATE = :modify_date 
        WHERE SAMPLE_CODE = :sample_code
    """
    return execute_mod(db, query, param.model_dump())
