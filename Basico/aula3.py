while True:

    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")

    try:
        n1 = float(numero1)
        n2 = float(numero2)
    except:
        print("Alguns dos número é inválido")
        continue

    print("Números válidos!")

