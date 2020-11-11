"""
Escreva uma função que verifique se duas listas possuem ao menos um elemento em comum, retornando True em caso positivo.
"""


def verifica(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False


print(verifica([1, 2, 3, 4, 5, 6], [10]))


