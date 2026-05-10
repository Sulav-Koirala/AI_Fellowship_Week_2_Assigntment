#For Task 2
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from app import crud,schemas,database
from app.logger import logger

router = APIRouter(prefix="/customers", tags=['Customers'])

@router.get("/{customer_id}", response_model=schemas.CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(database.get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        logger.warning(f"Customer {customer_id} not found.")
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.get("/", response_model=List[schemas.CustomerOut])
def get_customers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    existing_customer = crud.get_customer(db, customer_id=customer.customer_number)
    if existing_customer:
        logger.error(f"Failed to create: Customer ID {customer.customer_number} already exists.")
        raise HTTPException(
            status_code=400, 
            detail="Customer number already registered"
        )
    
    logger.info(f"Creating new customer: {customer.customer_name}")
    return crud.create_customer(db=db, customer=customer)
