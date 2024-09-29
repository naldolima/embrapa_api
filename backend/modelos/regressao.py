import pandas as pd
import sqlite3
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

connection = sqlite3.connect("../embrapa.db")
cursor = connection.cursor()
query = ("SELECT prod.produto,prod.quantidade as qtd_producao, com.quantidade as qtd_comercializacao"
         ", pros.quantidade as qtd_processamento FROM producao prod inner join comercializacao com on "
         "prod.produto = com.produto inner join processamento pros on prod.produto = pros.cultivar")

cursor.execute(query)
result = cursor.fetchall()
connection.close()

df = pd.DataFrame(result, columns=["produto","qtd_producao", "qtd_comercializacao", "qtd_processamento"])

x = df[["qtd_producao", "qtd_comercializacao","qtd_processamento"]]
y = df["produto"]

min_max_scaler = StandardScaler()
x = min_max_scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x , y,test_size=0.3,random_state=23)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

file = open("../data/data_metric.csv","w")
file.write("acuracia\n")
file.write(str(accuracy))
file.close()

df.to_csv('../data/data_base.csv',index=False)
pd.DataFrame(y_test, columns=["produto"]).to_csv('../data/data_test.csv',index=False)
pd.DataFrame(y_pred,columns=["produto"]).to_csv('../data/data_predict.csv',index=False)
