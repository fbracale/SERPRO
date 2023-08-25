while loop == True:
    valor1 = input("Digite um valor: ")
    loop = False if valor1.isnumeric else print("Isso não é um número!")
    valor2 = input("Digite outro valor: ")


if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor1 < valor2:
    print(f"{valor1} é menor que {valor2}")
else:
    print(f"{valor1} é igual a {valor2}")