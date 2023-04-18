import sqlite3


def search_students(name=None, grade=None):
    # Conecta-se ao banco de dados ou cria um novo se ele não existir
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()

    # Monta a consulta SQL com base nos parâmetros especificados pelo usuário
    query = "SELECT * FROM students"
    params = []
    if name is not None:
        query += " WHERE name LIKE ?"
        params.append("%" + name + "%")
    if grade is not None:
        if len(params) == 0:
            query += " WHERE grade = ?"
        else:
            query += " AND grade = ?"
        params.append(grade)

    # Executa a consulta SQL e retorna os resultados
    cursor.execute(query, params)
    results = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    connection.close()

    return results


# Exemplo de uso
results = search_students(name="Alice", grade=95)
for row in results:
    print(row)
