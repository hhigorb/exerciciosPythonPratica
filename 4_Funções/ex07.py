"""
Elabore uma função que receba um número inteiro e retorne o fatorial deste número.
"""


def fatorial(numero):
    controle_fatorial = 1
    for i in range(1, numero+1):
        controle_fatorial *= i
    return controle_fatorial


print(fatorial(7))