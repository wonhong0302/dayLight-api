from .sampleController import router as sample_router

# 등록할 라우터들을 리스트에 담습니다.
# 각 라우터가 이미 prefix를 가지고 있으므로 객체만 담으면 됩니다.
all_routers = [
    sample_router,
]