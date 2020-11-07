"""
Escreva um programa que peça números reais (float) do usuário indefinidamente . Caso os números digitados
não estejam situados entre 0 e 10 o programa deverá ser finalizado, mostrando a soma e a quantidade de
números digitados.
"""

soma = 0
quantidade = 0

while True:
    n = float(input('Digite um número: '))
    if n < 0 or n > 10:
        print(f'Você deve digitar números entre 0-10!')
        break
    else:
        quantidade += 1
        soma += n

print(f'Quantidade de números digitados: {quantidade}\n'
      f'Soma dos números digitados: {soma}')
