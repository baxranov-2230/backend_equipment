from fastapi import APIRouter
from src.api.v1.super_admin import super_admin_router
from src.api.v1.user import user_router
from src.api.v1.department import department_router
from src.api.v1.product import product_router

api_v1_router = APIRouter(prefix="/v1")



api_v1_router.include_router(super_admin_router)
api_v1_router.include_router(user_router)
api_v1_router.include_router(department_router)
api_v1_router.include_router(product_router)
