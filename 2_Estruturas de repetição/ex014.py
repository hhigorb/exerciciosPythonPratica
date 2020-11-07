"""
Elabore um programa que calcule e mostre na tela os números pares entre 1 e 200. Os números devem ser mostrados
na tela de acordo com o formato a seguir:
"""

for i in range(1, 201):
    if i % 2 == 0:
        print(i, end=' ')
