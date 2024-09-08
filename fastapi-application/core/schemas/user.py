from pydantic import BaseModel

from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserRead(schemas.BaseUser[UserIdType]):
    pass
