"""
Escreva um programa que peça 5 números inteiros não-nulos ao usuário e mostre na tela o quadrado de cada número
digitado.

"""

lista = []
for i in range(1, 6):
    num = int(input(f'Número {i}: '))
    if num > 0:
        lista.append(num)

for i in lista:
    print(f'{i} ** 2 = {i ** 2}')