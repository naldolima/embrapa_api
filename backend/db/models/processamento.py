from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base_class import Base

class Processamento(Base):
    id = Column(Integer, primary_key=True)
    cultivar = Column(String,nullable=True)
    quantidade = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=datetime.now())

