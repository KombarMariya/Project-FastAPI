from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class DeliveriesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    purchase_id: int
    courier_id: int
    address: str
    delivery_date: datetime | None = Field(default=None)
    status: str