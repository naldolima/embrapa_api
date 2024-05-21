from sqlalchemy.orm import Session
from db.models.importacao import Importacao
from core.config import settings
from db.embrapa_site import get_field_1,get_field_2,get_field_3
import re

def create_new_importacao(db: Session):

    paises = get_field_1(settings.URL_IMPORTACAO)
    quantidades = get_field_2(settings.URL_IMPORTACAO)
    valores = get_field_3(settings.URL_IMPORTACAO)

    for i in range(len(paises)):
        pais = paises[i].replace("\n", "").strip(" ")
        qtd = "".join(re.findall("\d+", quantidades[i]))
        val = "".join(re.findall("\d+", valores[i]))

        if qtd == '':
            qtd = 0

        if val == '':
            val = 0

        importacao = Importacao(
            pais=pais,
            quantidade=int(qtd),
            valor=int(val)
        )

        db.add(importacao)
        db.commit()
        db.refresh(importacao)


def list_importacao(db: Session):
    importacao = db.query(Importacao).all()
    return importacao

def delete_importacao(db: Session):
    db.query(Importacao).delete()
    db.commit()

