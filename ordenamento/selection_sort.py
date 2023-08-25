def SelectionSort(lista):
    for index in range(len(lista)):
        index_menor_valor = index

        for index_direita in range(index+1, len(lista)):
            if lista[index_direita] < lista[index_menor_valor]:
                index_menor_valor = index_direita
        lista[index], lista[index_menor_valor] = lista[index_menor_valor], lista[index]
        print(lista)
    return lista

numeros = [4,7,2,8,5,11,0,-1,7]
print(SelectionSort(numeros))
