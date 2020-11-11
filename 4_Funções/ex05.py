"""
Escreva um programa que pesquise um determinado valor em uma lista. Sua função deve ter como parâmetros a lista
e o valor a ser verificado. Caso o valor faça parte da lista informada retorne True e False, caso contrário.
"""


def verifica(lista, valor):
    for i in lista:
        if i == valor:
            return True
    return False


print(verifica([3, 2, 1, 2], 2))


