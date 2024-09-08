from fastapi import APIRouter

from api.dependencies.authentication.fastapi_users_router import fastapi_users
from api.dependencies.authentication.backend import authentication_backend
from core.config import settings
from core.schemas.user import UserRead, UserCreate


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)
# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=True,
    ),
)


# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead, UserCreate
    )
)


#/request-verify-token and /verify
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


#/forgot-password and /reset-password
router.include_router(
    fastapi_users.get_reset_password_router(),
)
