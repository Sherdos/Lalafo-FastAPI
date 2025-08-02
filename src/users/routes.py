from fastapi import APIRouter, Depends

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


@routes.post("/login")
async def login_user(
    user: UserLoginAndRegister, session: AsyncSession = Depends(get_async_session)
):
    """Login an existing user."""

    service = UserService(session)
    logged_in_user = await service.get_user_by_email(user.email)

    if not logged_in_user:
        raise HTTPException(status_code=400, detail="User login failed")

    return logged_in_user
