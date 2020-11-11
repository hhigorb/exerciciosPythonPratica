"""
Escreva uma função que receba uma lista de números reais como parâmetro e retorne a média destes números.
"""


def media(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma / len(lista)


print(media([3, 2, 1, 2, 3, 4, 5]))

