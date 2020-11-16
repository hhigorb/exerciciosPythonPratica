"""
Crie uma classe Conta para simular as operações de uma conta corrente. Sua classe deverá ter os seguintes atributos:

Titular;

Saldo (atributo privado).

E os seguintes métodos:

Depositar;

Sacar;

Retornar saldo.

Crie um objeto da classe Conta e teste o atributos e métodos implementados.
"""


class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 10:
            self.__saldo += valor
        else:
            print(f'O valor de depósito precisa ser maior que R$ 10,00.')

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print(f'Saldo insuficiente para realizar operação!')

    @property
    def retorna_saldo(self):
        return f'Saldo de: {self.__saldo}'


bradesco = Conta('Larissa', 5000)
print(bradesco.__dict__)
bradesco.depositar(1000)
print(bradesco.__dict__)
bradesco.sacar(5000)





