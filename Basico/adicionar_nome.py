import random
from pathlib import Path
import sqlite3

nomes = ["José", "João", "Antônio", "Francisco", "Carlos", "Paulo",
"Pedro", "Lucas", "Luiz", "Marcos", "Luis", "Gabriel", "Rafael", "Daniel",
"Marcelo", "Bruno", "Eduardo", "Felipe", "Raimundo", "Rodrigo", "Maria",
"Ana", "Francisca", "Antônia", "Adriana", "Juliana", "Márcia", "Fernanda",
"Patrícia", "Aline", "Sandra", "Camila", "Amanda", "Bruna", "Jéssica",
"Letícia", "Júlia", "Luciana", "Vanessa", "Mariana"]

sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues",
"Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro",
"Martins", "Carvalho", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira",
"Barbosa"]

ROOT_DIR = Path(__file__).parent
CSV = ROOT_DIR/'nomes.csv'
DATABASE = ROOT_DIR/'nomes.sqlite3'

'''
with open(CSV, 'w', encoding='utf8') as file:
    for i in range(1000):
        nome_aleatorio = random.choice(nomes)
        sobrenome_aleatorio = random.choice(sobrenomes)
        file.write(f'{nome_aleatorio} {sobrenome_aleatorio}\n')
'''

lista_nomes = []
with open(CSV, 'r', encoding='utf8') as file:
    for linha in file:
        lista_nomes.append(linha.strip())

sem_repeticao = list(set(lista_nomes))

print(f'Número de nomes na lista comum: {len(lista_nomes)}')
print(f'Número de nomes na lista sem repetições: {len(sem_repeticao)}')


conexao = sqlite3.connect(DATABASE)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS "nomes"(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT)')

for name in sem_repeticao:
    nome, *sobrenome = name.split()
    sobrenome = ' '.join(sobrenome)
    cursor.execute('INSERT INTO nomes(nome, sobrenome) VALUES (?, ?)', (nome, sobrenome))
conexao.commit()

cursor.close()
conexao.close()