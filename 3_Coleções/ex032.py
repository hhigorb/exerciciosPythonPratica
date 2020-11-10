"""
A partir da lista

matriz=[[1,2,3], [4,5,6], [7,8,9]]
Use List Comprehension e obtenha:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

Na sequência utilize a função sum() para obter a soma destes números.
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(sum([numero for linha in matriz for numero in linha]))