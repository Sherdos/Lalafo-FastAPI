from pydantic import BaseModel
from sqlalchemy import select
from src.core.models import Base

from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic

T = TypeVar("T", bound=Base)


class BaseDAO(Generic[T]):
    model: type[T]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_all(self) -> list[T]:
        """Fetch all records."""
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def find_one_or_none_by_id(self, id: int) -> T | None:
        """Fetch a record by its ID."""
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, values: BaseModel) -> T:
        """Create a new record."""
        obj = self.model(**values.model_dump())
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, id: int, values: BaseModel) -> T | None:
        """Update an existing record."""
        obj = await self.find_one_or_none_by_id(id)

        for key, value in values.model_dump().items():
            setattr(obj, key, value)

        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> dict | None:
        """Delete a record by its ID."""
        obj = await self.find_one_or_none_by_id(id)
        if not obj:
            return None

        await self.session.delete(obj)
        await self.session.commit()
        return {"message": "Record deleted successfully"}
