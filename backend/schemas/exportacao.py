from pydantic import BaseModel
from datetime import datetime

class CreateExportacao(BaseModel):
    pais: str
    quantidade: int
    valor: int


class ShowExportacao(BaseModel):
    pais: str
    quantidade: int
    valor: int
    created_at: datetime
    class Config():
        orm_mode = True
