"""
Faça um programa que peça uma temperatura em Farenheit (F) e converta esta temperatura para grau Celsius (C),
mostrando o resultado da conversão na tela.

Use a fórmula: C = 5 * ((F-32) / 9).
"""

f = int(input('Temperatura em Fahrenheit: '))
c = 5*((f-32)/9)
print(f'{f}° F equivale a {c:.2f}° C')