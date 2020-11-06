"""
Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.

Dica: utilize o módulo math.
"""

from math import log
n = int(input('Digite um valor: '))

print(f'Base 2: {log(n, 2):.2f}\n'
      f'Base 10: {log(n, 10):.2f}')

