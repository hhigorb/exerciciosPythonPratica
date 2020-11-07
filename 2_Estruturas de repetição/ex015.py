"""
Elabore um programa que calcule e mostre na tela os números ímpares entre 1 e 200. Os números devem ser mostrados na
tela de acordo com o formato a seguir:
"""

for i in range(1, 201):
    if i % 2 == 1:
        print(i, end=' ')