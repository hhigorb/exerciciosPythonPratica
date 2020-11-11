"""
Escreva uma função para checar se um determinado ano é bissexto.
"""


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return 'É bissexto'
    return 'Não é bissexto'


print(bissexto(1948))