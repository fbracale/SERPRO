import json

with open('aula14_json.json', 'r') as file:
    dados_json = json.load(file)

print (dados_json)

for i in dados_json:
    print (i+': '+str(dados_json[i]))
