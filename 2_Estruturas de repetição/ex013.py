"""
Escreva um programa que peça ao usuário 20 números reais e ao final mostre a soma e a média dos números digitados.
"""

soma = 0

for i in range(1, 21):
    n = int(input(f'Digite o {i} número: '))
    soma += n

print(f'A soma é: {soma} e a média: {soma / 20}')