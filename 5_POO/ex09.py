"""
Na classe Conta, do exercício anterior, incremente os métodos Depositar e Sacar, verificando se o valor inserido é
válido. No caso do último método, verifique se há dinheiro suficiente no saldo da conta. Crie objetos para testar
a sua implementação.
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
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
        else:
            print(f'Saldo insuficiente para realizar operação!')

    @property
    def retorna_saldo(self):
        return f'Saldo de: {self.__saldo}'


santander = Conta('Higor', 5000)
santander.sacar(0)
