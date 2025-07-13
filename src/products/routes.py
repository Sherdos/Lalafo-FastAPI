from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.products.models import Product
from src.products.schemas import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)

routes = APIRouter()


@routes.get("/products")
async def get_products(
    session: AsyncSession = Depends(get_async_session),
) -> List[ProductResponseSchema]:
    """Fetch all products."""
    result = await session.execute(select(Product))
    return list(result.scalars().all())


@routes.post("/products")
async def create_product(
    product: ProductCreateSchema,
    session: AsyncSession = Depends(get_async_session),
) -> ProductResponseSchema:
    """Create a new product."""
    new_product = Product(**product.model_dump())
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product


@routes.get("/products/{product_id}", response_model=ProductResponseSchema)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> ProductResponseSchema:
    """Fetch a product by ID."""
    result = await session.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@routes.put("/products/{product_id}")
async def update_product(
    product_id: int,
    product: ProductUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
) -> ProductResponseSchema:
    """Update an existing product."""
    result = await session.execute(select(Product).where(Product.id == product_id))
    existing_product = result.scalar_one_or_none()

    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.model_dump().items():
        setattr(existing_product, key, value)

    await session.commit()
    await session.refresh(existing_product)
    return existing_product


@routes.delete("/products/{product_id}")
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    """Delete a product by ID."""
    result = await session.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await session.delete(product)
    await session.commit()
    return {"detail": "Product deleted successfully"}
