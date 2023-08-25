nome = input("Qual o seu nome? ")
novo_nome = ""
contador = 0

while contador < len(nome):
    novo_nome += "*"+nome[contador]
    contador += 1

print("Seu nome era: ", nome)
print("Seu novo nome é: ", novo_nome)

