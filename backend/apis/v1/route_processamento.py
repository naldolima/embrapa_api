from typing import List
from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from apis.v1.route_login import get_current_user
from schemas.processamento import CreateProcessamento, ShowProcessamento
from db.repository.processamento import create_new_processamento, list_processamento,delete_processamento

router = APIRouter()

@router.get("",response_model=List[ShowProcessamento])
def get_all_processamento(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:
        delete_processamento(db=db)
        create_new_processamento(db=db)
        processamento = list_processamento(db=db)
    except:
        raise HTTPException(
            detail="Error import data",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return processamento


