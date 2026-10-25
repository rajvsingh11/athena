import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", "5432"))
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "athena_dev")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "Singh@11")
    
    #Security settings
    JWT_SECRET_KEY: str = os.getenv(
    "JWT_SECRET_KEY",
    "development-only-secret-change-before-deployment",
    )

    JWT_ALGORITHM: str = os.getenv(
    "JWT_ALGORITHM",
    "HS256",
    )

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )

settings = Settings()