from typing import List
from src.products.repositories import ProductDAO
from sqlalchemy.ext.asyncio import AsyncSession

from src.products.schemas import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)


class ProductService:
    """Service for managing products."""

    def __init__(self, session: AsyncSession):
        self.product_dao = ProductDAO(session)

    async def get_all_products(self) -> List[ProductResponseSchema]:
        """Fetch all products."""
        products = await self.product_dao.find_all()
        return [ProductResponseSchema.model_validate(product) for product in products]

    async def create_product(
        self, product_data: ProductCreateSchema
    ) -> ProductResponseSchema:
        """Create a new product."""
        try:
            product = await self.product_dao.create(product_data)
            return ProductResponseSchema.model_validate(product)
        except Exception as e:
            raise ValueError(f"Invalid product data. {e}")

    async def get_product_by_id(self, product_id: int) -> ProductResponseSchema:
        """Fetch a product by its ID."""
        product = await self.product_dao.find_one_or_none_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        return ProductResponseSchema.model_validate(product)

    async def update_product(
        self, product_id: int, product_data: ProductUpdateSchema
    ) -> ProductResponseSchema:
        """Update an existing product."""
        product = await self.product_dao.update(product_id, product_data)
        if not product:
            raise ValueError("Product not found")
        return ProductResponseSchema.model_validate(product)

    async def delete_product(self, product_id: int) -> dict:
        """Delete a product by its ID."""
        result = await self.product_dao.delete(product_id)
        if not result:
            raise ValueError("Product not found")
        return result
