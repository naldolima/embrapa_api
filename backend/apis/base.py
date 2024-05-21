from fastapi import APIRouter
from apis.v1 import route_user
from apis.v1 import route_login
from apis.v1 import route_producao
from apis.v1 import route_processamento
from apis.v1 import route_comercializacao
from apis.v1 import route_importacao
from apis.v1 import route_exportacao



api_router = APIRouter()

api_router.include_router(route_user.router,prefix="/users", tags=["users"])
api_router.include_router(route_login.router,prefix="", tags=["login"])
api_router.include_router(route_producao.router,prefix="/producao", tags=["producao"])
api_router.include_router(route_comercializacao.router,prefix="/comercializacao", tags=["comercializacao"])
api_router.include_router(route_processamento.router,prefix="/processamento", tags=["processamento"])
api_router.include_router(route_importacao.router,prefix="/importacao", tags=["importacao"])
api_router.include_router(route_exportacao.router,prefix="/exportacao", tags=["exportacao"])

