#Lista de tarefas CRUD: Create, Read, Update e Delete integrado com o MySQL (Banco de dados).

import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "bdexemplo"
)

cursor = conexao.cursor()

#CREATE

nome_produto = "chocolate"
valor = 10

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#READ

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

#UPDATE

nome_produto = "toddynho"
valor = 6

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE

nome_produto = "toddynho"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()
