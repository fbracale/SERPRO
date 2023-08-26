public class palindromo {
    public static boolean EPalindromo(String texto){
        String novo_texto = texto.strip().replace(" " , "").replace("," , "").replace("." , "").replace("-" , "").toLowerCase();
        System.out.println(novo_texto);
        int tamanho_frase = novo_texto.length();
        String novo_texto_reverso = "";
        for (int i = tamanho_frase - 1; i>=0; i--){
            novo_texto_reverso += novo_texto.charAt(i);
        }
        System.out.println(novo_texto);
        System.out.println(novo_texto_reverso);
        if (novo_texto.equals(novo_texto_reverso)){
            System.out.println("A frase '" + texto + "' É um palindromo");
            return true;
        }
        System.out.println("A frase '" + texto + "' NÃO é um palindromo");
        return false;
    }
        public static void main(String[] args) {
            String frase = "A cara rajada da jaararaca";
            boolean resposta = EPalindromo(frase);
        }
}
