import sqlite3


def get_user_info(username):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Código vulnerável a SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result


# Exemplo de uso
username = input(
    "Digite o nome de usuário: "
)  # Aqui o usuário pode inserir um payload SQL, como ' OR '1'='1
user_info = get_user_info(username)
print(user_info)
