from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.models import Base


class User(Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="user", lazy="joined"
    )
