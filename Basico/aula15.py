import json

comando = ''
lista = []
lista_refazer = []
json_file = 'aula15-dados.json'

try:
    with open(json_file, 'r') as file:
        lista = json.load(file)
except FileNotFoundError:
    print ('Arquivo "aula15-dados.json" não encontrado')
    print()

while True:
    print('Comandos: listar, desfazer, refazer, sair')
    comando = str(input('Digite uma tarefa para adicionar ou um comando: ')).lower().strip()
    if comando == 'listar':
        print()
        for item in lista:
            print(item)
        print()
    elif comando == 'desfazer':
        if not lista:
            print()
            print('Nada a desfazer')
            print()
            continue
        print()
        print('DESFAZENDO')
        print()
        lista_refazer.append(lista.pop()) 
    elif comando == 'refazer':
        if not lista_refazer:
            print()
            print('Nada a refazer')
            print()
            continue
        print()
        print('REFAZENDO')
        lista.append(lista_refazer.pop())
        print()
    elif comando == 'sair':
        with open(json_file, 'w', encoding='utf8') as file:
            json.dump(lista, file, indent=2)
        break
    else:
        lista.append(comando)
