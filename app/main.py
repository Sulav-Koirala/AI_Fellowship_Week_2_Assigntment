from fastapi import FastAPI
from app.routers import count_routers,customer_routers

app = FastAPI()
app.include_router(customer_routers.router)
app.include_router(count_routers.router)