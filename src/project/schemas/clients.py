from pydantic import BaseModel, ConfigDict, Field

class ClientsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    discount: float
