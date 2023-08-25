caminho_arquivo = 'aula13.txt'

# arquivo = open(caminho_arquivo,'w')
# arquivo.close

with open(caminho_arquivo, 'a') as arquivo:
    arquivo.write('Ola mundo!')