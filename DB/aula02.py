import pymysql

#funcao para limpar tabela inteira (e zerar os id novamente//DELETE limpa tbm mas não zera id)
def limpar_table(table, conexao, cursor):
    cursor.execute(f'TRUNCATE TABLE {table}')
    conexao.commit()

TABLE_NAME = 'customer'

#abrindo conexão e criando cursor
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_dados'
)
cursor = connection.cursor()

#criando tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, '
    'nome VARCHAR(50) NOT NULL, '
    'peso INT NOT NULL'
    ')'
)
connection.commit()

#limpando dados da tabela e zerando o indice
limpar_table(TABLE_NAME, connection, cursor)


#inserindo dados direto na tabela
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} '
#     '(nome, peso) VALUES'
#     '("Helena", 46), ("Jopger", 97.5)'
# )
# connection.commit()

#deletando dados na tabela
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME} '
#     'WHERE nome="Helena"'
# )
# connection.commit()


#adicionando dados na tabela
insert_data = f'INSERT INTO {TABLE_NAME} (nome, peso) VALUES (%s, %s)'
data = (('Luiz', 87), ('Maria', 16))
cursor.executemany(insert_data, data)
connection.commit()

#lendo osdados
cursor.execute(f'SELECT * FROM {TABLE_NAME}')
data_retrieve = cursor.fetchall()
# print(data_retrieve)
for row in data_retrieve:
    print(row)


#fechando conexão
cursor.close()
connection.close()