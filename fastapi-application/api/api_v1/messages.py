from fastapi import (
    APIRouter,
    Depends,
)

from api.dependencies.authentication.fastapi_users_router import (
    current_user,
    current_super_user,
)
from core.config import settings
from core.models import User
from core.schemas.user import UserRead


router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"]
)

@router.get("")
def get_user_messages(
        user: User = Depends(current_user),
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
        user: User = Depends(current_super_user),
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }
