from src.users.dao import UserDAO
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    """Service class for user-related operations."""

    def __init__(self, session: AsyncSession):
        self.user_dao = UserDAO(session)

    async def get_user_by_id(self, user_id: int):
        """Fetch a user by ID."""
        return await self.user_dao.find_one_or_none_by_id(user_id)

    async def create_user(self, user_data):
        """Create a new user."""
        return await self.user_dao.create(user_data)

    async def update_user(self, user_id: int, user_data):
        """Update an existing user."""
        return await self.user_dao.update(user_id, user_data)

    async def get_user_by_email(self, email: str):
        """Fetch a user by email."""
        return await self.user_dao.find_one_or_none(email=email)
