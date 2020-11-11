"""
Escreva uma função que verifique se um número é múltiplo do outro e retorne um valor lógico.
"""


def multiplo(v1, v2):
    if v1 % v2 == 0:
        return True
    return False


print(multiplo(2, 3))