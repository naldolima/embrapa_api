import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "API Embrapa"
    PROJECT_VERSION: str = "1.0.0"

    # postgresql

    #POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    #POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    #POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    #POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432)
    #POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    #DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # sqlite
    DATABASE_URL : str = os.getenv("SQLITE_URL")

    # token
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # url site embrapa
    URL_PRODUCAO: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    URL_PROCESSAMENTO: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    URL_COMERCIALIZACAO: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    URL_IMPORTACAO: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    URL_EXPORTACAO: str = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"

settings = Settings()
