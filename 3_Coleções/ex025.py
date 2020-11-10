"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Condição: eleve o número ao
quadrado se for par; se o número for ímpar calcule a raiz quadrada - utilize round() para arredondar as casas decimais.

1.0, 4, 1.73, 16, 2.24, 36, 2.65, 64, 3.0, 100, 3.32, 144, 3.61, 196, 3.87, 256, 4.12, 324, 4.36, 400, 4.58, 484,
4.8, 576, 5.0, 676, 5.2, 784, 5.39, 900, 5.57, 1024, 5.74, 1156, 5.92, 1296, 6.08, 1444, 6.24, 1600, 6.4, 1764, 6.56,
1936, 6.71, 2116, 6.86, 2304, 7.0, 2500]

Lembre que:

[f(x) for x in sequence if condition]
[f(x) if condition else g(x) for x in sequence]
"""

from math import sqrt

print([numero ** 2 if numero % 2 == 0 else round(sqrt(numero)) for numero in range(0, 100)])
