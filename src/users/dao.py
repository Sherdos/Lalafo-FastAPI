from src.core.dao import BaseDAO
from src.users.models import User


class UserDAO(BaseDAO[User]):
    """Data Access Object for User model."""

    model = User
