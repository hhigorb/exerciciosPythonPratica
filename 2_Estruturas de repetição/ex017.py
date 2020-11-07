"""
Escreva um programa que peça números inteiros positivos indefinidamente e armazene-os em uma lista. O programa
deverá ser encerrado caso o número digitado seja negativo ou nulo. Ao final mostre na tela a quantidade
números pares e ímpares.
"""

valores = []
pares = 0
impares = 0

while True:
    n = int(input('Digite um número: '))
    if n > 0:
        valores.append(n)
    else:
        print('Encerrando o programa...')
        break

for i in valores:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}\n'
      f'Quantidade de ímpares: {impares}')