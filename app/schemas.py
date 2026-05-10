from pydantic import BaseModel
from typing import Optional,List

class OrderSchema(BaseModel):
    order_number: int
    status: str
    class Config:
        from_attributes = True

class PaymentSchema(BaseModel):
    check_number: str
    amount: float
    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    customer_name : str
    contact_last_name : str
    contact_first_name : str
    phone : str
    address_line1: str
    city : str
    country : str
    class Config:
        from_attributes = True

class CustomerCreate(CustomerBase):
    customer_number : int
    class Config:
        from_attributes = True

class CustomerUpdate(CustomerBase):
    __annotations__ = {k: Optional[v] for k, v in CustomerBase.__annotations__.items()}

class CustomerOut(CustomerBase):
    customer_number : int
    orders : List[OrderSchema] = []
    payments : List[PaymentSchema] = []
    class Config:
        from_attributes = True
