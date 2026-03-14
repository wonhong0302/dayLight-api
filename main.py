from fastapi import FastAPI
from app.api import all_routers
from fastapi.middleware.cors import CORSMiddleware
from app.core.configs import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in all_routers:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "dayLight 캘린더 api 입니다."}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
