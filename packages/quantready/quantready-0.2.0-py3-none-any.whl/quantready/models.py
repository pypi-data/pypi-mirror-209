from pydantic import BaseModel


class QuantReadyInfo(BaseModel):
    name: str
    template: str
    description: str
    repo: str
    version: str
