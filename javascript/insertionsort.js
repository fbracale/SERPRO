function InsertionSort(lista){
    const index_maximo = lista.length;

    for (i = 0; i < index_maximo; i++){
        let j = i;
        while (j > 0){
            if (lista[j-1] > lista[j]){
                [lista[j-1], lista[j]] = [lista[j], lista[j-1]];
            }
            j--;
        }
    }
    return lista;
}

let numeros = [7, 5, 2, 0, 4, 9, 3];

let result = InsertionSort(numeros);
console.log("Resultado");
console.log(result);
