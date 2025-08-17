from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_async_session
from src.image.services import ImageService
from src.users.auth import get_current_user

image_router = APIRouter()
image_service = ImageService()


@image_router.post("/upload-image", response_model=dict)
def image_upload(file: UploadFile) -> dict:
    return image_service.upload_image(file)
