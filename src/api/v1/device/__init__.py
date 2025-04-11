from fastapi.routing import APIRoute, APIRouter

device_router = APIRouter(prefix="/device", tags=['Device'])


from src.api.v1.device.add import router as add_router
from src.api.v1.device.delete import router as delete_router
from src.api.v1.device.get import router as get_router
from src.api.v1.device.put import router  as put_router

device_router.include_router(add_router)
device_router.include_router(delete_router)
device_router.include_router(get_router)
device_router.include_router(put_router)