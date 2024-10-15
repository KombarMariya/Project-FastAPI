from pydantic import BaseModel, Field, ConfigDict

class ReleaseFormsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
