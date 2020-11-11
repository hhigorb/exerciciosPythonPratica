"""
Escreva uma função que retorna o tamanho de uma string.
"""


def tamanho(string):
    total = 0
    for caracter in string:
        total += 1
    return total


print(tamanho('Texto'))