"""
Implemente uma função recursiva para imprimir o n-ésimo termo da sequência Fibonacci.
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(3))