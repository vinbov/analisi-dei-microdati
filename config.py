from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'My Application'
    environment: str = 'development'
    debug: bool = True

    class Config:
        env_file = '.env'

settings = Settings()