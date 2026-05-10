from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customer_number = Column("customerNumber", Integer, primary_key=True, nullable=False)
    customer_name = Column("customerName", String(50), nullable=False)
    contact_last_name = Column("contactLastName", String(50), nullable=False)
    contact_first_name = Column("contactFirstName", String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    address_line1 = Column("addressLine1", String(50), nullable=False)
    address_line2 = Column("addressLine2", String(50), nullable=True)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=True)
    postal_code = Column("postalCode", String(15), nullable=True)
    country = Column(String(50), nullable=False)
    sales_rep_employee_number = Column("salesRepEmployeeNumber", Integer, ForeignKey("employees.employeeNumber"), nullable=True) 
    credit_limit = Column("creditLimit", Numeric(10, 2), nullable=True)

    orders = relationship("Order", back_populates="customer")
    payments = relationship("Payment", back_populates="customer")
    employee = relationship("Employee", back_populates="customer")


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

class Payment(Base):
    __tablename__ = "payments"

    customer_number = Column("customerNumber", Integer, ForeignKey("customers.customerNumber"), primary_key=True, nullable=False)
    check_number = Column("checkNumber", String(50), primary_key=True, nullable=False)
    payment_date = Column("paymentDate", Date, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    customer = relationship("Customer", back_populates="payments")


#Only defined the model with table name and primary key because i don't need other attributes to find count in Task 3
class Product(Base):
    __tablename__ = "products"
    product_code = Column("productCode", String(15), primary_key=True)

class Employee(Base):
    __tablename__ = "employees"
    employee_number = Column("employeeNumber", Integer, primary_key=True)
    customer = relationship("Customer", back_populates="employee")

class Office(Base):
    __tablename__ = "offices"
    office_code = Column("officeCode", String(10), primary_key=True)

class OrderDetail(Base):
    __tablename__ = "orderdetails"
    order_number = Column("orderNumber", Integer, primary_key=True)

class ProductLine(Base):
    __tablename__ = "productlines"
    product_line = Column("productLine", String(50), primary_key=True)