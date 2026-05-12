from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    order_number = Column("orderNumber", Integer, primary_key=True, nullable=False)
    order_date = Column("orderDate", Date, nullable=False)
    required_date = Column("requiredDate", Date, nullable=False)
    shipped_date = Column("shippedDate", Date, nullable=True)
    status = Column(String(15), nullable=False)
    comments = Column(Text, nullable=True)
 
    customer_number = Column("customerNumber", Integer, ForeignKey("customers.customerNumber"), nullable=False)
    customer = relationship("Customer", back_populates="orders")

class OrderDetail(Base):
    __tablename__ = "orderdetails"
    order_number = Column("orderNumber", Integer, primary_key=True)