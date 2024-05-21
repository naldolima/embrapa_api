from typing import List
from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from schemas.exportacao import CreateExportacao, ShowExportacao
from db.repository.exportacao import create_new_exportacao, list_exportacao,delete_exportacao

router = APIRouter()

@router.get("",response_model=List[ShowExportacao])
def get_all_exportacao(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        delete_exportacao(db=db)
        create_new_exportacao(db=db)
        exportacao = list_exportacao(db=db)
    except:
        raise HTTPException(
            detail="Error import data",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return exportacao


