def zipper (l1, l2):
    nova_lista = []
    i = 0
    i_max = len(l1) if len(l2) > len(l1) else len(l2)
    while i < i_max:
        nova_lista.append((l1[i], l2[i]))
        i += 1

    return nova_lista


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Cabo Frio', 'Araçatuba']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista1, lista2))



