def BubbleSort(lista):
    for index_final in range(len(lista), 0, -1):
        for index in range(0, index_final-1):
            if lista[index] > lista[index+1]:
                print(lista)
                lista[index+1], lista[index] = lista[index], lista[index+1]
    return lista

numeros = [4,7,2,8,5,11,0,-1,7]
print(BubbleSort(numeros))