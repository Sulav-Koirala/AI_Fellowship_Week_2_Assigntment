from sqlalchemy.orm import Session,joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app import models, schemas
from app.logger import logger

#task 2
def get_customer(db: Session, customer_id: int):
    logger.info(f"Searching for customer ID: {customer_id}")
    return db.query(models.Customer).options(joinedload(models.Customer.orders), joinedload(models.Customer.payments))\
            .filter(models.Customer.customer_number == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    logger.info(f"Fetching customers with offset {skip} and limit {limit}")
    return db.query(models.Customer).options(joinedload(models.Customer.orders), joinedload(models.Customer.payments)).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    logger.info(f"Created new customer with ID: {db_customer.customer_number}")
    return db_customer

#task 3
async def get_count(db: AsyncSession, model):
    model_name = model.__name__
    logger.info(f"Starting count query for {model_name}")
    try:
        result = await db.execute(select(func.count()).select_from(model))
        count = result.scalar() or 0
        logger.info(f"Completed count for {model_name}: {count}")
        return count 
    except Exception as e:
        logger.error(f"Error counting {model_name}: {str(e)}")
        return 0
    