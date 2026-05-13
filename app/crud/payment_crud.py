from sqlalchemy.orm import Session
from app.models import Payment
from app.schemas.payment_schemas import PaymentCreate, PaymentUpdate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_payments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Payment).offset(skip).limit(limit).all()

def get_payment(db: Session, customer_number: int, check_number: str):
    payment = db.query(Payment).filter(
        Payment.customer_number == customer_number,
        Payment.check_number == check_number
    ).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

def create_payment(db: Session, data: PaymentCreate):
    try:
        db_payment = Payment(**data.model_dump())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def update_payment(db: Session, customer_number: int, check_number: str, data: PaymentUpdate):
    try:
        db_payment = get_payment(db, customer_number, check_number)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error"
        )

def delete_payment(db: Session, customer_number: int, check_number: str):
    db_payment = get_payment(db, customer_number, check_number)
    db.delete(db_payment)
    db.commit()
    return {"message": "Payment deleted"}