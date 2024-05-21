from pydantic import BaseModel
from datetime import datetime

class CreateImportacao(BaseModel):
    pais: str
    quantidade: int
    valor: int


class ShowImportacao(BaseModel):
    pais: str
    quantidade: int
    valor: int
    created_at: datetime
    class Config():
        orm_mode = True
