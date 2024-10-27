from datetime import date

from pydantic import BaseModel, ConfigDict, Field

class CouriersSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    last_name: str
    first_name: str
    middle_name: str
    birth_date: date | None = Field(default=None)
    passport: str
    phone: str
    transport: str