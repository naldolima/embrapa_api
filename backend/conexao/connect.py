import sqlite3

connection = sqlite3.connect("../embrapa.db")

# Criação do cursor, elemento que "aponta" para os dados e permite percorrê-los
cursor = connection.cursor()

# Definição da string de busca no banco de dados
query = "SELECT * FROM comercializacao"

# Execução da consulta pelo cursor
cursor.execute(query)

# Extração dos resultados
result = cursor.fetchall()

connection.close()


for row in result:
    print(row)