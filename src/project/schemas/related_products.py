from pydantic import BaseModel, Field, ConfigDict

class RelatedProductsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    quantity: int