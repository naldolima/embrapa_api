from sqlalchemy.orm import Session
from db.models.comercializacao import Comercializacao
from core.config import settings
from db.embrapa_site import get_field_1,get_field_2
import re

def create_new_comercializacao(db: Session):

    produtos = get_field_1(settings.URL_COMERCIALIZACAO)
    quantidades = get_field_2(settings.URL_COMERCIALIZACAO)

    for i in range(len(produtos)):
        prod = produtos[i].replace("\n", "").strip(" ")
        qtd = "".join(re.findall("\d+", quantidades[i]))
        if qtd == '':
            qtd = 0
        comercializacao = Comercializacao(
            produto=prod,
            quantidade=int(qtd)
        )

        db.add(comercializacao)
        db.commit()
        db.refresh(comercializacao)


def list_comercializacao(db: Session):
    comercializacao = db.query(Comercializacao).all()
    return comercializacao

def delete_comercializacao(db: Session):
    db.query(Comercializacao).delete()
    db.commit()

