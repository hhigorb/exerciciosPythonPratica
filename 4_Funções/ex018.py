"""
a) Utilize a função map() para criar uma lista com o quadrado de cada número par e o cubo de cada número ímpar.
Considere o intervalo [1,20].


Output:


[(1, 1), (2, 4), (3, 27), (4, 16), (5, 125), (6, 36), (7, 343), (8, 64), (9, 729), (10, 100), (11, 1331),
(12, 144), (13, 2197), (14, 196), (15, 3375), (16, 256), (17, 4913), (18, 324), (19, 6859), (20, 400)]


b) Utilize a função map() para criar uma lista com o os números divisíveis por 3 e 5, no intervalo [1,50].
Se o número não for divisível calcule sua raiz quadrada.


Output:



[1.0, 1.41, 3, 2.0, 5, 6, 2.65, 2.83, 9]
"""

# a)

a = map(lambda n: (n, n ** 2) if n % 2 == 0 else (n, n ** 3), range(1, 21))
print(list(a))

# b)

b = map(lambda n: n if (n % 3 == 0 or n % 5 == 0) else round(n ** 0.5, 2), range(1, 51))
print(list(b))
