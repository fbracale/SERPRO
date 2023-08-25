def zipper (l1, l2):
    i_max = min(len(l1), len(l2))
    return [l1[i] + l2[i] for i in range(i_max)]


lista1 = [1, 8, 5, 2, 0, 7, 9]
lista2 = [5, 7, 9, 5, 3]

print(zipper(lista1, lista2))