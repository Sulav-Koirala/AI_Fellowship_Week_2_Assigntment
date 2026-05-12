from pydantic import BaseModel

class PaymentSchema(BaseModel):
    check_number: str
    amount: float
    class Config:
        from_attributes = True