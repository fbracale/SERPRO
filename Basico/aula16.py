import json

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('Felipe', 34)
p2 = Pessoas('Laiane', 28)
p3 = Pessoas('Ana', 1)

print(p1.nome)
print(p1.idade)
print(p2.nome)
print(p2.idade)
print(p3.nome)
print(p3.idade)

lista = []
lista.append(vars(p1))
lista.append(vars(p2))
lista.append(vars(p3))

with open('aula16.json', 'w') as file:
    json.dump(lista, file, indent=2)