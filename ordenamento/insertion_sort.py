def InsertionSort(lista):
    for index in range(0, len(lista)):
        while index > 0:
            if lista[index-1] > lista[index]:
                lista[index], lista[index-1] = lista[index-1], lista[index]
            index -= 1
            print(lista)
    return lista

numeros = [4,7,2,8,5,11,0,-1,7]
print(InsertionSort(numeros))