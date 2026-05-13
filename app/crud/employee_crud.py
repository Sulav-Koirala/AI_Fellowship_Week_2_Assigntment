from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Employee
from app.schemas.employee_schemas import EmployeeCreate, EmployeeUpdate
from fastapi import HTTPException

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_number: int):
    employee = db.query(Employee).filter(Employee.employee_number == employee_number).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

def create_employee(db: Session, data: EmployeeCreate):
    try:
        db_employee = Employee(**data.model_dump())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="ForeignKey Error: Ensure the Office Code and Manager ID exist."
        )

def update_employee(db: Session, employee_number: int, data: EmployeeUpdate):
    db_employee = get_employee(db, employee_number)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_number: int):
    db_employee = get_employee(db, employee_number)
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted"}