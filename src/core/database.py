from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine
from typing import AsyncGenerator
from sqlalchemy.orm.session import sessionmaker, Session
from src.core.config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, echo=True)
sunc_en = create_engine(
    DATABASE_URL.replace("postgresql+asyncpg", "postgresql"), echo=True
)
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
session_maker = sessionmaker(
    sunc_en,  # The SQLAlchemy Engine used to connect to the database
    class_=Session,  # Optional: specify a custom Session class (default is sqlalchemy.orm.Session)
    expire_on_commit=False,  # Prevents objects from being expired after commit
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
