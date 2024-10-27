from pydantic import BaseModel, ConfigDict, Field
from datetime import date

class PharmacistsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    last_name: str
    first_name: str
    middle_name: str
    birth_date: date | None = Field(default=None)
    passport: str
    phone: str