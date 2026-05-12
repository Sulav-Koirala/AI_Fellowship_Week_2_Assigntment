from pydantic import BaseModel

class OrderSchema(BaseModel):
    order_number: int
    status: str
    class Config:
        from_attributes = True