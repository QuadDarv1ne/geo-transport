# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    yandex_api_key: str
    debug: bool

    class Config:
        env_file = ".env"

settings = Settings()