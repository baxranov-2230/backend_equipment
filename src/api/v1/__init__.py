from fastapi import APIRouter
from .super_admin import super_admin_router
from .user import user_router

api_v1_router = APIRouter(prefix="/v1")


api_v1_router.include_router(super_admin_router)
api_v1_router.include_router(user_router)