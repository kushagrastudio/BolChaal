"""Application configuration. Load secrets from environment variables."""


class Settings:
    app_name: str = "BolChaal"
    environment: str = "development"


settings = Settings()
