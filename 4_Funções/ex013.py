"""
Escreva uma função que faça uma cópia de uma lista.
"""


def copiar_lista(lista):
    copia = []
    if type(lista) == list:
        for elemento in lista:
            copia.append(elemento)
        return copia
    else:
        return copia


print(copiar_lista([]))
