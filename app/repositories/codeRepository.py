from app.core.dbUtils import execute_sel, execute_mod

def select_code(db, param):
    query = """
        SELECT /* from codeRepository.select_code by codeController */
              CODE_LGROUP
            , CODE_MGROUP
            , CODE_NAME
            , REF1
            , REF2
            , REF3
        FROM TB_CODE 
        WHERE CODE_LGRUOP = :code_lgroup
        AND CODE_MGROUP = :code_mgroup
    """
    return execute_sel(db, query, param)
