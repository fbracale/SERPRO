# validador de cpf

while True:
    #cpf_user = input("Qual o número do CPF? ")
    cpf_user = "391.065.058-99"

    cpf_9digitos = ""
    cpf_10digitos = ""
    cpf_completo = ""
    cpf_validador = ""
    cpf_somaDigito1 = 0
    cpf_somaDigito2 = 0
    multiplicador1 = 10
    multiplicador2 = 11
    digito1 = 0
    digito2 = 0

    for digito in cpf_user:
        if digito.isdecimal():
            cpf_completo += digito
    if len(cpf_completo) != 11:
        print("CPF informado não contém 11 digitos!")
        continue

    print(f"CPF informado: {cpf_user}")
    print(f"CPF desformatado: {cpf_completo}")

    # for digito in cpf_user:
    #     if digito.isdecimal() and len(cpf_9digitos) < 9: 
    #         cpf_9digitos += digito

    cpf_9digitos = cpf_completo[:9]
    # print(cpf_9digitos) 

    # 3*10 = 30 / 9*9 = 81 / 1*8 = 8 / 0*7 = 0 / # 6*6 = 36 / 0*5 = 0 / 0*4 = 0 / 5*3 = 15 / 8*2 = 16
    #Total = 186
    #cpf_soma_esperado = 3*10+9*9+1*8+0*7+6*6+0*5+0*4+5*3+8*2
    #print(cpf_soma_esperado)

    for numero in cpf_9digitos:
        cpf_somaDigito1 += int(numero)*multiplicador1
        multiplicador1 -= 1

    # print(cpf_somaDigito1)

    cpf_somaDigito1 *= 10
    # print(cpf_somaDigito1)

    cpf_somaDigito1 %= 11
    # print(cpf_somaDigito1)

    digito1 = 0 if cpf_somaDigito1 > 9 else cpf_somaDigito1
    print(f"O 1º digito é {digito1}")

    cpf_10digitos = cpf_9digitos + str(digito1)
    for numero in cpf_10digitos:
        cpf_somaDigito2 += int(numero)*multiplicador2
        multiplicador2 -= 1

    # print(cpf_somaDigito2)

    cpf_somaDigito2 *= 10
    # print(cpf_somaDigito2)

    cpf_somaDigito2 %= 11
    # print(cpf_somaDigito2)

    digito2 = 0 if cpf_somaDigito2 > 9 else cpf_somaDigito2
    print(f"O 2º digito é {digito2}")
    
    cpf_validador = cpf_10digitos + str(digito2)

    print(f"O CPF {cpf_user} é válido") if cpf_validador == cpf_completo else print(f"O CPF {cpf_user} é inválido")
    break
