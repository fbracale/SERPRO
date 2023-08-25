import json

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

lista = []

with open('aula16.json', 'r') as file:
    lista = json.load(file)


print(lista)

p1 = Pessoas(**lista[0])

print(vars(p1))
print(p1.idade, p1.nome )
