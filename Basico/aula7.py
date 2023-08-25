#retorna todos arguentos passados no método e os multiplica
def multiplicador (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(multiplicador(2, 5, 7, 1, 2))

def par_impar (a):
    return "Par" if a % 2 == 0 else "Impar"

print(par_impar(3386))