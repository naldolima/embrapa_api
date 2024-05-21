from typing import List
from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from schemas.comercializacao import CreateComercializacao, ShowComercializacao
from db.repository.comercializacao import create_new_comercializacao, list_comercializacao,delete_comercializacao

router = APIRouter()

@router.get("",response_model=List[ShowComercializacao])
def get_all_comercializacao(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        delete_comercializacao(db=db)
        create_new_comercializacao(db=db)
        comercializacao = list_comercializacao(db=db)
    except:
        raise HTTPException(
            detail="Error import data",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return comercializacao


