from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_NAME: str
    API_VERSION: str
    DEBUG: bool = False

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    """
    Carrega as configurações apenas uma vez durante
    toda a execução da aplicação.
    """
    return Settings()

settings = get_settings()