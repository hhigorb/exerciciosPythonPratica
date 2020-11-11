"""
Escreva uma função para checar se uma lista é vazia ou não.
"""


def vazio(lista):
    return not len(lista) > 0


print(vazio([3, 2, 1, 2, 3]))
print(vazio([]))