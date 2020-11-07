"""
Considere um número inteiro positivo n especificado pelo usuário. Elabore um programa que calcule e mostre na tela:

A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;

A soma dos n primeiros números pares;

A soma dos n primeiros números ímpares.
"""

soma = 0
soma_pares = 0
soma_impares = 0

n = int(input('Digite um número: '))

for i in range(1, n+1):
    soma += i
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f'Soma total: {soma}\n'
      f'Soma pares: {soma_pares}\n'
      f'Soma impares: {soma_impares}')


