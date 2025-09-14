from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.products.deps import get_current_user_and_check_owner
from src.products.schemas import (
    CategoryResponse,
    ProductCreateInputSchema,
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
    Filters
)
from src.products.services import ProductService
from src.users.auth import get_current_user
from src.users.models import User

routes = APIRouter()

# routes(FastAPI) -> services -> dao(Database Access Object)
#                             -> MongoDB Access Object


@routes.post("/search/products")
async def get_products(
    filters: Filters,
    session: AsyncSession = Depends(get_async_session), 
) -> List[ProductResponseSchema]:
    """Fetch all products."""
    service = ProductService(session)
    products = await service.get_all_products(filters)

    return products


@routes.post("/products")
async def create_product(
    product: ProductCreateSchema,
    session: AsyncSession = Depends(get_async_session),
    user_data: User = Depends(get_current_user),
) -> ProductResponseSchema:
    """Create a new product."""
    try:
        service = ProductService(session)
        model = ProductCreateInputSchema.model_validate(
            {**product.model_dump(), "user_id": user_data.id}
        )
        return await service.create_product(model)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@routes.get("/products/{product_id}", response_model=ProductResponseSchema)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> ProductResponseSchema:
    """Fetch a product by ID."""
    try:
        service = ProductService(session)
        return await service.get_product_by_id(product_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")


@routes.put("/products/{product_id}")
async def update_product(
    product_id: int,
    product: ProductUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
    user_data: User = Depends(get_current_user_and_check_owner),
) -> ProductResponseSchema:
    """Update an existing product."""
    try:
        service = ProductService(session)
        return await service.update_product(product_id, product)
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")


@routes.delete("/products/{product_id}")
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
    user_data: User = Depends(get_current_user_and_check_owner),
) -> dict:
    """Delete a product by ID."""
    try:
        service = ProductService(session)
        return await service.delete_product(product_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")


@routes.get("/categories/tree", response_model=List[CategoryResponse])
async def get_tree(session: AsyncSession = Depends(get_async_session)):
    service = ProductService(session)
    return await service.get_tree()
