from email.policy import HTTP

from fastapi import HTTPException
from src.users.dao import UserDAO
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import pbkdf2_sha256


# from src.core.dao import BaseDAO


class UserService:
    """Service class for user-related operations."""

    def __init__(self, session: AsyncSession):
        self.user_dao = UserDAO(session)

    async def get_user_by_id(self, user_id: int):
        """Fetch a user by ID."""
        return await self.user_dao.find_one_or_none_by_id(user_id)

    async def create_user(self, user_data):
        """Create a new user."""
        hashed_password = pbkdf2_sha256.hash(user_data.password)
        user_data.password = hashed_password
        return await self.user_dao.create(user_data)

    async def update_user(self, user_id: int, user_data):
        """Update an existing user."""
        return await self.user_dao.update(user_id, user_data)

    async def get_user_by_email(self, email: str):
        """Fetch a user by email."""
        return await self.user_dao.find_one_or_none(email=email)

    async def authenticate_user(self, user_data):
        """Authenticate a user."""
        user = await self.get_user_by_email(user_data.email)
        if not user or not pbkdf2_sha256.verify(user_data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user
