from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ROUND_NUM: int = 3
    SERVER: str = '192.168.22.155'
    PORT: str = '8080'
    TIMEOUT: int = 1750
    AVAILABLE_CLIENTS: int = 5
    FRACTION_FIT: float = 0.2
    FRACTION_EVALUATE: float = 1
    MIN_NUM_CLIENTS: int = 3
    MIN_EVALUATE_CLIENTS: int = 2
    SAMPLING_TIMEOUT: int = 60

