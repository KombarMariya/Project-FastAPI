from pydantic import BaseModel, Field, ConfigDict

class DosagesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str