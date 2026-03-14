from typing import Any, Union

def to_str(value: Any, default: str = "") -> str:
    # 어떤 값이든 문자열로 변환 (None이면 기본값 반환)
    if value is None:
        return default
    return str(value).strip()

def to_int(value: Any, default: int = 0) -> int:
    # 문자열이나 실수를 정수로 변환 (실패 시 기본값 반환)
    try:
        if value is None or str(value).strip() == "":
            return default
        return int(float(value))
    except (ValueError, TypeError):
        return default

def to_float(value: Any, default: float = 0.0) -> float:
    # 문자열이나 정수를 실수(Double)로 변환
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(value)
    except (ValueError, TypeError):
        return default

def nvl(value: Any, default: Any) -> Any:
    # Null 값 처리
    return value if value is not None else default