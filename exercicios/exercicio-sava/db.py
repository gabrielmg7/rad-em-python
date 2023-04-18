import sqlite3

# Conecta-se ao banco de dados ou cria um novo se ele não existir
connection = sqlite3.connect("mydatabase.db")

# Cria a tabela "students" com as colunas "name" e "grade"
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (name TEXT, grade INTEGER)")

# Insere alguns dados na tabela
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 95))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Bob", 84))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Charlie", 72))

# Salva as alterações no banco de dados
connection.commit()

# Fecha a conexão com o banco de dados
connection.close()
