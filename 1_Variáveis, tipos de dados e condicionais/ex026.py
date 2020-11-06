"""
Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.
"""

n = int(input('Digite um número: '))

if n > 0:
    print(f'{n} é positivo.')
elif n < 0:
    print(f'{n} é negativo.')
else:
    print(f'{n} é nulo.')