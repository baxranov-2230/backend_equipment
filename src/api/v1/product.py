from fastapi import APIRouter

product_router = APIRouter(prefix="/product", tags=['Products'])

@product_router.post("/")
async def add_product():
    ...

@product_router.get("/")
async def get_product():
    ...

@product_router.put("/")
async def change_product():
    pass


@product_router.delete("/")
async def delete_product():
    pass