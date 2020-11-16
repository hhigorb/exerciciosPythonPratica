"""
Faça as seguintes modificações na classe Conta do exercício anterior:

Crie o método extrato, para registrar e mostrar na tela as operações efetuadas (tipo, valor e data);

Crie o método resumo, para mostrar na tela o titular e o saldo da conta.
"""

from datetime import datetime


class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        self.__extrato = []

    def depositar(self, valor):
        if valor > 10:
            self.__saldo += valor
            data = datetime.today().strftime('%d/%m/%Y')
            self.__extrato.append(['Deposito', valor, data])
        else:
            print(f'O valor de depósito precisa ser maior que R$ 10,00.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
        else:
            print(f'Saldo insuficiente para realizar operação!')

    def extrato(self):
        for operacao in self.__extrato:
            print(f'Data: {operacao[2]}')
            print(f'Operação: {operacao[0]}')
            print(f'Valor: R$ {operacao[2]:.2f}')
            print()

    @property
    def retorna_saldo(self):
        return f'Saldo de: {self.__saldo}'

    @property
    def resumo(self):
        return self.__dict__


santander = Conta('Higor', 5000)
santander.depositar(5000)
print(santander.resumo)


