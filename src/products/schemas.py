from typing import Optional
from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    id: int
    name: str


class ProductSchema(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = Field(None, max_length=255)
    price: float = Field(..., gt=0)
    image: str | None = Field(None, max_length=255)
    category_id: int = Field(..., gt=0)

    model_config = {
        "from_attributes": True,
    }

    # values['title'] -> values.title


class ProductCreateSchema(ProductSchema): ...


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    price: Optional[float] = Field(None, gt=0)
    image: Optional[str] = Field(None, max_length=255)


class ProductResponseSchema(ProductSchema):
    id: int
