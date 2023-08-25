minha_lista = []
indice_apagar = ''
lista_add = ''
while True:
    print("")
    print("#"*60)
    opcao = input("Selecione uma opção: [I]nserie, [D]eletar, [L]istar ").lower()

    if opcao == 'i':
        lista_add = input("O que deseja adicionar? ")
        minha_lista.append(lista_add)

    elif opcao == 'd':
        try:
            indice_apagar = int(input("Qual o índice do item que deseja apagar? "))
        except:
            print("Insira apenas números!")
            continue
        if indice_apagar > (len(minha_lista)-1):
            print("Índice inexistente")
            continue
        else:
            minha_lista.pop(indice_apagar)

    elif opcao == 'l':
        if not minha_lista:
            print("Lista Vazia!")
            continue
        else:
            for item in minha_lista:
                print(item)

    else:
        print("Selecione uma opção válida!")
        continue
