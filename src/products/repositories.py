from src.core.dao import BaseDAO
from src.products.models import Product


class ProductDAO(BaseDAO[Product]):  # Data Access Object for Product model.
    """Data Access Object for Product model."""

    model = Product
