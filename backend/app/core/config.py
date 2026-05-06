from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")

    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/wedding"
    cors_origins: str = "http://localhost:5174,http://localhost:8080"
    static_uploads_dir: str = "app/static/uploads"
    auto_create_and_seed: bool = True

    @property
    def database_url_sqlalchemy(self) -> str:
        # Supabase often provides postgres://...; SQLAlchemy wants postgresql+psycopg://...
        if self.database_url.startswith("postgres://"):
            return self.database_url.replace("postgres://", "postgresql+psycopg://", 1)
        return self.database_url


settings = Settings()

