from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PATH: str
    CLIENT_ORIGIN: str

    class Config:
        env_file = "./.env"


settings = Settings()
