from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.orderdetail_schemas import OrderDetailCreate, OrderDetailOut, OrderDetailUpdate
from app.crud import orderdetail_crud
from typing import List

router = APIRouter(prefix="/orderdetails", tags=["OrderDetails"])

@router.get("/", response_model=List[OrderDetailOut])
def read_order_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return orderdetail_crud.get_order_details(db, skip, limit)

@router.get("/{order_number}/{product_code}", response_model=OrderDetailOut)
def read_order_detail(order_number: int, product_code: str, db: Session = Depends(get_db)):
    return orderdetail_crud.get_order_detail(db, order_number, product_code)

@router.post("/", response_model=OrderDetailOut)
def create_order_detail(detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return orderdetail_crud.create_order_detail(db, detail)

@router.put("/{order_number}/{product_code}", response_model=OrderDetailOut)
def update_order_detail(order_number: int, product_code: str, detail: OrderDetailUpdate, db: Session = Depends(get_db)):
    return orderdetail_crud.update_order_detail(db, order_number, product_code, detail)

@router.delete("/{order_number}/{product_code}")
def delete_order_detail(order_number: int, product_code: str, db: Session = Depends(get_db)):
    return orderdetail_crud.delete_order_detail(db, order_number, product_code)