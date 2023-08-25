function bubbleSort(lista) {

    const index_maximo = lista.length-1;

    for (i = index_maximo; i>0; i--){
        for(j = 0; j<i; j++){
            if(lista[j] > lista[j+1]){
                console.log(lista);
                [lista[j], lista[j+1]] = [lista[j+1], lista[j]];
            }
        }
    }
    return lista
}

let numeros = [7, 5, 2, 0, 4, 9, 3]

let result = bubbleSort(numeros)
console.log("Resultado")
console.log(result)

