from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, String, Integer, ForeignKey, Column

from src.core.models import Base
from src.users.models import User


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category", lazy="joined"
    )
    parent_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=True
    )
    parent: Mapped["Category"] = relationship(
        "Category",
        back_populates="childer",
        remote_side="Category.id",
    )

    childer: Mapped[list["Category"]] = relationship(
        "Category", back_populates="parent"
    )


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products",
        foreign_keys=[category_id],
        lazy="selectin",
    )

    user: Mapped["User"] = relationship(
        "User", back_populates="products", foreign_keys=[user_id], lazy="selectin"
    )
