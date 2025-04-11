from fastapi import APIRouter

from src.utils import refresh_access_token

router = APIRouter()


@router.post("/refresh")
def refresh_token_endpoint(refresh_token: str):
        tokens = refresh_access_token(refresh_token)
        access_token=tokens.get('access_token')
        refresh_token=tokens.get('refresh_token')
        return {'access_token': access_token, 'refresh_token': refresh_token}