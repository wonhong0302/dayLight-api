# message 관리 파일
# 1. 구분별, 2. 알파벳 순으로 나열할 것
class Msg:
    # ERROR
    DB_PROCESSING_ERROR     = "데이터 처리 중 오류가 발생했습니다."
    INVALID_INPUT           = "입력값이 올바르지 않습니다."
    NOT_FOUND               = "요청하신 정보를 찾을 수 없습니다."
    NULL_REQUEST_PARAMETER  = "요청 데이터가 없습니다."
    RUN_QUERY_ERROR         = "조회 실행 중 오류가 발생했습니다."
    UNAUTHORIZED            = "접근 권한이 없습니다."
    
    # SUCCESS
    LOGIN_SUCCESS       = "로그인에 성공했습니다."
    PROCESS_SUCCESS     = "정상적으로 처리되었습니다."

    @staticmethod
    def db_error_occur(detail: str):
        return f"DB 에러 발생 | 상세: {detail}"

    @staticmethod
    def logic_error_occur(detail: str):
        return f"로직 에러 발생 | 상세: {detail}"

    @staticmethod
    def request_error_occur(detail: str):
        return f"요청 처리 중 오류가 발생했습니다: {detail}"

    @staticmethod
    def update_error_occur(detail: str):
        return f"업데이트 중 오류가 발생했습니다. 내용: {detail}"
