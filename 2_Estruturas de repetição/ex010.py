"""
Escreva um programa que peça ao usuário números entre 0-10. Se o usuário inserir um número fora desse intervalo
o programa deverá finalizar com uma mensagem personalizada.
"""

while True:
    n = int(input('Digite um número entre 0-10: '))
    if n < 0 or n > 10:
        print(f'O número deve entre 0-10!')
        break
