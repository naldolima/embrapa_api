from sqlalchemy.orm import Session
from db.models.processamento import Processamento
from core.config import settings
from db.embrapa_site import get_field_1,get_field_2
import re

def create_new_processamento(db: Session):

    cultivar = get_field_1(settings.URL_COMERCIALIZACAO)
    quantidades = get_field_2(settings.URL_COMERCIALIZACAO)

    for i in range(len(cultivar)):
        cult = cultivar[i].replace("\n", "").strip(" ")
        qtd = "".join(re.findall("\d+", quantidades[i]))
        if qtd == '':
            qtd = 0
        processamento = Processamento(
            cultivar=cult,
            quantidade=int(qtd)
        )

        db.add(processamento)
        db.commit()
        db.refresh(processamento)


def list_processamento(db: Session):
    processamento = db.query(Processamento).all()
    return processamento

def delete_processamento(db: Session):
    db.query(Processamento).delete()
    db.commit()

