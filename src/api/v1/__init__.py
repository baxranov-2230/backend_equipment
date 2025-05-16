from fastapi import APIRouter

from .device import device_router
from .user import user_router
from .department import department_router
from .category import category_router

api_v1_router = APIRouter(prefix='/v1')

api_v1_router.include_router(user_router)
api_v1_router.include_router(department_router)
api_v1_router.include_router(device_router)
api_v1_router.include_router(category_router)