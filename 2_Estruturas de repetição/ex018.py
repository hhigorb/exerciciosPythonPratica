"""
Elabore um programa que embaralhe a lista a seguir e mostre na tela cada elemento.

lista=['A','B','C','D','E','F','G','H','I','J','K','L','M']

O output do programa pode seguir o padrão abaixo:

A
C
B
K
J
F
M
D
H
G
L
I
E
"""

from random import shuffle

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
shuffle(lista)

for letra in lista:
    print(letra)
