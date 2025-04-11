
import uvicorn
from fastapi import FastAPI


from src.api.v1 import  api_v1_router


app = FastAPI()

app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
