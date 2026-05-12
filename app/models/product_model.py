from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    product_code = Column("productCode", String(15), primary_key=True)


class ProductLine(Base):
    __tablename__ = "productlines"
    product_line = Column("productLine", String(50), primary_key=True)