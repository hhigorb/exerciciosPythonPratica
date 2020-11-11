"""
Crie uma função que recebe um número e verifique se este é primo. Posteriormente, use a função filter() para criar
uma lista com todos os números pares de 1 a 50.


[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""


def primo(n):
    divisoes = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisoes += 1
    if divisoes == 2:
        return True
    return False


print(list(filter(lambda n: primo(n), range(1, 51))))