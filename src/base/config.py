import os
from datetime import datetime

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DB_USER: str = os.getenv('DB_USER')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_PORT: str = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

    @property
    def connection_string(self):
        values = self.model_dump()

        return (f'postgresql+asyncpg://'
                f'{values["DB_USER"]}:'
                f'{values["DB_PASSWORD"]}@'
                f'{values["DB_HOST"]}:{values["DB_PORT"]}/'
                f'{values["DB_NAME"]}')


settings = Settings()