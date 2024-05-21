from pydantic import BaseModel
from datetime import datetime

class CreateProducao(BaseModel):
    produto: str
    quantidade: int


class ShowProducao(BaseModel):
    produto: str
    quantidade: int
    created_at: datetime
    class Config():
        orm_mode = True
