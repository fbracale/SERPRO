from abc import ABC

class CalculadoraAbstrata(ABC):
    def parser(self, entrada:str):
        numero1, *operacao, numero2 = entrada.split()
        # print(numero1)
        # print(operacao)
        # print(numero2)

        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
        except ValueError:
            print('Entrada inválida!')
            return None 

        if 'menos' in operacao:
            return numero1 - numero2
        elif 'mais' in operacao:
            return numero1 + numero2
        elif 'dividido' in operacao:
            return numero1 / numero2
        elif 'vezes' in operacao:
            return numero1 * numero2
        elif 'elevado' in operacao:
            return numero1 ** numero2

class CalculadoraConsole(CalculadoraAbstrata):
    def main(self):
        print('Bem vindo a Calculadora de console!')
        print('#'*82)
        print('# Escreva no formato: Numero1 operação Numero2')
        print('# EX: 4 mais 5')
        print('# Operaçoes disponíveis: "mais", "menos", "dividido por", "vezes", "elevado a"')
        print('#'*82)
        calculo = input('Digite sua operação: ')
        resultado = self.parser(calculo)
        print(resultado)


if __name__ == '__main__':

    # c1 = CalculadoraAbstrata
    # print(c1.parser('3 menos 3'))

    # numero = 'a'
    # rtet = int(numero)

    c2 = CalculadoraConsole()
    c2.main()


