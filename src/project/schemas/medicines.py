from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

class MedicinesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    creation_date: datetime
    expiration_period: int
    price: float
    quantity: int
    release_condition: str
    type_of_medicine_id: int
    release_form_id: int
    manufacturer_id: int
    dosage_id: int