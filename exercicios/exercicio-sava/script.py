import sqlite3 as connector

connection = connector.connect("mydatabase.db")  # Conecta-se ao banco de dados ou cria um novo se ele não existir
cursor = connection.cursor()  # Cria conexão do Cursor

cursor.execute(  # Cria a tabela "students" com as colunas "nome" e "grade"
    "CREATE TABLE students (nome TEXT, grade INTEGER)"
)

# Insere alguns dados na tabela
cursor.execute("INSERT INTO students (nome, grade) VALUES (?, ?)", ("Alice", 95))
cursor.execute("INSERT INTO students (nome, grade) VALUES (?, ?)", ("Bob", 84))
cursor.execute("INSERT INTO students (nome, grade) VALUES (?, ?)", ("Charlie", 72))

connection.commit()  # Salva as alterações no banco de dados
connection.close()  # Encerra a conexão com o banco de dados
cursor.close()  # Encerra conexão do Cursor