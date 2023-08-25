import sqlite3
from pathlib import Path

#limpa os dados da tabela e zera o indice (DELETE sozinho apneas limpa, mas não zera os ids)
def limpar_table(table, conexao, cursor):
    cursor.execute(f'DELETE FROM {table}')
    cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table}"')
    conexao.commit()


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR/DB_NAME

TABLE_NAME = 'customer'

#abrindo conexão e criando cursor
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#criando tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
    'nome TEXT NOT NULL, '
    'peso REAL NOT NULL'
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
insert_data = f'INSERT INTO {TABLE_NAME} (nome, peso) VALUES (?, ?)'

cursor.executemany(insert_data, (['Luiz', 87], ['Marcia', 44], ['Duilio', 66]))
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