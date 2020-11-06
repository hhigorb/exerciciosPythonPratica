"""
Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'O maior número é: {maior}')