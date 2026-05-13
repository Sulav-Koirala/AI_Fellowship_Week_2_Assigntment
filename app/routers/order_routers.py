from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order_schemas import OrderCreate, OrderOut, OrderUpdate
from app.crud import order_crud
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=List[OrderOut])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return order_crud.get_orders(db, skip, limit)

@router.get("/{order_number}", response_model=OrderOut)
def read_order(order_number: int, db: Session = Depends(get_db)):
    return order_crud.get_order(db, order_number)

@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(db, order)

@router.put("/{order_number}", response_model=OrderOut)
def update_order(order_number: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return order_crud.update_order(db, order_number, order)

@router.delete("/{order_number}")
def delete_order(order_number: int, db: Session = Depends(get_db)):
    return order_crud.delete_order(db, order_number)