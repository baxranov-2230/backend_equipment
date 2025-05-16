from fastapi.routing import APIRoute, APIRouter

category_router = APIRouter(prefix="/category", tags=['Category'])


from src.api.v1.category.add import router as add_router
from src.api.v1.category.get_all import router as get_router


category_router.include_router(add_router)
category_router.include_router(get_router)
