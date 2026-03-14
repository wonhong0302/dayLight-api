class Settings:
    # 허용할 도메인 리스트를 여기에 직접 관리
    ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
    ]

    # 나중에 필요한 설정(DB 주소 등)도 여기에 추가하면 관리하기 편합니다.
    PROJECT_NAME = "FastAPI Template"

settings = Settings()