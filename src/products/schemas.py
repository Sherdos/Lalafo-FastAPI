from typing import List, Optional
from pydantic import BaseModel, Field

from src.users.schemas import UserResponse


class CategorySchema(BaseModel):
    id: int
    name: str
    model_config = {
        "from_attributes": True,
    }


class CategoryResponse(CategorySchema):
    parent_id: int | None
    childer: List["CategoryResponse"]


class ProductSchema(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = Field(None, max_length=255)
    price: float = Field(..., gt=0)
    image: str | None = Field(None, max_length=255)

    model_config = {
        "from_attributes": True,
    }

    # values['title'] -> values.title


class ProductCreateSchema(ProductSchema):
    category_id: int = Field(..., gt=0)


class ProductCreateInputSchema(ProductCreateSchema):
    user_id: int = Field(..., gt=0)


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    price: Optional[float] = Field(None, gt=0)
    image: Optional[str] = Field(None, max_length=255)


class ProductResponseSchema(ProductSchema):
    id: int
    user: UserResponse
    category: CategorySchema

    model_config = {
        "from_attributes": True,
    }


ProductResponseSchema.model_rebuild()
