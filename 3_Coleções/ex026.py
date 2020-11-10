"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir. Ademais, tente resolver este
problema sem usar Compreensão em Lista.

[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""

lista = []

for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            lista.append((x, y))

print(lista)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])