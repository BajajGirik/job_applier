class EnvError(Exception):
    def __init__(self, message: str, env_name: str) -> None:
        super().__init__(message)
        self.env_name = env_name

    def __str__(self) -> str:
        return f"{self.env_name}: {self}"

