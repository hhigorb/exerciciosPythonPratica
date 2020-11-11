"""
Crie uma função que recebe um número e verifique se este é par. Posteriormente, use a função filter() para criar
uma lista com todos os números pares de 1 a 50.

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
"""


def par(n):
    if n % 2 == 0:
        return True
    return False


print(list(filter(lambda n: par(n), range(1, 51))))