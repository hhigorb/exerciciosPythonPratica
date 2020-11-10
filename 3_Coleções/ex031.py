"""
Utilize Compreensão em Lista (List Comprehension) para criar as listas a seguir.

a)

[(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7), (13, 8), (14, 9)]

b)

[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

"""

print([(x, y) for x, y in enumerate(range(10), start=5)])

print([(x, x ** 2) for x in range(10)])