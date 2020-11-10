"""
Use compreensão de dicionários e obtenha os dicionários a seguir:

a)

{2: 1.0, 4: 2.0, 6: 2.585, 8: 3.0, 10: 3.322, 12: 3.585, 14: 3.807, 16: 4.0, 18: 4.17, 20: 4.322}

Dica: este dicionário calcula o logaritmo de base 2 para todos os números pares no intervalo [1,20].

b)

{'C': 3, 'E': 5, 'F': 6, 'I': 9, 'J': 10, 'L': 12, 'O': 15, 'R': 18, 'T': 20}
"""

# a)
from math import log

print({chave: round(log(chave, 2), 3) for chave in range(1, 21) if chave % 2 == 0})

# b)

print({chr(64+num):num for num in range(1,21) if num%5==0 or num%3==0})


