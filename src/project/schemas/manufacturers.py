from pydantic import BaseModel, Field, ConfigDict

class ManufacturersSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    country: str
    city: str
    phone: str | None = Field(default=None)