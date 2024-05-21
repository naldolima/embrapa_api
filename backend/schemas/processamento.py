from pydantic import BaseModel
from datetime import datetime

class CreateProcessamento(BaseModel):
    cultivar: str
    quantidade: int


class ShowProcessamento(BaseModel):
    cultivar: str
    quantidade: int
    created_at: datetime
    class Config():
        orm_mode = True
