from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class PurchasedMedicinesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    medicine_id: int
    quantity: int
    amount: float
    date_time: datetime
    purchase_id: int