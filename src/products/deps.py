from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException

from src.core.database import get_async_session
from src.products.models import Product
from src.users.auth import get_current_user
from src.users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


async def get_current_user_and_check_owner(
    product_id: int,
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_async_session),
) -> User:
    """Get the current user and check ownership."""
    print(f"Checking ownership for product ID: {product_id}")
    user = await get_current_user(token, session)
    stmt = select(Product).where(
        Product.user_id == user.id and Product.id == product_id
    )
    result = await session.execute(stmt)
    is_owner = result.first() is not None
    if not user.is_superuser and not is_owner:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return user
