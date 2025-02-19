from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    REDIS_URL: str
    EMAIL_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
