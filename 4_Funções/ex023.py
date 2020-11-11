"""
a) Use list() e zip() para criar uma nova lista de tuplas a partir da lista1 e lista2.

lista1=[1,2,3,4]
lista2=['Python','JavaScript','Java','HTML']

output:

[(1, 'Python'), (2, 'JavaScript'), (3, 'Java'), (4, 'HTML')]

b) Use list() e zip() para criar uma nova lista de tuplas a partir da lista1 e lista2.

lista1=[40,50,60,70,80]
lista2=[-4,2,0,50,1]

output:

[(40, -4), (50, 2), (60, 0), (70, 50), (80, 1)]
"""

lista1 = [1, 2, 3, 4]
lista2 = ['Python', 'JavaScript', 'Java', 'HTML']

# a)

print(list(zip(lista1, lista2)))

lista1 = [40, 50, 60, 70, 80]
lista2 = [-4, 2, 0, 50, 1]

# b)

print(list(zip(lista1, lista2)))



