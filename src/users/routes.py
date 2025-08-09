from fastapi import APIRouter, Depends

from src.users.auth import create_access_token, get_current_user
from src.users.models import User
from src.users.schemas import UserCreate, UserLoginAndRegister, UserResponse
from src.users.service import UserService

from src.core.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


routes = APIRouter()


@routes.get("/users/{user_id}")
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    """Fetch a user by ID."""

    service = UserService(session)
    user = await service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@routes.post("/register")
async def register_user(
    user: UserLoginAndRegister, session: AsyncSession = Depends(get_async_session)
):
    """Register a new user."""

    service = UserService(session)
    new_user = await service.create_user(user)

    if not new_user:
        raise HTTPException(status_code=400, detail="User registration failed")

    return new_user


@routes.post("/auth/token")
async def login_user(
    user_data: UserLoginAndRegister, session: AsyncSession = Depends(get_async_session)
):
    """Login an existing user."""

    service = UserService(session)
    user = await service.authenticate_user(user_data)
    token = create_access_token(user.id)

    return {"access_token": token}


@routes.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get the current user."""
    return current_user
