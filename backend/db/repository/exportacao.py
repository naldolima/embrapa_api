from sqlalchemy.orm import Session
from db.models.exportacao import Exportacao
from core.config import settings
from db.embrapa_site import get_field_1,get_field_2,get_field_3
import re

def create_new_exportacao(db: Session):

    paises = get_field_1(settings.URL_EXPORTACAO)
    quantidades = get_field_2(settings.URL_EXPORTACAO)
    valores = get_field_3(settings.URL_EXPORTACAO)

    for i in range(len(paises)):
        pais = paises[i].replace("\n", "").strip(" ")
        qtd = "".join(re.findall("\d+", quantidades[i]))
        val = "".join(re.findall("\d+", valores[i]))

        if qtd == '':
            qtd = 0

        if val == '':
            val = 0

        exportacao = Exportacao(
            pais=pais,
            quantidade=int(qtd),
            valor=int(val)
        )

        db.add(exportacao)
        db.commit()
        db.refresh(exportacao)


def list_exportacao(db: Session):
    exportacao = db.query(Exportacao).all()
    return exportacao

def delete_exportacao(db: Session):
    db.query(Exportacao).delete()
    db.commit()

