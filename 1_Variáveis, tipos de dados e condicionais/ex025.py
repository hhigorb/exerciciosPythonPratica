"""
Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado.
Considere a possibilidade de o usuário digitar dois números iguais.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print(f'Os números são iguais')