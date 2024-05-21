from typing import List
from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from schemas.producao import CreateProducao, ShowProducao
from db.repository.producao import create_new_producao, list_producao,delete_producao

router = APIRouter()

@router.get("",response_model=List[ShowProducao])
def get_all_producao(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        delete_producao(db=db)
        create_new_producao(db=db)
        producao = list_producao(db=db)
    except:
        raise HTTPException(
            detail="Error import data",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return producao


