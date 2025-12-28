from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    DRIVERNAME: str = "postgresql+asyncpg"
    DB_HOST: str = Field(description="Хост БД.")
    DB_PORT: int = Field(description="Порт БД.")
    DB_DATABASE: str = Field(description="Название БД.")
    DB_USERNAME: str = Field(description="Пользователь БД.")
    DB_PASSWORD: str = Field(description="Пароль БД.")
    model_config = SettingsConfigDict(env_file="template.env")

    @property
    def db_url(self) -> str:
        """Формирует строку подключения к PostgreSQL."""
        return (
            f"{self.DRIVERNAME}://"
            f"{self.DB_USERNAME}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.DB_DATABASE}"
        )


db_settings = Settings()
