"""
Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada (multiplicação) de
um número inserido pelo usuário.
"""

n = int(input('Digite um número: '))

for i in range(11):
    print(f'{n} x {i} = {n * i}')