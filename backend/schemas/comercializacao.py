from pydantic import BaseModel
from datetime import datetime

class CreateComercializacao(BaseModel):
    produto: str
    quantidade: int


class ShowComercializacao(BaseModel):
    produto: str
    quantidade: int
    created_at: datetime
    class Config():
        orm_mode = True
