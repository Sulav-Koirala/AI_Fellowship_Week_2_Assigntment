from pydantic import BaseModel
from typing import Optional,List
from app.schemas.order_schemas import OrderSchema
from app.schemas.payment_schemas import PaymentSchema

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