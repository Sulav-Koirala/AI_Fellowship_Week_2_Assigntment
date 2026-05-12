from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    employee_number = Column("employeeNumber", Integer, primary_key=True)
    customer = relationship("Customer", back_populates="employee")