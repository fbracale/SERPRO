import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB = 'db.sqlite3'
DB_PATCH = ROOT_DIR/DB
TABLE_NAME = 'new_customer'

conexao = sqlite3.connect(DB_PATCH)

cursor = conexao.cursor()


cursor.execute(
	f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, nota REAL)')
conexao.commit()

conexao.execute(f'DELETE FROM {TABLE_NAME}')
conexao.commit()

sql = f'INSERT INTO {TABLE_NAME} (nome, nota) VALUES (?, ?)'
valores = (('Valesca', 9.0),('Jussara', 6.0))
valores2 = ('Dolores Carolina', 6.0)

cursor.executemany(sql, valores)
cursor.execute(sql, valores2)
conexao.commit()

cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE nome="Valesca"')
cursor.execute(f'UPDATE {TABLE_NAME} SET nota=7.5, nome="Jussara Valoesca" WHERE nome="Jussara"')

conexao.commit()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for item in cursor.fetchall():
    print(item)

cursor.close()
conexao.close()
