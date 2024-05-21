from typing import List
from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from schemas.importacao import CreateImportacao, ShowImportacao
from db.repository.importacao import create_new_importacao, list_importacao,delete_importacao

router = APIRouter()

@router.get("",response_model=List[ShowImportacao])
def get_all_importacao(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        delete_importacao(db=db)
        create_new_importacao(db=db)
        importacao = list_importacao(db=db)
    except:
        raise HTTPException(
            detail="Error import data",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return importacao


