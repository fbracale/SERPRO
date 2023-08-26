def EPalindromo(texto: str):
    texto_novo = texto.strip().lower().replace(' ','').replace('.','').replace(',','').replace('!','').replace('-','')
    print(texto_novo)
    if texto_novo == texto_novo[::-1]:
        print(f'A frase "{texto}" é um palindromo!')
        return True
    print(f'A frase "{texto}" NÃO é um palindromo!')
    return False


frase = 'A cara rajada da jararaca'
frase2 = 'Socorram-me, subi no onibus em Marrocos!'
EPalindromo(frase)