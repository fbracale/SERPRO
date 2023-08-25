def saudacao (msg, nome):
    return f"Olá {nome}, {msg}"

def executar (funcao, *args):
    return funcao(*args)

print(executar(saudacao, 'boa tarde', 'Felipe'))


def multiplicador (multiplicador):
    def valor(numero):
        return numero*multiplicador
    return valor

duplica = multiplicador(2)
triplica = multiplicador(3)

print(duplica(7))
print(triplica(9))


