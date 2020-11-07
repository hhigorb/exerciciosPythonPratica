"""
Escreva um programa para checar se um determinado número é primo ou não.

Lembrete: um número primo pode ser dividido por apenas dois números, quais sejam: ele mesmo e o número um.



2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 e 97  (Números primos
entre 1 e 100)
"""

divisoes = 0

n = int(input('Digite um número: '))

for i in range(1, n+1):
    if n % i == 0:
        divisoes += 1

if divisoes == 2:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')
