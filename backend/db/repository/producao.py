from sqlalchemy.orm import Session
from db.models.producao import Producao
from core.config import settings
from db.embrapa_site import get_field_1,get_field_2
import re

def create_new_producao(db: Session):

    produtos = get_field_1(settings.URL_PRODUCAO)
    quantidades = get_field_2(settings.URL_PRODUCAO)

    for i in range(len(produtos)):
        prod = produtos[i].replace("\n", "").strip(" ")
        qtd = "".join(re.findall("\d+", quantidades[i]))
        if qtd == '':
            qtd = 0
        producao = Producao(
            produto=prod,
            quantidade=int(qtd)
        )

        db.add(producao)
        db.commit()
        db.refresh(producao)


def list_producao(db: Session):
    producao = db.query(Producao).all()
    return producao

def delete_producao(db: Session):
    db.query(Producao).delete()
    db.commit()

