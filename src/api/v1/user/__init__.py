from fastapi import APIRouter

user_router =APIRouter(prefix='/user', tags = ['User'])


from src.api.v1.user.add import router as add_user
from src.api.v1.user.get import router as get_user
from src.api.v1.user.delete import router as delete_user
from src.api.v1.user.refresh import router as refresh_user
from src.api.v1.user.login import router as login_user
from src.api.v1.user.logout import router as logout_user
from src.api.v1.user.register import router as register_user


user_router.include_router(add_user)
user_router.include_router(get_user)
user_router.include_router(delete_user)
user_router.include_router(refresh_user)
user_router.include_router(login_user)
user_router.include_router(logout_user)
user_router.include_router(register_user)