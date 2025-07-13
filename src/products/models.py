from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, String, Integer, ForeignKey, Column

from src.models import Base


class Category(Base):
    __tablename__ = "categories"
    """ id: int = Column(Integer, primary_key=True) """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=True)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
