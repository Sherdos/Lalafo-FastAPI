from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.core.database import get_async_session
from src.users.models import User
from src.users.service import UserService
from sqlalchemy.ext.asyncio import AsyncSession

algorithm = "HS256"
secret_key = "Helloworld"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_async_session),
) -> User:
    """Get the current user from the JWT token."""
    user_service = UserService(session)
    try:
        payload = jwt.decode(
            token, secret_key, algorithms=[algorithm]
        )  # {"uid": user_id}
        user_id: int = payload.get("uid", "")
        if user_id is None:
            raise JWTError("User ID not found in token")
        user = await user_service.get_user_by_id(user_id)
        if user is None:
            raise JWTError("User not found")
        return user
    except JWTError as e:
        raise JWTError(f"Invalid token: {str(e)}") from e


def create_access_token(user_id: int) -> str:
    """Create a JWT access token for the user."""
    payload = {"uid": user_id}
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token
