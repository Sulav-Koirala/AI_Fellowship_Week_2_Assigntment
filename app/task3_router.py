from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from fastapi import APIRouter,Depends
from app import models,crud,database
from app.logger import logger

router = APIRouter(prefix="/count", tags=['Counts'])

@router.get("/customers")
async def count_customers(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/customers")
    count =  await crud.get_count(db, models.Customer)
    return {"customers": count}

@router.get("/orders")
async def count_orders(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/orders")
    count =  await crud.get_count(db, models.Order)
    return {"orders": count}

@router.get("/payments")
async def count_payments(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/payements")
    count =  await crud.get_count(db, models.Payment)
    return {"payments": count}

@router.get("/employees")
async def count_employees(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/employees")
    count =  await crud.get_count(db, models.Employee)
    return {"employees": count}

@router.get("/products")
async def count_products(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/products")
    count =  await crud.get_count(db, models.Product)
    return {"products": count}

@router.get("/offices")
async def count_offices(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/offices")
    count =  await crud.get_count(db, models.Office)
    return {"offices": count}

@router.get("/orderdetails")
async def count_orderdetails(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/orderdetails")
    count =  await crud.get_count(db, models.OrderDetail)
    return {"orderdetails": count}

@router.get("/productlines")
async def count_productlines(db: AsyncSession = Depends(database.get_async_db)):
    logger.info("Request received: GET /count/productlines")
    count =  await crud.get_count(db, models.ProductLine)
    return {"productlines": count}

@router.get("/overall_counts")
async def get_overall_counts(session_factory=Depends(database.get_async_session_factory)):
    logger.info("Request: Starting concurrent counts")

    async def count(model):
        async with session_factory() as session:
            return await crud.get_count(session, model)

    results = await asyncio.gather(
        count(models.Customer),
        count(models.Order),
        count(models.Product),
        count(models.Employee),
        count(models.Office),
        count(models.Payment),
        count(models.OrderDetail),
        count(models.ProductLine),
    )

    return {
        "customers": results[0],
        "orders": results[1],
        "products": results[2],
        "employees": results[3],
        "offices": results[4],
        "payments": results[5],
        "orderdetails": results[6],
        "productlines": results[7],
    }