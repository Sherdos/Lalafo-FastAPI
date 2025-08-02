from pydantic import BaseModel


class UserBase(BaseModel):
    """Base class for user-related schemas."""

    email: str
    is_superuser: bool = False


class UserCreate(UserBase):
    """Schema for creating a new user."""

    password: str


class UserUpdate(UserBase):
    """Schema for updating an existing user."""

    email: str | None = None
    password: str | None = None


class UserResponse(UserBase):
    id: int


class UserLoginAndRegister(BaseModel):
    """Schema for user login and registration."""

    email: str
    password: str

    model_config = {"from_attributes": True}
