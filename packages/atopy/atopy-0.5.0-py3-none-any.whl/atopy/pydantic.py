from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
    BaseSettings,
)

BModel = BaseModel


class BSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
