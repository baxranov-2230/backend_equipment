
import uvicorn
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from src.api.v1 import  api_v1_router


app = FastAPI()

app.include_router(api_v1_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # Test uchun; keyin frontend URLni qo‘shing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",

    ],
)