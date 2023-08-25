"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC



class Conta(ABC):
    def __init__(self, agencia, numero_conta):
        self.agencia = agencia
        self.conta = numero_conta
        self._saldo = 0.00

    def sacar(self, valor):
        ...

    def depositar (self, valor):
        valor = round(float(valor), 2)
        self._saldo += valor
        return print(f'Depositado R${valor:.2f}')
    
    def verificar_saldo(self):
        print(f'Seu saldo é de R${self._saldo:.2f}')

class ContaCorrente (Conta):
    _limite = 1000.00
    def sacar(self, valor):
        if valor < self._saldo:
            print(f'SACANDO R${valor:.2f}...')
        elif valor < (self._saldo + self._limite):
            uso_limite = valor - self._saldo
            print(f'Para sacar esse valor você irá ultilizar R${uso_limite:.2f} do seu limite')
            print(f'SACANDO R${valor:.2f}...')
        else:
            acima_limite = valor - (self._saldo + self._limite)
            print(f'Não é possível sacar R${valor:.2f} da sua conta corrente. Está acima de R${acima_limite:.2f} do seu limite')
            return False
        self._saldo -= valor


class ContaPoupanca (Conta):
    def sacar(self, valor):
        if valor < self._saldo:
            print(f'SACANDO R${valor:.2f}...')
        else:
            print(f'Não é possível sacar R${valor:.2f}. Você só tem R${self._saldo:.2f} na sua conta poupança')
            return False
        self._saldo -= valor


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._idade = idade
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, nome):
        self._nome = nome

class Cliente(Pessoa):
    ...

# c1 = ContaCorrente(144, 35662)
# c1.verificar_saldo()
# c1.depositar(500)
# c1.verificar_saldo()
# c1.sacar(410.55)
# c1.verificar_saldo()
# c1.sacar(488.77)
# c1.verificar_saldo()
# c1.sacar(10)
# c1.verificar_saldo()
# c1.sacar(1500)
# c1.verificar_saldo()

# c2 = ContaPoupanca(143, 356)
# c2.depositar(1200)
# c2.verificar_saldo()
# c2.sacar(800)
# c2.verificar_saldo()
# c2.sacar(755)
# c2.verificar_saldo()

l1 = Cliente('Jose', 14)
print(l1.nome)
l1.nome = 'a'
print(l1.nome)