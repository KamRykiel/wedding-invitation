from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")

    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/wedding"
    cors_origins: str = "http://localhost:5174,http://localhost:8080"
    static_uploads_dir: str = "app/static/uploads"


settings = Settings()

