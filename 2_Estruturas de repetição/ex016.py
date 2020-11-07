"""
Escreva um programa que peça um número inteiro do usuário e mostre na tela o fatorial deste número.
"""

n = int(input('Digite um número: '))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i


print(f'{n}! = {fatorial}')