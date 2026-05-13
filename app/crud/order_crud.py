from sqlalchemy.orm import Session
from app.models import Order
from app.schemas.order_schemas import OrderCreate, OrderUpdate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()

def get_order(db: Session, order_number: int):
    order = db.query(Order).filter(Order.order_number == order_number).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def create_order(db: Session, data: OrderCreate):
    try: 
        db_order = Order(**data.model_dump())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def update_order(db: Session, order_number: int, data: OrderUpdate):
    try:
        db_order = get_order(db, order_number)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def delete_order(db: Session, order_number: int):
    db_order = get_order(db, order_number)
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted"}