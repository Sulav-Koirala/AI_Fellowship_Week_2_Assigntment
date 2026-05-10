from fastapi import FastAPI
from app import router,task3_router

app = FastAPI()
app.include_router(router.router)
app.include_router(task3_router.router)