"""
Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.

Dica: utilize o módulo math do Python, especificamente math.fatorial.
"""

from math import factorial

n = int(input('Digite um número: '))

print(f'O fatorial de {n} é {factorial(n)}')