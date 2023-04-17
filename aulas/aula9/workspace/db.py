import os
import sqlite3 as conector

dirname = os.path.dirname(__file__)
url = os.path.join(dirname, 'mysql.db')


conexao = conector.connect(url)
cursor = conexao.cursor()

sql = (
    #query
)

cursor.execute(sql)

cursor.close()
conexao.close()