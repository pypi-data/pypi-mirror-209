from typing import (
    Any,
    List,
)

from dotenv import find_dotenv
from pydantic import BaseSettings

from src.constants import Environment


class Config(BaseSettings):
    env_file = find_dotenv('.secrets/.env')
    env_file_encoding = 'utf-8'
    # ENVIRONMENT: Environment = Environment.LOCAL
    # DEBUG: bool = False
    # CORS_ORIGINS: List[str]
    # CORS_ORIGINS_REGEX: str | None
    # CORS_HEADERS: List[str]
    IDPA_URL: str
    # APP_VERSION: str = '1'


settings = Config(_env_file='.env')

app_configs: dict[str, Any] = {'title': 'JWT-Validation - API'}
if settings.ENVIRONMENT.is_deployed:
    app_configs['root_path'] = f'/v{settings.APP_VERSION}'

if not settings.ENVIRONMENT.is_debug:
    app_configs['openapi_url'] = None  # hide docs
#