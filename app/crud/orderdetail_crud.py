from sqlalchemy.orm import Session
from app.models import OrderDetail
from app.schemas.orderdetail_schemas import OrderDetailCreate, OrderDetailUpdate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_order_details(db: Session, skip: int = 0, limit: int = 10):
    return db.query(OrderDetail).offset(skip).limit(limit).all()

def get_order_detail(db: Session, order_number: int, product_code: str):
    detail = db.query(OrderDetail).filter(
        OrderDetail.order_number == order_number,
        OrderDetail.product_code == product_code
    ).first()
    if not detail:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return detail

def create_order_detail(db: Session, data: OrderDetailCreate):
    try:
        db_detail = OrderDetail(**data.model_dump())
        db.add(db_detail)
        db.commit()
        db.refresh(db_detail)
        return db_detail
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def update_order_detail(db: Session, order_number: int, product_code: str, data: OrderDetailUpdate):
    try:
        db_detail = get_order_detail(db, order_number, product_code)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(db_detail, key, value)
        db.commit()
        db.refresh(db_detail)
        return db_detail
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def delete_order_detail(db: Session, order_number: int, product_code: str):
    db_detail = get_order_detail(db, order_number, product_code)
    db.delete(db_detail)
    db.commit()
    return {"message": "OrderDetail deleted"}