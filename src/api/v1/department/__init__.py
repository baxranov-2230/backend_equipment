from fastapi import APIRouter

department_router = APIRouter(prefix='/department', tags=['Department'])

from src.api.v1.department.add import router as add_router
from src.api.v1.department.delete import router as delete_router
from src.api.v1.department.put import router as put_router
from src.api.v1.department.get import router as get_router

department_router.include_router(add_router)
department_router.include_router(delete_router)
department_router.include_router(put_router)
department_router.include_router(get_router)