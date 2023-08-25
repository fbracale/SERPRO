public class bubblesort {
    public static int[] BubbleSort(int[] lista){
        int index_max = lista.length-1;
        boolean troca;

        for (int i = index_max; i > 0; i--){
            troca = false;
            for (int j = 0; j < index_max; j++){
                if (lista[j] > lista[j+1]) {
                    int temp = lista[j];
                    lista[j] = lista[j+1];
                    lista[j+1] = temp;
                    troca = true;
                }
            }
            if (!troca) {
                break;
            }
        }
        return lista;
    }

    public static void main(String[] args) {
    
    int[] numbers = {4,5,2,1,8,0,7,2};
    for (int num : numbers) 
        System.out.println(num + " ");
    BubbleSort(numbers);
    for (int num : numbers) 
        System.out.println(num + " ");

    }
}



