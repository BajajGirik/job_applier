import os
from .custom_exceptions import EnvError

def get_env(env_name: str) -> str:
    val = os.getenv(env_name)

    if val is None:
        raise EnvError("Missing env", env_name)

    return val
