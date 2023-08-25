lista_duplicados = [4, 6, 7, 9, 0 , 9, 4, 22]

duplicados = 0
lista_duplicados_copia = lista_duplicados.copy()
for i, item in enumerate(lista_duplicados_copia):
    duplo = 0
    for i2, item2 in enumerate(lista_duplicados_copia):
        if item == item2 and i != i2:
            duplo += 1
            lista_duplicados_copia.pop(i2)
            
    if duplo > 0:
        duplicados += 1
print('ACABOU')
print(f'Foram encontrados {duplicados} itens duplicados')
print(f'Lista Original: {lista_duplicados}')
print(f'Lista sem itens duplicados: {lista_duplicados_copia}')



