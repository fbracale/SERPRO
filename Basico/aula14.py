import json

dados = {
    'Nome': 'Felipe',
    'Sobrenome': 'Bracale',
    'Idade': 34,
    'Nota': 62,
    'segundaFase': True
}

json_serpro = 'aula14_json.json'
with open(json_serpro, 'w', encoding='utf8') as file:
    json.dump(dados, file, indent=2)


