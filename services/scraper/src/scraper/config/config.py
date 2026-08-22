from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hh_api_url: str
    request_timeout: float = 10.0
    retries : int = 3