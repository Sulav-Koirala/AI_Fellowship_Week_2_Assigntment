from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Office(Base):
    __tablename__ = "offices"
    office_code = Column("officeCode", String(10), primary_key=True)