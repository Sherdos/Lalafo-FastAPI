from sqlalchemy import select
from src.core.dao import BaseDAO
from src.products.models import Category, Product
from src.products.schemas import CategoryResponse


class ProductDAO(BaseDAO[Product]):  # Data Access Object for Product model.
    """Data Access Object for Product model."""

    model = Product

    async def get_tree(self):
        result = await self.session.execute(select(Category))
        categories = result.unique().scalars().all()
        return self.build_tree(list(categories))

    def build_tree(self, categories: list[Category]):
        def build_node(category_id):
            subcat = [
                CategoryResponse.model_validate(
                    {
                        "id": cat.id,
                        "name": cat.name,
                        "parent_id": cat.parent_id,
                        "childer": build_node(cat.id),
                    }
                )
                for cat in categories
                if cat.parent_id == category_id
            ]
            return subcat

        return build_node(None)
