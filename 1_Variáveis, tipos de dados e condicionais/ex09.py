"""
Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao
final o programa deverá mostrar na tela a área da circunferência.

Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.

Dica: você pode usar a biblioteca math para pegar a constante pi.
"""

raio = int(input('Digite o valor do raio do círculo: '))

print(f'A área equivale a: {3.14* raio ** 2}')