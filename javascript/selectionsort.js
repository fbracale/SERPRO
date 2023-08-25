function selectionSort(lista) {
    const index_maximo = lista.length -1;

    for (i = 0; i < index_maximo; i++) {
        let index_menor_valor = i;

        for (j = i+1; j <= index_maximo; j++) {
            if (lista[j] < lista[index_menor_valor]) {
                index_menor_valor = j;
            }
        }
        [lista[i], lista[index_menor_valor]] = [lista[index_menor_valor], lista[i]];
        console.log(lista);
    }
    return lista;
}

let numeros = [7, 5, 2, 0, 4, 9, 3]

let result = selectionSort(numeros)
console.log("Resultado")
console.log(result)

