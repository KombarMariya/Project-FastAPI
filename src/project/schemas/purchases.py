from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class PurchasesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    pharmacist_id: int
    quantity: int
    total_amount: float
    date_time: datetime